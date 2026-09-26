# Phase 3: System Architecture & Design
## PocketSmart AI — Architectural Blueprint & Subsystem Decomposition

---

### 1. High-Level Architectural Pattern
PocketSmart AI adopts a **Layered Modular Micro-Monolith Architecture** with clean separation of concerns:
1. **Presentation Layer**: Client browser running responsive Jinja2-rendered templates enriched with vanilla ES6+ async JavaScript, CSS Grid/Flexbox design, Chart.js for data visualization, and toast notifications.
2. **API & Routing Layer**: FastAPI asynchronous ASGI server managing route dispatching, request deserialization, CORS policies, rate limiting, and HTTP status handling.
3. **Domain & Business Logic Layer**:
   * `HomePlannerService`: Implements room budget allocation rules, furniture priority matrices, and item bundling.
   * `PartyPlannerService`: Implements per-head economics, event venue ratios, and catering allocation algorithms.
   * `JewelryPlannerService`: Implements vision-based palette extraction, metal-to-fabric harmony models, and piece coordination.
   * `MockService`: High-fidelity deterministic heuristic engine guaranteeing zero downtime when offline or without external API keys.
4. **AI & Integration Layer**: Google Gemini Generative AI Client (`google-generativeai` SDK) utilizing Gemini 1.5 Flash for language reasoning and multimodal image inspection.
5. **Persistence & Data Layer**: SQLite relational database managed via SQLAlchemy ORM with foreign key cascades, connection pooling, and indexed lookups.

---

### 2. High-Level Architecture Diagram (Mermaid)

```mermaid
graph TD
    subgraph Client ["Client Presentation Tier (Browser)"]
        UI_Home[Home Planner UI]
        UI_Party[Party Planner UI]
        UI_Jewelry[Jewelry Planner UI + Image Upload]
        UI_Auth[Auth & Session Modals]
        UI_History[History & Details Viewer]
    end

    subgraph Backend ["FastAPI Application Server (Python 3.11)"]
        Router_Auth["Auth Router (/register, /login, /token, /session-info)"]
        Router_Home["Home Router (/generate-home)"]
        Router_Party["Party Router (/generate-party)"]
        Router_Jewel["Jewelry Router (/generate-jewelry)"]
        Router_Hist["History Router (/history, /recommendations-details)"]
        Router_Pages["Page Router (HTML Views)"]

        PydanticValidator["Pydantic v2 Validation & Sanitization"]
        AuthMiddleware["JWT Authentication & Security Context"]

        subgraph CoreServices ["Business Logic & Planners"]
            Svc_Home[HomePlanner Service]
            Svc_Party[PartyPlanner Service]
            Svc_Jewel[JewelryPlanner Service]
            Svc_Mock[Deterministic Fallback Heuristic Service]
        end

        subgraph Integration ["AI Integration Layer"]
            GeminiClient["Google Gemini 1.5 Flash SDK"]
        end
    end

    subgraph DataTier ["Persistence Tier"]
        DB[(SQLite Datastore)]
        UserTable[(Users Table)]
        RecTable[(Recommendations Table)]
    end

    subgraph ExternalCloud ["External AI Services"]
        GoogleAIStudio["Google AI Studio (Gemini 1.5 Flash / Pro)"]
    end

    Client -->|HTTP / JSON / Multipart| Backend
    Router_Auth --> AuthMiddleware
    Router_Home --> PydanticValidator --> Svc_Home
    Router_Party --> PydanticValidator --> Svc_Party
    Router_Jewel --> PydanticValidator --> Svc_Jewel
    Router_Hist --> AuthMiddleware --> RecTable

    Svc_Home --> GeminiClient
    Svc_Party --> GeminiClient
    Svc_Jewel --> GeminiClient

    Svc_Home -.->|On Exception / No Key| Svc_Mock
    Svc_Party -.->|On Exception / No Key| Svc_Mock
    Svc_Jewel -.->|On Exception / No Key| Svc_Mock

    GeminiClient -->|HTTPS REST / gRPC| GoogleAIStudio
    AuthMiddleware --> UserTable
    Svc_Home --> RecTable
    Svc_Party --> RecTable
    Svc_Jewel --> RecTable
```

---

### 3. Module Responsibilities

| Subsystem / Directory | Key Files | Responsibility |
| :--- | :--- | :--- |
| `backend/app/config.py` | `Settings` | Centralized Pydantic settings loading from `.env` (API keys, JWT secrets, DB path). |
| `backend/app/database.py` | `engine`, `Base`, `get_db` | SQLite connection setup, thread-safe session generator. |
| `backend/app/models.py` | `User`, `Recommendation` | SQLAlchemy database models with indexes and relationships. |
| `backend/app/schemas.py` | Pydantic Request/Response models | Enforces type contracts and validation constraints for all endpoints. |
| `backend/app/auth.py` | `create_access_token`, `get_current_user` | Bcrypt hashing, JWT generation, and dependency injection for protected routes. |
| `backend/app/services/` | `gemini_service.py`, `home_planner.py`, etc. | Core domain logic, prompt engineering, JSON schema parsing, and fallback mock generator. |
| `backend/app/routers/` | `auth_routes.py`, `planner_routes.py`, etc. | Endpoint definitions, HTTP status codes, error handling. |
| `frontend/templates/` | `base.html`, `home_planner.html`, etc. | Modular Jinja2 layouts with accessible components. |
| `frontend/static/` | CSS, JS scripts, icons | Responsive styles, client-side budget charts, and image upload handlers. |

