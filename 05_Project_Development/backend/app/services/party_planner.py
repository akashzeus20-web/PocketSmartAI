import json
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session

from .gemini_service import gemini_service
from ..models import Recommendation, User

def plan_party_event(
    occasion: str,
    budget: float,
    guest_count: int,
    venue_type: str,
    user: Optional[User] = None,
    db: Optional[Session] = None
) -> Dict[str, Any]:
    """Coordinates party planning generation, per-guest math, and optional persistence."""
    result = gemini_service.generate_party_plan(
        occasion=occasion,
        budget=budget,
        guest_count=guest_count,
        venue_type=venue_type
    )

    rec_id = None
    if user and db:
        rec = Recommendation(
            user_id=user.id,
            category="party",
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

