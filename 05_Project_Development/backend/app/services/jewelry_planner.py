import json
from typing import Dict, Any, Optional
from PIL import Image
from sqlalchemy.orm import Session

from .gemini_service import gemini_service
from ..models import Recommendation, User

def plan_jewelry_ensemble(
    budget: float,
    occasion: str,
    style_preference: str,
    pil_image: Optional[Image.Image] = None,
    user: Optional[User] = None,
    db: Optional[Session] = None
) -> Dict[str, Any]:
    """Coordinates jewelry ensemble generation, vision analysis, and optional persistence."""
    result = gemini_service.generate_jewelry_plan(
        budget=budget,
        occasion=occasion,
        style_preference=style_preference,
        pil_image=pil_image
    )

    rec_id = None
    if user and db:
        rec = Recommendation(
            user_id=user.id,
            category="jewelry",
            title=result["title"],
            budget=result["budget"],
            total_estimated_cost=result["total_estimated_cost"],
            remaining_budget=result["remaining_budget"],
            details=json.dumps(result),
            is_sample_data=result["is_sample_data"]
        )
        db.add(rec)
        db.commit()
        db.refresh(rec)
        rec_id = rec.id

    result["id"] = rec_id
    return result

