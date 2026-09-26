# Phase 1: Problem Statement & Vision Document
## PocketSmart AI — Intelligent Context-Aware Budget & Purchase Planning System

---

### 1. Executive Summary
In the modern consumer landscape, individuals frequently face choice overload when attempting to plan budget-constrained purchases for complex, multi-item undertakings. Specifically, domains such as **Home Interior Rejuvenation**, **Event and Party Hosting**, and **Curated Jewelry & Fashion Styling** present steep cognitive hurdles:
1. **Budget Fragmentation**: Users struggle to distribute a finite budget across disparate categories (e.g., in a \$1,500 party budget, how much belongs to catering vs. decor vs. entertainment?).
2. **Catalog Exhaustion**: E-commerce platforms display millions of uncurated items without holistic stylistic cohesion.
3. **Lack of Personalization**: Generic search engines provide isolated links rather than synthesized, balanced, and ready-to-execute itemized bundles.
4. **Visual Disconnect**: In styling and jewelry coordination, consumers cannot readily evaluate whether an accessory will match an existing outfit without professional consultation.

**PocketSmart AI** resolves these friction points by uniting Google Gemini’s multimodal generative intelligence with a deterministic budget allocation engine and a responsive web application. The platform converts freeform user preferences, budget caps, guest counts, room parameters, and uploaded outfit imagery into structured, itemized, and stylistically harmonious purchasing roadmaps.

---

### 2. Core Problem Statements

#### 2.1 Domain 1: Home Interior Planning
* **Current Pain Point**: Users seeking to furnish or revamp a bedroom, living room, home office, or balcony with a strict budget (e.g., \$2,000) spend tens of hours browsing various online stores. They frequently overspend on aesthetic centerpiece items (e.g., sofas) and run out of funds for vital functional elements (e.g., task lighting, storage, window treatments).
* **The PocketSmart AI Solution**: Users input their total budget, target room type, stylistic preference (e.g., Scandinavian Minimalist, Mid-Century Modern, Industrial, Bohemian, Neo-Classical), and required items/quantities. The system applies domain-weighted budget distribution algorithms and queries Google Gemini to curate an itemized package featuring furniture, ambient/task lighting, and accents—complete with transparent estimated pricing, dimensional harmony, and sample vendor links.

#### 2.2 Domain 2: Event & Party Planning
* **Current Pain Point**: Event planning involves multi-variable optimization. A host with \$1,200 hosting a 20-guest birthday party must calculate per-head catering allocations, venue or setup costs, aesthetic thematic decor, and entertainment. Inexperienced hosts consistently suffer from cost overruns or experience deficits (e.g., abundant food but zero ambiance or entertainment).
* **The PocketSmart AI Solution**: Users specify the occasion (e.g., Birthday, Anniversary, Cocktail Reception, Game Night, Graduation), budget, guest headcount, and venue context (indoor home, backyard, rented hall). PocketSmart AI automatically computes a proportional category breakdown (Venue 20%, Catering 45%, Decor 20%, Entertainment/Favors 15%), validates per-guest viability, and generates a concrete action list with itemized cost targets.

#### 2.3 Domain 3: Jewelry & Wardrobe Matching
* **Current Pain Point**: Selecting jewelry for special occasions (weddings, galas, formal interviews, cultural festivities) requires nuanced understanding of color palettes, neckline cuts, fabric textures, metal compatibility (e.g., warm gold vs. cool silver vs. rose gold), and gem accents. Users frequently buy pieces that clash with their attire or breach their discretionary budget.
* **The PocketSmart AI Solution**: Users input their budget, occasion, and style preferences, with the option to upload a photo of their outfit. Leveraging Gemini's Multimodal Vision capabilities, the engine analyzes fabric tones, patterns, and neckline geometry to curate metal, gemstone, earring, necklace, bracelet, and ring suggestions that harmonize seamlessly while remaining strictly within budget.

---

### 3. Target Audience & Personas

| Persona | Demographics / Profile | Primary Goal | Pain Points | Value Proposition |
| :--- | :--- | :--- | :--- | :--- |
| **Priya S. (First-time Homeowner)** | Age 29, Urban Professional, Budget: \$3,500 | Furnish a living/dining room efficiently | Overwhelmed by furniture catalogs; fear of budget blowouts | Instant balanced package with prioritized items and aesthetic cohesion |
| **Marcus T. (Social Host)** | Age 24, University Club Lead, Budget: \$600 | Host a 25-person themed game night party | Unsure how to divide funds between food, drinks, and lighting | Automated per-guest cost breakdown and themed checklist |
| **Elena R. (Wedding Guest)** | Age 33, Corporate Consultant, Budget: \$400 | Find jewelry matching an emerald green evening gown | Uncertainty about matching necklace styles with asymmetric necklines | Multimodal vision upload matches metals and stones directly to gown photo |

---

### 4. Vision & Project Objectives
1. **Zero-Overrun Guarantee**: Every generated plan enforces mathematical budget compliance, providing clear warnings if requirements are economically unfeasible.
2. **Multimodal Accessibility**: Enable frictionless interaction via structured forms and direct image uploads for aesthetic appraisal.
3. **Transparency & Trust**: Clearly distinguish between live supplier listings and AI-curated estimated/sample listings.
4. **Persistent History**: Enable authenticated users to store, revisit, compare, and export their past curated plans.
5. **Resilient Architecture**: Provide graceful degradation with rule-based heuristics and local fallback models whenever external AI services experience latency or quota limits.

