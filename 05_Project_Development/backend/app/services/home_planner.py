import json
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session

from .gemini_service import gemini_service
from ..models import Recommendation, User

def plan_home_interior(
    budget: float,
    room_type: str,
    style: str,
    required_items: List[str],
    user: Optional[User] = None,
    db: Optional[Session] = None
) -> Dict[str, Any]:
    """Coordinates home interior generation, budget capping, and optional persistence."""
    result = gemini_service.generate_home_plan(
        budget=budget,
        room_type=room_type,
        style=style,
        required_items=required_items
    )

    rec_id = None
    if user and db:
        rec = Recommendation(
            user_id=user.id,
            category="home",
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

