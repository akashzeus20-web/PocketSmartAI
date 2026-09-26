from datetime import datetime
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, EmailStr, Field, ConfigDict

# --- User & Auth Schemas ---

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=6, description="Password (min 6 characters)")

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: Optional[UserOut] = None

class SessionInfo(BaseModel):
    authenticated: bool
    user_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    session_active: bool = False


# --- Generic Item Schema ---

class BudgetItem(BaseModel):
    name: str
    category: str
    quantity: int = 1
    estimated_price: float
    description: str
    vendor_link: str = "https://example.com/item"
    link_type: str = "mock_sample"  # 'mock_sample' or 'live_listing'


# --- Home Planner Schemas ---

class HomePlannerRequest(BaseModel):
    budget: float = Field(..., gt=0, description="Total budget in USD")
    room_type: str = Field(..., min_length=2, description="Target room (e.g., Living Room, Bedroom)")
    style: str = Field(..., min_length=2, description="Design aesthetic (e.g., Scandinavian, Industrial)")
    required_items: List[str] = Field(default_factory=list, description="List of required furniture/decor items")

class HomePlannerResponse(BaseModel):
    id: Optional[int] = None
    category: str = "home"
    title: str
    budget: float
    total_estimated_cost: float
    remaining_budget: float
    is_sample_data: bool = False
    items: List[BudgetItem]
    budget_breakdown: Dict[str, float] = Field(default_factory=dict)
    design_tips: List[str] = Field(default_factory=list)
    created_at: Optional[datetime] = None


# --- Party Planner Schemas ---

class PartyPlannerRequest(BaseModel):
    occasion: str = Field(..., min_length=2, description="Event occasion (e.g., Birthday, Anniversary)")
    budget: float = Field(..., gt=0, description="Total party budget in USD")
    guest_count: int = Field(..., ge=1, description="Expected number of attendees")
    venue_type: str = Field(default="Home / Backyard", description="Indoor, Backyard, Rented Hall, etc.")

class PartyPlannerResponse(BaseModel):
    id: Optional[int] = None
    category: str = "party"
    title: str
    budget: float
    total_estimated_cost: float
    per_guest_cost: float
    remaining_budget: float
    is_sample_data: bool = False
    allocations: Dict[str, float] = Field(default_factory=dict)
    items: List[BudgetItem]
    checklist: List[str] = Field(default_factory=list)
    created_at: Optional[datetime] = None


# --- Jewelry Planner Schemas ---

class JewelryPlannerRequest(BaseModel):
    budget: float = Field(..., gt=0, description="Total jewelry budget in USD")
    occasion: str = Field(..., min_length=2, description="Occasion (e.g., Wedding, Gala, Casual)")
    style_preference: str = Field(..., min_length=2, description="Style (e.g., Minimalist, Royal Antique)")

class VisionAnalysis(BaseModel):
    image_processed: bool = False
    detected_colors: List[str] = Field(default_factory=list)
    neckline_detected: Optional[str] = None
    aesthetic_profile: Optional[str] = None

class JewelryPlannerResponse(BaseModel):
    id: Optional[int] = None
    category: str = "jewelry"
    title: str
    budget: float
    total_estimated_cost: float
    remaining_budget: float
    is_sample_data: bool = False
    vision_analysis: Optional[VisionAnalysis] = None
    recommended_metal: str = "Yellow Gold / Silver"
    items: List[BudgetItem]
    styling_advice: str = ""
    created_at: Optional[datetime] = None


# --- History Schemas ---

class RecommendationSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: Optional[int] = None
    category: str
    title: str
    budget: float
    total_estimated_cost: float
    remaining_budget: float
    is_sample_data: bool
    created_at: datetime


class RecommendationDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: Optional[int] = None
    category: str
    title: str
    budget: float
    total_estimated_cost: float
    remaining_budget: float
    is_sample_data: bool
    details: Dict[str, Any]
    created_at: datetime

