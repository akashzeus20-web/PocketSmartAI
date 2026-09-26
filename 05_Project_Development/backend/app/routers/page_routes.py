from typing import Optional
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..config import settings
from ..models import User
from ..auth import get_optional_current_user

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))

@router.api_route("/", methods=["GET", "HEAD"], response_class=HTMLResponse)
def index_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"user": current_user, "active_tab": "home"}
    )


@router.get("/home-planner", response_class=HTMLResponse)
def home_planner_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="home_planner.html",
        context={"user": current_user, "active_tab": "home-planner"}
    )

@router.get("/party-planner", response_class=HTMLResponse)
def party_planner_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="party_planner.html",
        context={"user": current_user, "active_tab": "party-planner"}
    )

@router.get("/jewelry-planner", response_class=HTMLResponse)
def jewelry_planner_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={"user": current_user, "active_tab": "jewelry-planner"}
    )

@router.get("/history-view", response_class=HTMLResponse)
@router.get("/history-page", response_class=HTMLResponse)
def history_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={"user": current_user, "active_tab": "history"}
    )

@router.get("/details-page", response_class=HTMLResponse)
def details_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="details.html",
        context={"user": current_user, "active_tab": "history"}
    )

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"user": current_user, "active_tab": "login"}
    )

@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request, current_user: Optional[User] = Depends(get_optional_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={"user": current_user, "active_tab": "register"}
    )
