# Phase 3: UI/UX Wireframes & Component Design
## PocketSmart AI — User Interface Specifications & Layouts

---

### 1. Design System & Theme
* **Typography**: Modern system sans-serif stack (`Inter`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`).
* **Color Palette**:
  * Primary Accent: Deep Indigo / Violet (`#4F46E5` / `#6366F1`)
  * Secondary Accent: Vibrant Emerald (`#10B981`)
  * Backgrounds: Warm Off-White (`#F9FAFB`) & Slate (`#0F172A`)
  * Cards / Surfaces: Pure White (`#FFFFFF`) with subtle border (`#E2E8F0`) and soft shadows (`box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1)`)
  * Warning / Alert: Amber (`#F59E0B`) & Crimson (`#EF4444`)
* **Responsive Breakpoints**:
  * Mobile: < 640px (single column stack, compact headers)
  * Tablet: 640px – 1024px (2-column layout)
  * Desktop: > 1024px (multi-column grid, sidebar analytics)

---

### 2. Layout Wireframes (ASCII)

#### 2.1 Navigation & Global Header
```
+-----------------------------------------------------------------------------------------+
| [PocketSmart AI Logo]   [Home Planner] [Party Planner] [Jewelry Planner] [History]      |
|                                                     [Session: Alex (User)] [Log Out]     |
+-----------------------------------------------------------------------------------------+
```

#### 2.2 Home Interior Planner Interface
```
+-----------------------------------------------------------------------------------------+
|  HOME INTERIOR BUDGET PLANNER                                                           |
|  Curate aesthetic living spaces within your exact financial ceiling.                    |
+--------------------------------------------+--------------------------------------------+
|  INPUT SPECIFICATIONS                      |  AI BUDGET ROADMAP & RECOMMENDATIONS       |
|                                            |                                            |
|  Total Budget ($): [ 2000.00             ] |  +---------------------------------------+ |
|                                            |  | SUMMARY: Scandinavian Living Room     | |
|  Room Type:        [ Living Room       v ] |  | Total Budget: $2,000 | Spent: $1,890   | |
|                                            |  | Remaining / Savings: $110.00           | |
|  Design Style:     [ Scandinavian Mini v ] |  +---------------------------------------+ |
|                                            |                                            |
|  Priority Items:                           |  ITEMIZED CURATION:                        |
|  [X] Sofa   [X] Coffee Table  [X] Floor Lamp|  [Card 1] Nordic 3-Seater Sofa - $950     |
|  [X] Area Rug  [ ] Bookshelf               |           Clean lines, oak legs. [Link]    |
|                                            |  [Card 2] Round Oak Coffee Table - $280    |
|  [  Generate Smart Interior Plan  ]        |           Matte finish oak.      [Link]    |
|                                            |  [Card 3] Arc Brass Floor Lamp - $160      |
+--------------------------------------------+--------------------------------------------+
```

#### 2.3 Party Planner Interface
```
+--------------------------------------------+--------------------------------------------+
|  PARTY & EVENT BUDGET PLANNER              |  BUDGET SPLIT & CHECKLIST                  |
|  Occasion:         [ Birthday Bash     v ] |                                            |
|  Total Budget ($): [ 1500.00             ] |  [ Catering & Bar:  $675.00 (45%)        ] |
|  Guest Headcount:  [ 25                  ] |  [ Venue & Rentals: $300.00 (20%)        ] |
|  Venue Setting:    [ Backyard Patio    v ] |  [ Decor & Lights:  $250.00 (16.7%)      ] |
|                                            |  [ Entertainment:   $195.00 (13.3%)      ] |
|  [  Compute Smart Event Plan  ]            |  Per-Guest Allocation: $56.80 / person     |
+--------------------------------------------+--------------------------------------------+
```

#### 2.4 Jewelry Planner (Multimodal Vision) Interface
```
+--------------------------------------------+--------------------------------------------+
|  JEWELRY & WARDROBE PLANNER                |  MATCHING JEWELRY ENSEMBLE                 |
|  Occasion:         [ Evening Gala        ] |                                            |
|  Budget ($):       [ 450.00              ] |  VISION INSIGHTS:                          |
|  Style Preference: [ Emerald & Gold Eleg ] |  - Dominant Tone: Deep Forest Emerald      |
|                                            |  - Neckline: Asymmetrical Off-Shoulder     |
|  OUTFIT IMAGE UPLOAD:                      |                                            |
|  +---------------------------------------+ |  RECOMMENDED METAL: 18K Yellow Gold        |
|  | [ Drag & Drop Outfit Photo Here ]     | |                                            |
|  | [ Browse File ] (gown_preview.jpg)    | |  [Card 1] Emerald Drop Earrings - $210   |
|  +---------------------------------------+ |  [Card 2] Gold Minimalist Cuff - $140      |
|  [  Analyze Outfit & Curate Jewelry  ]     |  [Card 3] Stackable Gold Rings - $85       |
+--------------------------------------------+--------------------------------------------+
```

