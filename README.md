# ✨ PocketSmart AI — Intelligent Context-Aware Budget & Purchase Planning System

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Google Gemini 1.5](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-4285F4.svg)](https://aistudio.google.com/)
[![Tests](https://img.shields.io/badge/Pytest-20%2F20%20Passed%20(100%25)-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-purple.svg)]()

> **PocketSmart AI** is a full-stack, multimodal generative AI web application that optimizes consumer discretionary expenditures across three complex verticals: **Home Interiors**, **Events & Parties**, and **Wardrobe-Matched Jewelry**. Powered by **Google Gemini 1.5 Flash**, it combines semantic AI reasoning with deterministic mathematical guardrails to guarantee zero budget overruns ($Total \le Budget$).

---

## 🗂️ Master Repository Structure

```
PocketSmartAI/
├── 01_Brainstorming_and_Ideation/       # Phase 1: Problem statement, feasibility, mind map, competitive analysis
│   ├── 01_problem_statement.md
│   ├── 02_feasibility_study.md
│   ├── 03_mind_map_and_ideation.md
│   └── 04_competitive_analysis.md
│
├── 02_Requirement_Analysis/             # Phase 2: IEEE 830 SRS, use cases, Agile user stories
│   ├── 01_ieee_830_srs.md
│   ├── 02_use_case_specifications.md
│   └── 03_agile_user_stories.md
│
├── 03_Project_Design/                    # Phase 3: System architecture, DFDs, data contracts, UI/UX
│   ├── 01_system_architecture.md
│   ├── 02_data_flow_diagrams.md
│   ├── 03_data_contracts_and_schemas.md
│   ├── 04_ui_ux_wireframes.md
│   └── 05_database_schema.md
│
├── 04_Project_Planning/                  # Phase 4: WBS, 12-week Gantt schedule, risk mitigation
│   ├── 01_work_breakdown_structure.md
│   ├── 02_12_week_gantt_schedule.md
│   └── 03_risk_mitigation_matrix.md
│
├── 05_Project_Development/               # Phase 5: Complete runnable source code, templates & assets
│   ├── backend/
│   │   └── app/
│   │       ├── main.py                   # FastAPI initialization & middleware
│   │       ├── config.py                 # Pydantic v2 settings (.env loader)
│   │       ├── database.py               # SQLite connection & session maker
│   │       ├── models.py                 # SQLAlchemy ORM models (User, Recommendation)
│   │       ├── schemas.py                # Pydantic request/response contracts
│   │       ├── auth.py                   # BCrypt password hashing & JWT handling
│   │       ├── routers/                  # API and page routers
│   │       │   ├── auth_routes.py        # /register, /login, /logout, /session-info
│   │       │   ├── planner_routes.py     # /generate-home, /generate-party, /generate-jewelry
│   │       │   ├── history_routes.py     # /history, /recommendations-details
│   │       │   └── page_routes.py        # Jinja2 HTML page views
│   │       ├── services/                 # Business logic & AI clients
│   │       │   ├── gemini_service.py     # Google Gemini 1.5 Flash text & vision client
│   │       │   ├── mock_service.py       # Deterministic heuristic fallback engine
│   │       │   ├── home_planner.py       # Home interior curation logic
│   │       │   ├── party_planner.py      # Event headcount allocation logic
│   │       │   └── jewelry_planner.py    # Multimodal jewelry & vision curation
│   │       └── utils/                    # Budget capping & image processors
│   ├── frontend/
│   │   ├── static/                       # CSS, JavaScript & uploaded media
│   │   │   ├── css/main.css
│   │   │   └── js/                       # Modular ES6 controllers
│   │   └── templates/                    # Modular Jinja2 web views
│   ├── tests/                            # Automated 20-case test suite
│   ├── venv/                             # Configured Python virtual environment
│   ├── .env                              # Active local environment variables
│   ├── .env.example                      # Template with variable names only
│   ├── requirements.txt                  # Python dependencies
│   └── run_server.py                     # Direct application server entrypoint
│
├── 06_Project_Testing/                   # Phase 6: Test plan, 20-case matrix, automated test suite
│   ├── 01_test_plan.md
│   └── 02_test_case_matrix.md
│
├── 07_Project_Documentation/             # Phase 7: Final academic report/thesis, API specs, user manual
│   ├── 01_academic_thesis_report.md
│   ├── 02_api_specifications.md
│   └── 03_user_and_operations_manual.md
│
├── 08_Project_Demonstration/             # Phase 8: Viva presentation outline, live demo scripts, screenshots
│   ├── 01_viva_presentation_outline.md
│   ├── 02_live_demo_scripts.md
│   └── 03_screenshots_walkthrough.md
│
├── .gitignore                            # Excludes .env, API keys, venvs, and build artifacts
├── run.bat                               # 1-Click Windows Batch launcher (delegates to Phase 5)
├── run.ps1                               # 1-Click Windows PowerShell launcher (delegates to Phase 5)
└── README.md                             # Master repository evaluation guide & documentation index
```

---

## 🔑 How & Where to Get Your Gemini API Key

### 1. Obtain Your Free API Key
1. Visit **Google AI Studio**: [https://aistudio.google.com/](https://aistudio.google.com/)
2. Sign in with your standard Google Account.
3. In the left navigation sidebar, click on **"Get API key"**.
4. Click **"Create API key"** (select an existing Google Cloud project or click "Create API key in new project").
5. Copy the generated key string (format: `AIzaSy...`).

### 2. Where to Paste It
Open the `.env` file located in `05_Project_Development/.env`:

```env
# Open 05_Project_Development/.env in VS Code or Notepad:
GEMINI_API_KEY=AIzaSyYourGeneratedSecretKeyHere
```

Save the file. When you launch PocketSmart AI, the server will detect the key and connect to Google Gemini 1.5 Flash.

> **Zero Downtime Guarantee**: If you run without an API key, PocketSmart AI automatically switches to its built-in **Deterministic Mock Service**. All recommendations will be generated using realistic market samples labeled `[Algorithmic Market Estimate]`.

---

## 🚀 How to Run the Project

### Method 1: 1-Click Windows Launchers (Recommended)
From the repository root folder, simply run either:
* **Double-click `run.bat`** (Windows Command Prompt Batch Launcher)
* **Right-click `run.ps1` -> Run with PowerShell** (PowerShell Launcher)

The launcher automatically detects the virtual environment, verifies dependencies, and starts the server.

### Method 2: Manual Terminal Execution
```bash
# 1. Open terminal and navigate to 05_Project_Development
cd 05_Project_Development

# 2. Activate the virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows Command Prompt:
.\venv\Scripts\activate.bat
# Linux / macOS:
source venv/bin/activate

# 3. Start the application
python run_server.py
```

### Accessing the Web Application
* 🌐 **Web Interface:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
* 📖 **Interactive Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* 📚 **Interactive ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running the Automated Test Suite

The project includes an automated 20-case test suite validating all planners, authentication endpoints, budget ceiling constraints, image uploads, and history CRUD operations:

```bash
cd 05_Project_Development
.\venv\Scripts\pytest -v
```

### Test Suite Summary:
```
tests/test_auth.py::test_register_user_success PASSED
tests/test_auth.py::test_register_duplicate_username PASSED
tests/test_auth.py::test_register_duplicate_email PASSED
tests/test_auth.py::test_login_success PASSED
tests/test_auth.py::test_login_invalid_password PASSED
tests/test_auth.py::test_session_info_unauthenticated PASSED
tests/test_auth.py::test_session_info_authenticated PASSED
tests/test_auth.py::test_session_data_endpoint PASSED
tests/test_history.py::test_history_unauthenticated_fails PASSED
tests/test_history.py::test_history_authenticated_lifecycle PASSED
tests/test_home_planner.py::test_generate_home_plan_valid PASSED
tests/test_home_planner.py::test_home_planner_budget_ceiling PASSED
tests/test_home_planner.py::test_home_planner_negative_budget PASSED
tests/test_home_planner.py::test_home_planner_authenticated_persistence PASSED
tests/test_jewelry_planner.py::test_generate_jewelry_text_only PASSED
tests/test_jewelry_planner.py::test_generate_jewelry_with_image PASSED
tests/test_jewelry_planner.py::test_generate_jewelry_invalid_image_type PASSED
tests/test_party_planner.py::test_generate_party_plan_valid PASSED
tests/test_party_planner.py::test_party_planner_per_guest_calc PASSED
tests/test_party_planner.py::test_party_planner_zero_guests PASSED
======================= 20 passed in 7.40s (100% Success) =======================
```

---

## 📡 API Routes Specification

| HTTP Method | Route | Description | Access |
| :--- | :--- | :--- | :--- |
| `POST` | `/register` | Register new user account | Public |
| `POST` | `/login` | Authenticate user & issue JWT cookie | Public |
| `POST` | `/token` | Standard OAuth2 token endpoint | Public |
| `POST` | `/logout` | Invalidate cookie session | Public |
| `GET` | `/session-info` | Inspect visitor session state | Public |
| `GET` | `/session-data` | Alias for session data payload | Public |
| `POST` | `/generate-home` | Generate interior furnishing plan | Public / Authenticated |
| `POST` | `/generate-party` | Generate event budget split & checklist | Public / Authenticated |
| `POST` | `/generate-jewelry` | Curate jewelry with optional outfit image | Public / Authenticated |
| `GET` | `/history` | List user's saved recommendations | Authenticated |
| `GET` | `/recommendations-details` | Inspect full recommendation details (`?id=...`) | Authenticated |
| `DELETE`| `/history/{id}` | Delete recommendation from database | Authenticated |

---

## 🛡️ Security & Disclaimers

1. **API Keys Protection**: `GEMINI_API_KEY` and `SECRET_KEY` are stored strictly in `05_Project_Development/.env` and excluded from git via `.gitignore`.
2. **Password Security**: Passwords are salt-hashed using bcrypt (12 rounds) prior to database insertion.
3. **Data Transparency**: In compliance with requirements, all estimated prices are modeled market averages, and third-party product links are explicitly tagged as `mock_sample`.

