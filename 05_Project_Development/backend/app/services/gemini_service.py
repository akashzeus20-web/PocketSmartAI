import json
import logging
from typing import Optional, Dict, Any, List
from PIL import Image

import google.generativeai as genai
from ..config import settings
from ..utils.budget_utils import audit_and_cap_budget, compute_party_budget_split, compute_home_budget_split
from .mock_service import MockService

logger = logging.getLogger("pocketsmart.gemini")

class GeminiService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY.strip() if settings.GEMINI_API_KEY else ""
        self.model_name = settings.GEMINI_MODEL
        if self.api_key:
            genai.configure(api_key=self.api_key)
            logger.info("Google Gemini configured with provided API key.")
        else:
            logger.warning("No GEMINI_API_KEY configured. MockService heuristic fallback will be utilized.")

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key and len(self.api_key) > 5)

    def _clean_json_response(self, text: str) -> Dict[str, Any]:
        """Strips markdown code blocks and loads json."""
        clean = text.strip()
        if clean.startswith("```json"):
            clean = clean[7:]
        elif clean.startswith("```"):
            clean = clean[3:]
        if clean.endswith("```"):
            clean = clean[:-3]
        clean = clean.strip()
        return json.loads(clean)

    def generate_home_plan(
        self,
        budget: float,
        room_type: str,
        style: str,
        required_items: List[str]
    ) -> Dict[str, Any]:
        """Generates home interior recommendations using Gemini 1.5 Flash."""
        if not self.is_configured:
            return MockService.generate_home_recommendations(budget, room_type, style, required_items)

        items_str = ", ".join(required_items) if required_items else "sofa, coffee table, lighting, area rug"
        prompt = f"""
You are an expert interior designer and budget optimization AI for PocketSmart AI.
Create a detailed, balanced shopping and furnishing plan within a STRICT budget ceiling.

USER CONSTRAINTS:
- Total Budget: ${budget:.2f} USD
- Target Room Type: {room_type}
- Aesthetic Style: {style}
- Priority Required Items: {items_str}

CRITICAL RULES:
1. The sum of (estimated_price * quantity) for all items MUST be LESS THAN OR EQUAL to ${budget:.2f}.
2. Group items across categories: Key Furniture, Ambient Lighting, Decor & Accents.
3. For each item provide:
   - "name": Descriptive product title
   - "category": Category string
   - "quantity": Integer (usually 1)
   - "estimated_price": Numeric float in USD
   - "description": Why it fits the room and style
   - "vendor_link": A realistic sample search URL (e.g. "https://www.ikea.com/sample/item" or "https://www.target.com/sample/item")
   - "link_type": Always "mock_sample"
4. Include "budget_breakdown": map of category to total spent.
5. Include "design_tips": list of 3 practical layout/styling tips.

Respond ONLY with a valid JSON object matching this structure:
{{
  "title": "{style} {room_type} Plan",
  "items": [
    {{
      "name": "...",
      "category": "...",
      "quantity": 1,
      "estimated_price": 0.0,
      "description": "...",
      "vendor_link": "https://www.ikea.com/sample/...",
      "link_type": "mock_sample"
    }}
  ],
  "budget_breakdown": {{
    "Key Furniture": 0.0,
    "Lighting": 0.0,
    "Decor & Accents": 0.0
  }},
  "design_tips": ["...", "..."]
}}
"""
        try:
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            data = self._clean_json_response(response.text)
            items = data.get("items", [])
            audited_items, total_spent, remaining = audit_and_cap_budget(items, budget)

            return {
                "title": data.get("title", f"{style} {room_type} Plan"),
                "budget": round(budget, 2),
                "total_estimated_cost": total_spent,
                "remaining_budget": remaining,
                "is_sample_data": False,
                "items": audited_items,
                "budget_breakdown": data.get("budget_breakdown", compute_home_budget_split(budget)),
                "design_tips": data.get("design_tips", ["Layer lighting for warmth", "Coordinate textures"])
            }
        except Exception as e:
            logger.warning(f"Gemini API call failed ({e}). Gracefully falling back to MockService.")
            return MockService.generate_home_recommendations(budget, room_type, style, required_items)

    def generate_party_plan(
        self,
        occasion: str,
        budget: float,
        guest_count: int,
        venue_type: str
    ) -> Dict[str, Any]:
        """Generates event and party planning recommendations."""
        if not self.is_configured:
            return MockService.generate_party_recommendations(occasion, budget, guest_count, venue_type)

        prompt = f"""
You are an expert event planner and budget strategist for PocketSmart AI.
Create a comprehensive party budget allocation and itemized checklist for:

EVENT CONSTRAINTS:
- Occasion: {occasion}
- Total Budget: ${budget:.2f} USD
- Expected Guests: {guest_count} attendees
- Venue Setting: {venue_type}

CRITICAL RULES:
1. Divide the budget across 4 pillars: Catering & Drinks (~45%), Venue & Rentals (~20%), Decorations (~20%), Entertainment & Favors (~15%).
2. The sum of all item costs MUST be <= ${budget:.2f}.
3. Provide itemized lines with "name", "category", "quantity", "estimated_price", "description", "vendor_link", "link_type": "mock_sample".
4. Calculate per-guest cost.
5. Provide a chronological 5-item prep checklist.

Respond ONLY with a valid JSON object matching this structure:
{{
  "title": "{occasion} Celebration Plan",
  "allocations": {{
    "catering_and_drinks": 0.0,
    "venue_and_rentals": 0.0,
    "decorations": 0.0,
    "entertainment_and_favors": 0.0
  }},
  "items": [
    {{
      "name": "...",
      "category": "...",
      "quantity": 1,
      "estimated_price": 0.0,
      "description": "...",
      "vendor_link": "https://sample-vendor.local/...",
      "link_type": "mock_sample"
    }}
  ],
  "checklist": ["...", "..."]
}}
"""
        try:
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(
                prompt,
                generation_config={"response_mime_type": "application/json"}
            )
            data = self._clean_json_response(response.text)
            items = data.get("items", [])
            audited_items, total_spent, remaining = audit_and_cap_budget(items, budget)
            per_guest = round(budget / max(guest_count, 1), 2)

            return {
                "title": data.get("title", f"{occasion} Celebration Plan"),
                "budget": round(budget, 2),
                "total_estimated_cost": total_spent,
                "per_guest_cost": per_guest,
                "remaining_budget": remaining,
                "is_sample_data": False,
                "allocations": data.get("allocations", compute_party_budget_split(budget, guest_count, venue_type)),
                "items": audited_items,
                "checklist": data.get("checklist", ["Confirm RSVP count", "Set up venue", "Test audio"])
            }
        except Exception as e:
            logger.warning(f"Gemini API call failed ({e}). Gracefully falling back to MockService.")
            return MockService.generate_party_recommendations(occasion, budget, guest_count, venue_type)

    def generate_jewelry_plan(
        self,
        budget: float,
        occasion: str,
        style_preference: str,
        pil_image: Optional[Image.Image] = None
    ) -> Dict[str, Any]:
        """Generates jewelry recommendations with optional multimodal image analysis."""
        if not self.is_configured:
            return MockService.generate_jewelry_recommendations(budget, occasion, style_preference, has_image=bool(pil_image))

        has_image = pil_image is not None
        vision_instruction = ""
        if has_image:
            vision_instruction = """
Analyze the attached outfit image:
1. Identify dominant colors and accent undertones.
2. Note the neckline cut (e.g. V-neck, sweetheart, boatneck, collar) and silhouette.
3. Recommend metal tones and gemstones that harmonize specifically with this attire.
"""

        prompt = f"""
You are a luxury jewelry stylist and gemologist for PocketSmart AI.
{vision_instruction}

PARAMETERS:
- Occasion: {occasion}
- Total Budget: ${budget:.2f} USD
- Preferred Style: {style_preference}

CRITICAL RULES:
1. Total sum of suggested jewelry items MUST be <= ${budget:.2f}.
2. Recommend pieces covering: Earrings, Necklace, Bracelets, and Rings.
3. Provide "recommended_metal" (e.g. 18K Yellow Gold, Platinum, Rhodium Silver).
4. Provide actionable "styling_advice".
5. All vendor links must have "link_type": "mock_sample".

Respond ONLY with a valid JSON object matching:
{{
  "title": "{style_preference} Jewelry Ensemble for {occasion}",
  "vision_analysis": {{
    "image_processed": {str(has_image).lower()},
    "detected_colors": ["..."],
    "neckline_detected": "...",
    "aesthetic_profile": "..."
  }},
  "recommended_metal": "...",
  "styling_advice": "...",
  "items": [
    {{
      "name": "...",
      "category": "Earrings / Necklace / Bracelets / Rings",
      "quantity": 1,
      "estimated_price": 0.0,
      "description": "...",
      "vendor_link": "https://www.bluenile.com/sample/...",
      "link_type": "mock_sample"
    }}
  ]
}}
"""
        try:
            model = genai.GenerativeModel(self.model_name)
            inputs = [prompt, pil_image] if pil_image else [prompt]
            response = model.generate_content(
                inputs,
                generation_config={"response_mime_type": "application/json"}
            )
            data = self._clean_json_response(response.text)
            items = data.get("items", [])
            audited_items, total_spent, remaining = audit_and_cap_budget(items, budget)

            return {
                "title": data.get("title", f"{style_preference} Jewelry Ensemble"),
                "budget": round(budget, 2),
                "total_estimated_cost": total_spent,
                "remaining_budget": remaining,
                "is_sample_data": False,
                "vision_analysis": data.get("vision_analysis", {
                    "image_processed": has_image,
                    "detected_colors": ["Custom Color Harmonization"],
                    "neckline_detected": "Appropriate Cut",
                    "aesthetic_profile": f"Styling for {occasion}"
                }),
                "recommended_metal": data.get("recommended_metal", "Yellow Gold / Vermeil"),
                "items": audited_items,
                "styling_advice": data.get("styling_advice", "Pair minimal pieces with statement elements.")
            }
        except Exception as e:
            logger.warning(f"Gemini API call failed ({e}). Gracefully falling back to MockService.")
            return MockService.generate_jewelry_recommendations(budget, occasion, style_preference, has_image=has_image)

gemini_service = GeminiService()

