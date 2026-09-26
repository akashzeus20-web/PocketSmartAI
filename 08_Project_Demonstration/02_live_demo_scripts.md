# Phase 8: Live Evaluation Demonstration Scripts
## PocketSmart AI — Step-by-Step Live Evaluator Narrative

---

### Step 1: Bootstrapping & Readiness Check (30 seconds)
1. Open PowerShell or Terminal in the repository root.
2. Launch the application:
   ```powershell
   .\run.ps1
   ```
   *(Or double-click `run.bat`)*
3. Point out terminal initialization message:
   ```
   ==================================================
    PocketSmart AI — Starting Application Server
    Host: http://127.0.0.1:8000
    Docs: http://127.0.0.1:8000/docs
   ==================================================
   ```
4. Open browser to `http://127.0.0.1:8000`. Show the clean modern UI landing page.

---

### Step 2: User Registration & Session Validation (1 minute)
1. Click **Sign Up** on the top navigation bar.
2. Register a new account:
   * **Username**: `evaluator_demo`
   * **Email**: `evaluator@university.edu`
   * **Password**: `TestPass123`
3. Click **Create Account**. Toast confirms creation; redirect to Login.
4. Log in. Point out that the navigation bar updates immediately to display: `Hi, evaluator_demo` and the **My History** and **Log Out** buttons.
5. In another tab, navigate to `http://127.0.0.1:8000/session-info`. Highlight the clean JSON returning `"authenticated": true`.

---

### Step 3: Vertical 1 — Home Interior Planning (1 minute)
1. Click **Home Interior** in navigation.
2. Fill in parameters:
   * **Total Budget**: `$2,000.00`
   * **Room Type**: `Living Room`
   * **Aesthetic Style**: `Scandinavian Minimalist`
   * **Check Priority Items**: Sofa, Coffee Table, Floor Lighting, Area Rug.
3. Click **Generate Smart Interior Plan**.
4. Observe the smooth loading animation followed by the results showcase:
   * Highlight **Total Budget** ($2,000.00) vs. **Estimated Total** ($1,890.00) vs. **Surplus** ($110.00).
   * Demonstrate that the total does NOT exceed the budget.
   * Highlight item cards with descriptions, quantity, price, and sample vendor links (`View Item &rarr;`).
   * Read out the generated layout and design tips.

---

### Step 4: Vertical 2 — Party & Event Planning (1 minute)
1. Click **Party Planner** in navigation.
2. Fill in parameters:
   * **Occasion**: `30th Birthday Bash`
   * **Budget**: `$1,500.00`
   * **Guest Count**: `25`
   * **Venue**: `At Home / Private Backyard`
3. Click **Compute Smart Event Plan**.
4. Review the results:
   * Point out the calculated **Per-Guest metric** (`$60.00 / person`).
   * Show the 4-pillar budget allocation breakdown with proportional progress bars (Catering, Venue, Decor, Entertainment).
   * Review the 5-step preparation checklist.

---

### Step 5: Vertical 3 — Jewelry & Multimodal Vision Planning (1.5 minutes)
1. Click **Jewelry & Vision** in navigation.
2. Set budget: `$450.00`, Occasion: `Evening Gala`, Style: `Warm 18k Gold & Emerald`.
3. Drag and drop any image into the outfit upload zone. Show the instant thumbnail preview.
4. Click **Analyze Outfit & Curate Jewelry**.
5. Examine output:
   * Multimodal Vision Insights (Detected Palette, Neckline, Formality).
   * Recommended Metal Tone (`18K Yellow Gold Vermeil`).
   * Itemized collection: Earrings, Necklace, Cuff Bangle, Ring.
   * Stylist commentary.

---

### Step 6: History Inspection & Details Export (1 minute)
1. Click **My History** in the navigation bar.
2. Observe all generated plans listed with category tags, timestamp, and budgets.
3. Click **Inspect Details** on one of the items.
4. Show the dedicated details view (`/details-page?id=...` calling `/recommendations-details`).
5. Click **Download JSON** to demonstrate raw data export.
6. Click **Print / Save PDF** to show formatted printable layout.
7. Return to history and delete one record to prove database CRUD consistency.

---

### Step 7: Automated Test Verification (30 seconds)
1. In terminal:
   ```powershell
   .\venv\Scripts\pytest -v
   ```
2. Demonstrate that all 20 test cases pass in under 8 seconds.

