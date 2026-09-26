import random
from typing import List, Dict, Any, Optional
from ..utils.budget_utils import audit_and_cap_budget, compute_party_budget_split, compute_home_budget_split

class MockService:
    """
    Deterministic Heuristic Generator.
    Produces high-fidelity, schema-compliant recommendations when the Google Gemini API
    is unreachable, out of quota, or when running offline without an API key.
    All links are transparently marked as mock/sample.
    """

    @staticmethod
    def generate_home_recommendations(
        budget: float,
        room_type: str,
        style: str,
        required_items: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        splits = compute_home_budget_split(budget)
        furniture_budget = splits["key_furniture"]
        lighting_budget = splits["lighting"]
        decor_budget = splits["decor_and_rugs"]

        # Curate items based on room and style
        clean_style = style.strip().title()
        clean_room = room_type.strip().title()

        items = [
            {
                "name": f"{clean_style} Ergonomic Statement Sofa",
                "category": "Key Furniture",
                "quantity": 1,
                "estimated_price": round(furniture_budget * 0.65, 2),
                "description": f"A refined {clean_style.lower()} focal couch tailored for a {clean_room.lower()} layout with stain-resistant fabric.",
                "vendor_link": "https://www.ikea.com/sample/statement-sofa",
                "link_type": "mock_sample"
            },
            {
                "name": f"{clean_style} Solid Oak Coffee Table",
                "category": "Key Furniture",
                "quantity": 1,
                "estimated_price": round(furniture_budget * 0.35, 2),
                "description": f"Sleek architectural coffee table complementing the {clean_style.lower()} design language.",
                "vendor_link": "https://www.target.com/sample/coffee-table",
                "link_type": "mock_sample"
            },
            {
                "name": f"Dimmable Arc Brass Floor Lamp",
                "category": "Ambient Lighting",
                "quantity": 1,
                "estimated_price": round(lighting_budget * 0.70, 2),
                "description": "Warm-spectrum 2700K ambient floor luminaire with matte brass finish.",
                "vendor_link": "https://www.westelm.com/sample/arc-lamp",
                "link_type": "mock_sample"
            },
            {
                "name": f"Minimalist Accent Table Lamp",
                "category": "Ambient Lighting",
                "quantity": 1,
                "estimated_price": round(lighting_budget * 0.30, 2),
                "description": "Ceramic base table lamp providing focused reading illumination.",
                "vendor_link": "https://www.cb2.com/sample/accent-lamp",
                "link_type": "mock_sample"
            },
            {
                "name": f"Handwoven Wool Area Rug (8x10)",
                "category": "Decor & Accents",
                "quantity": 1,
                "estimated_price": round(decor_budget * 0.60, 2),
                "description": f"Geometric natural fiber rug anchoring the {clean_room.lower()}.",
                "vendor_link": "https://www.rugsusa.com/sample/wool-rug",
                "link_type": "mock_sample"
            },
            {
                "name": f"Curated Botanical Wall Art (Set of 3)",
                "category": "Decor & Accents",
                "quantity": 1,
                "estimated_price": round(decor_budget * 0.40, 2),
                "description": f"Framed minimalist giclée prints reinforcing the {clean_style.lower()} color story.",
                "vendor_link": "https://www.etsy.com/sample/wall-art-set",
                "link_type": "mock_sample"
            }
        ]

        audited_items, total_spent, remaining = audit_and_cap_budget(items, budget)

        return {
            "title": f"{clean_style} {clean_room} Budget Roadmap",
            "budget": round(budget, 2),
            "total_estimated_cost": total_spent,
            "remaining_budget": remaining,
            "is_sample_data": True,
            "items": audited_items,
            "budget_breakdown": {
                "Key Furniture": round(furniture_budget, 2),
                "Lighting": round(lighting_budget, 2),
                "Decor & Accents": round(decor_budget, 2)
            },
            "design_tips": [
                f"Anchor the {clean_room.lower()} by aligning the front legs of the sofa on the area rug.",
                "Layer illumination by combining overhead, floor, and table lighting for depth.",
                f"Stick to 3 core complementary tones matching the {clean_style.lower()} aesthetic to avoid visual clutter."
            ]
        }

    @staticmethod
    def generate_party_recommendations(
        occasion: str,
        budget: float,
        guest_count: int,
        venue_type: str
    ) -> Dict[str, Any]:
        allocations = compute_party_budget_split(budget, guest_count, venue_type)
        clean_occ = occasion.strip().title()
        per_head = round(budget / max(guest_count, 1), 2)

        items = [
            {
                "name": f"Gourmet Buffet & Finger Food Catering ({guest_count} Pax)",
                "category": "Catering & Refreshments",
                "quantity": guest_count,
                "estimated_price": round(allocations["catering_and_drinks"] * 0.65, 2),
                "description": f"Assorted artisan appetizers, skewers, sliders, and dessert bites for {clean_occ}.",
                "vendor_link": "https://sample-catering.local/menu",
                "link_type": "mock_sample"
            },
            {
                "name": "Craft Mocktail & Beverage Station Set",
                "category": "Catering & Refreshments",
                "quantity": 1,
                "estimated_price": round(allocations["catering_and_drinks"] * 0.35, 2),
                "description": "Drink dispensers, fresh garnishes, ice tubs, and artisanal syrups.",
                "vendor_link": "https://sample-drinks.local/station",
                "link_type": "mock_sample"
            },
            {
                "name": f"Thematic Arch & Table Decor Ensemble",
                "category": "Decorations & Ambience",
                "quantity": 1,
                "estimated_price": round(allocations["decorations"] * 0.70, 2),
                "description": f"Cohesive backdrop arch, organic balloon/floral garland, and table runners for {clean_occ}.",
                "vendor_link": "https://sample-decor.local/backdrop",
                "link_type": "mock_sample"
            },
            {
                "name": "Warm Fairy Light & Ambient Lantern Strings",
                "category": "Decorations & Ambience",
                "quantity": 4,
                "estimated_price": round(allocations["decorations"] * 0.30, 2),
                "description": "Waterproof outdoor-rated LED fairy lights to establish celebration mood.",
                "vendor_link": "https://sample-decor.local/lights",
                "link_type": "mock_sample"
            },
            {
                "name": "Tables, Folding Chairs & Linen Rental Package",
                "category": "Venue & Rentals",
                "quantity": 1,
                "estimated_price": allocations["venue_and_rentals"],
                "description": f"Seating arrangements accommodating {guest_count} guests comfortably.",
                "vendor_link": "https://sample-rentals.local/seating",
                "link_type": "mock_sample"
            },
            {
                "name": "High-Output Bluetooth Sound System & Curated Playlist Setup",
                "category": "Entertainment & Favors",
                "quantity": 1,
                "estimated_price": round(allocations["entertainment_and_favors"] * 0.60, 2),
                "description": "Wireless portable PA speaker with dual microphones for toasts and music.",
                "vendor_link": "https://sample-av.local/speaker-rentals",
                "link_type": "mock_sample"
            },
            {
                "name": f"Custom Keepsake Party Favors ({guest_count} units)",
                "category": "Entertainment & Favors",
                "quantity": guest_count,
                "estimated_price": round(allocations["entertainment_and_favors"] * 0.40, 2),
                "description": f"Personalized commemorative favors thanking guests for attending.",
                "vendor_link": "https://sample-favors.local/custom",
                "link_type": "mock_sample"
            }
        ]

        audited_items, total_spent, remaining = audit_and_cap_budget(items, budget)

        return {
            "title": f"{clean_occ} Celebration Plan ({guest_count} Guests)",
            "budget": round(budget, 2),
            "total_estimated_cost": total_spent,
            "per_guest_cost": per_head,
            "remaining_budget": remaining,
            "is_sample_data": True,
            "allocations": allocations,
            "items": audited_items,
            "checklist": [
                f"Confirm guest RSVP count 5 days before the event (target: {guest_count}).",
                f"Schedule rental delivery for chairs and tables 4 hours before guest arrival.",
                "Set up the beverage and mocktail station 1 hour prior to kickoff.",
                "Test Bluetooth audio connectivity and microphone batteries.",
                "Chill all refreshments and prep ice storage bins."
            ]
        }

    @staticmethod
    def generate_jewelry_recommendations(
        budget: float,
        occasion: str,
        style_preference: str,
        has_image: bool = False
    ) -> Dict[str, Any]:
        clean_occ = occasion.strip().title()
        clean_style = style_preference.strip().title()

        # Decide metal based on style
        if "gold" in clean_style.lower() or "royal" in clean_style.lower() or "traditional" in clean_style.lower():
            metal = "18K Yellow Gold Vermeil"
            gem = "Emerald & Freshwater Pearl"
        elif "silver" in clean_style.lower() or "modern" in clean_style.lower() or "minimalist" in clean_style.lower():
            metal = "Rhodium-Plated 925 Sterling Silver"
            gem = "Brilliant Moissanite & Blue Topaz"
        else:
            metal = "Rose Gold & Platinum Duo"
            gem = "Swarovski Pavé Crystal"

        items = [
            {
                "name": f"{clean_style} Statement Chandelier Earrings",
                "category": "Earrings",
                "quantity": 1,
                "estimated_price": round(budget * 0.38, 2),
                "description": f"Artisanal earrings crafted in {metal}, accented with {gem}.",
                "vendor_link": "https://www.bluenile.com/sample/earrings",
                "link_type": "mock_sample"
            },
            {
                "name": f"Delicate Layered Pendant Necklace",
                "category": "Necklace",
                "quantity": 1,
                "estimated_price": round(budget * 0.34, 2),
                "description": f"Adjustable fine-chain necklace designed to rest flatteringly along the collarbone.",
                "vendor_link": "https://mejuri.com/sample/pendant",
                "link_type": "mock_sample"
            },
            {
                "name": f"Slim Stackable Cuff Bangle",
                "category": "Bracelets",
                "quantity": 1,
                "estimated_price": round(budget * 0.16, 2),
                "description": f"Polished minimalist {metal} cuff providing graceful wrist movement.",
                "vendor_link": "https://www.gorjana.com/sample/cuff",
                "link_type": "mock_sample"
            },
            {
                "name": f"Pavé Accented Solitaire Band",
                "category": "Rings",
                "quantity": 1,
                "estimated_price": round(budget * 0.12, 2),
                "description": f"Micro-pavé gem band finishing the ensemble with refined sparkle.",
                "vendor_link": "https://www.catbirdnyc.com/sample/ring",
                "link_type": "mock_sample"
            }
        ]

        audited_items, total_spent, remaining = audit_and_cap_budget(items, budget)

        vision_analysis = {
            "image_processed": has_image,
            "detected_colors": ["Harmonizing Neutral Base", "Vibrant Accent Tones"] if has_image else ["Classic Evening Palette"],
            "neckline_detected": "V-Neck / Collar Opening" if has_image else "Standard Formal Cut",
            "aesthetic_profile": f"Tailored {clean_occ} Elegance with {clean_style} flair"
        }

        return {
            "title": f"{clean_style} Jewelry Ensemble for {clean_occ}",
            "budget": round(budget, 2),
            "total_estimated_cost": total_spent,
            "remaining_budget": remaining,
            "is_sample_data": True,
            "vision_analysis": vision_analysis,
            "recommended_metal": metal,
            "items": audited_items,
            "styling_advice": (
                f"For {clean_occ.lower()}, balance your silhouette by letting the {items[0]['name']} "
                f"be the hero piece. The {metal} tone warms your skin tone and harmonizes effortlessly."
            )
        }

