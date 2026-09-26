# Phase 7: User & Operations Manual
## PocketSmart AI — Installation, User Guide & Troubleshooting

---

### 1. System Requirements
* **Operating System**: Windows 10/11, macOS Monterey+, or Ubuntu Linux 22.04+.
* **Python Runtime**: Python 3.10, 3.11, or 3.12 (Python 3.11 recommended).
* **Network**: Standard internet access for Google Gemini API calls (or local execution in offline heuristic mode).

---

### 2. Quick Setup & Execution

#### Option A: 1-Click Launchers (Windows)
* Double-click `run.bat` (Batch launcher) or right-click `run.ps1` -> **Run with PowerShell**.
* The launcher automatically verifies the virtual environment, installs missing dependencies, and boots the FastAPI server on `http://127.0.0.1:8000`.

#### Option B: Manual Terminal Execution
```bash
# 1. Navigate to Phase 5 development directory
cd 05_Project_Development

# 2. Activate the virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows Command Prompt:
.\venv\Scripts\activate.bat
# Linux / macOS:
source venv/bin/activate

# 3. Launch server
python run_server.py
```
Visit `http://127.0.0.1:8000` in your web browser.

---

### 3. API Key Setup Guide

#### How & Where to Obtain your Google Gemini API Key:
1. Navigate to **Google AI Studio** in your browser: [https://aistudio.google.com/](https://aistudio.google.com/)
2. Sign in with your Google Account.
3. Click on the blue **"Get API key"** button in the left navigation sidebar.
4. Click **"Create API key"** and choose or create a Google Cloud Project.
5. Copy the generated API key (it starts with `AIzaSy...`).

#### Where to Paste It:
1. Open the file `05_Project_Development/.env` in VS Code or any text editor.
2. Locate the line:
   ```env
   GEMINI_API_KEY=
   ```
3. Paste your key directly after the `=` sign:
   ```env
   GEMINI_API_KEY=AIzaSyYourGeneratedSecretKeyHere
   ```
4. Save the file.
5. Restart the server. PocketSmart AI will automatically detect your key and switch to live Gemini AI inference!

> **Note**: Even without an API key, PocketSmart AI will run gracefully in **Deterministic Sample Mode**, ensuring you can test and demonstrate all features immediately.

---

### 4. End-User Workflow Guide

#### 4.1 Creating an Account
1. Click **Sign Up** on the top-right navigation bar.
2. Enter your chosen username, email, and password.
3. Upon registration, log in to establish your authenticated session.

#### 4.2 Using the Home Interior Planner
1. Navigate to **Home Interior** in the menu.
2. Set your maximum budget (e.g., `$2,000.00`).
3. Select your room type and design aesthetic.
4. Check your required items (sofa, coffee table, lighting, area rug).
5. Click **Generate Smart Interior Plan**.
6. Review the itemized cards, estimated prices, and sample vendor links.

#### 4.3 Using the Party & Event Planner
1. Navigate to **Party Planner**.
2. Enter the occasion, budget, guest count, and venue setting.
3. Click **Compute Smart Event Plan**.
4. View the 4-pillar budget allocation chart, per-guest metric, and preparation checklist.

#### 4.4 Using the Jewelry & Vision Planner
1. Navigate to **Jewelry & Vision**.
2. Enter the occasion, budget, and style preference.
3. *(Optional)* Drag & drop a photo of your outfit into the upload box.
4. Click **Analyze Outfit & Curate Jewelry**.
5. Observe the vision analysis (color palette and neckline geometry) and matching jewelry collection.

#### 4.5 Inspecting and Managing History
1. Click **My History** in the navigation bar.
2. View all previously generated plans.
3. Click **Inspect Details** to view full breakdown, export to JSON, or print to PDF.
4. Click **Delete** to remove a record from your history.

