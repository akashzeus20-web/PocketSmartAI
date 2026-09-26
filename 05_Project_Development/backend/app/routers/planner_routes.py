import json
from typing import Optional, List
from fastapi import APIRouter, Depends, Form, File, UploadFile, Request
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas import (
    HomePlannerRequest, HomePlannerResponse,
    PartyPlannerRequest, PartyPlannerResponse,
    JewelryPlannerResponse
)
from ..auth import get_optional_current_user
from ..services.home_planner import plan_home_interior
from ..services.party_planner import plan_party_event
from ..services.jewelry_planner import plan_jewelry_ensemble
from ..utils.image_utils import process_and_validate_image

router = APIRouter(tags=["AI Planners"])

@router.post("/generate-home", response_model=HomePlannerResponse)
def generate_home(
    req: HomePlannerRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Generates intelligent home interior recommendations within budget.
    Automatically persists to user history if logged in.
    """
    result = plan_home_interior(
        budget=req.budget,
        room_type=req.room_type,
        style=req.style,
        required_items=req.required_items,
        user=current_user,
        db=db
    )
    return result


@router.post("/generate-party", response_model=PartyPlannerResponse)
def generate_party(
    req: PartyPlannerRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Generates party and event budget allocation and itemized checklist.
    Automatically persists to user history if logged in.
    """
    result = plan_party_event(
        occasion=req.occasion,
        budget=req.budget,
        guest_count=req.guest_count,
        venue_type=req.venue_type,
        user=current_user,
        db=db
    )
    return result


@router.post("/generate-jewelry", response_model=JewelryPlannerResponse)
async def generate_jewelry(
    budget: float = Form(..., description="Total budget for jewelry"),
    occasion: str = Form(..., description="Target occasion or event"),
    style_preference: str = Form(..., description="Style preference"),
    image: Optional[UploadFile] = File(None, description="Optional outfit photo"),
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Generates jewelry recommendations with optional multimodal outfit photo analysis.
    Automatically persists to user history if logged in.
    """
    pil_img = None
    if image and image.filename:
        processed = await process_and_validate_image(image)
        if processed:
            pil_img = processed[0]

    result = plan_jewelry_ensemble(
        budget=budget,
        occasion=occasion,
        style_preference=style_preference,
        pil_image=pil_img,
        user=current_user,
        db=db
    )
    return result

