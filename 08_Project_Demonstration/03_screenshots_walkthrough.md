# Phase 8: Screenshots & Visual Showcase Guide
## PocketSmart AI — User Interface Walkthrough Catalog

This catalog outlines all primary user interface screens available in the PocketSmart AI web application.

---

### Screen 1: Master Landing Page (`/`)
* **Visual Components**:
  * Hero banner with gradient typography and quick-action buttons.
  * 3 Vertical Feature Cards for Home Interior, Party Planner, and Jewelry Vision.
  * System Architecture & Engine status card highlighting Python FastAPI, Gemini 1.5, SQLite, and JWT Security.
  * Responsive navigation header with live session detection.

---

### Screen 2: Home Interior Planner (`/home-planner`)
* **Input Specifications**:
  * Numeric budget ceiling input with step controls.
  * Target room type dropdown (Living Room, Primary Bedroom, Office, Dining, Patio).
  * Design style dropdown (Scandinavian Minimalist, Mid-Century Modern, Industrial Loft, Bohemian Chic, Modern Japandi, Contemporary Luxe).
  * Multi-select priority items checkboxes.
* **Results Showcase**:
  * Dual-tone dark banner with Total Budget, Estimated Cost, and Surplus / Savings.
  * Itemized product cards with name, description, quantity, price tag, and sample vendor links (`https://www.ikea.com/sample/...`, `https://www.target.com/sample/...`).
  * Professional styling and layout advice box.

---

### Screen 3: Party & Event Planner (`/party-planner`)
* **Input Specifications**:
  * Occasion text input.
  * Budget input.
  * Guest headcount numeric input.
  * Venue setting dropdown (At Home / Backyard, Rented Hall, Park Pavilion, Rooftop).
* **Results Showcase**:
  * High-level summary displaying Per-Guest allocation (`$XX.XX / person`).
  * Visual progress bars detailing budget distribution across Catering (45%), Venue (20%), Decor (20%), and Entertainment (15%).
  * Categorized rental and purchase cards.
  * Chronological 5-step preparation checklist.

---

### Screen 4: Jewelry & Multimodal Vision Planner (`/jewelry-planner`)
* **Input Specifications**:
  * Occasion, budget ceiling, and style preference inputs.
  * Drag-and-drop file upload zone for outfit photos (JPEG, PNG, WEBP).
  * Instant client-side thumbnail image preview.
* **Results Showcase**:
  * Multimodal Vision Insights card detailing detected fabric palette, neckline geometry, and formality profile.
  * Recommended Metal Tone banner (e.g. 18K Yellow Gold Vermeil vs. Rhodium Silver).
  * Coordinated jewelry collection (Earrings, Necklace, Cuff Bangle, Rings).
  * Certified gemologist styling commentary.

---

### Screen 5: User History & Personal Archives (`/history-page`)
* **Features**:
  * Chronological cards of all past recommendations saved under the authenticated account.
  * Vertical category tags (`HOME`, `PARTY`, `JEWELRY`).
  * Live AI vs. Heuristic Sample data badges.
  * Action buttons: "Inspect Details" and "Delete".

---

### Screen 6: Detailed Recommendation Inspector (`/details-page?id=...`)
* **Features**:
  * Direct invocation of the `/recommendations-details` API route.
  * Full breakdown of item quantities, price points, and links.
  * "Print / Save PDF" one-click browser print integration.
  * "Download JSON" raw payload export.

---

### Screen 7: Authentication Views (`/login` & `/register`)
* **Features**:
  * Clean, focused card layouts with input validation and feedback toast notifications.
  * Immediate session token synchronization with localStorage and cookies.

