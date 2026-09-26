# Phase 2: Software Requirements Specification (SRS)
## PocketSmart AI — Document Reference: IEEE-830-2026-PSA

---

### 1. Introduction

#### 1.1 Purpose
This document specifies the software requirements for the **PocketSmart AI** web application in accordance with the IEEE Std 830-1998 standard. It provides an exhaustive description of functional, non-functional, interface, and behavioral constraints for developers, evaluators, and stakeholders.

#### 1.2 Scope of the System
**PocketSmart AI** is an intelligent, context-aware budget planning platform powered by Google Gemini generative models. The system optimizes discretionary consumer spending across three specialized verticals:
1. **Home Interior Planner**: Room-type and style-based furniture, lighting, and decor curation within an exact budget ceiling.
2. **Party Planner**: Algorithmic financial distribution across catering, venue, decor, and entertainment based on headcount and celebration type.
3. **Jewelry Planner**: Wardrobe-matching accessories curated using multimodal vision input (outfit photograph) and textual occasion constraints.
4. **Accounts & History Subsystem**: User authentication, session management, and persistent storage of past curated plans.

#### 1.3 Definitions, Acronyms, and Abbreviations
* **SRS**: Software Requirements Specification
* **LLM**: Large Language Model
* **JWT**: JSON Web Token
* **REST**: Representational State Transfer
* **CORS**: Cross-Origin Resource Sharing
* **ORM**: Object Relational Mapping (SQLAlchemy)
* **ACID**: Atomicity, Consistency, Isolation, Durability

#### 1.4 References
* IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications.
* Google Gemini API Documentation (Multimodal Structured Output Specs).
* FastAPI Framework Reference Documentation (v0.110+).

---

### 2. Overall Description

#### 2.1 Product Perspective
PocketSmart AI operates as a self-contained, modular web service. It interfaces with client web browsers via HTTPS/HTTP, manages a local SQLite datastore for persistence, and issues secure REST calls to Google Gemini AI endpoints.

```
+-------------------------------------------------------------+
|                     Client Web Browser                      |
|       (HTML5 / Modern CSS / Vanilla JS / Jinja2 Views)      |
+------------------------------+------------------------------+
                               | REST API (JSON / FormData)
+------------------------------v------------------------------+
|                     FastAPI Backend                         |
|  - Routers: Auth, Planners, History, Pages                  |
|  - Validation: Pydantic v2 Models                           |
|  - Services: Gemini AI Integration & Fallback Engine        |
+---------------+-----------------------------+---------------+
                |                             |
+---------------v---------------+ +-----------v---------------+
|        SQLite Database        | |      Google Gemini API    |
| (Users, Sessions, History)    | |  (Multimodal Flash Vision)|
+-------------------------------+ +---------------------------+
```

#### 2.2 User Characteristics
* General consumers with varying degrees of technical literacy.
* Event organizers, first-time homeowners, college students, and wedding guests seeking rapid budgeting decisions.

#### 2.3 Operating Environment
* Server: Windows 10/11, macOS, or Linux running Python 3.10+.
* Client: Any standard evergreen web browser (Google Chrome 110+, Mozilla Firefox 110+, Apple Safari 16+, Microsoft Edge 110+).

#### 2.4 Constraints
* API keys must remain strictly confidential and never be checked into git or sent to the browser.
* Total costs of generated recommendations must not exceed the user-specified budget ceiling.
* The system must operate reliably with mock data when external APIs or keys are unavailable.

---

### 3. Specific Functional Requirements

#### 3.1 Module 1: Home Interior Planner
* **FR-HOME-01**: The system shall accept `budget` (numeric positive float), `room_type` (e.g., Living Room, Bedroom, Home Office), `style` (e.g., Scandinavian, Industrial, Modern Minimalist, Bohemian), and `required_items` (array of strings or comma-separated items with desired quantities).
* **FR-HOME-02**: The system shall generate itemized selections categorized into:
  * Key Furniture
  * Ambient & Accent Lighting
  * Decorative Accents & Rugs
* **FR-HOME-03**: Each suggested item shall include `name`, `category`, `estimated_price`, `quantity`, `description`, and `vendor_link` (labeled as mock/sample or live).
* **FR-HOME-04**: The system shall compute `total_estimated_cost` and verify `total_estimated_cost <= budget`.

#### 3.2 Module 2: Party Planner
* **FR-PARTY-01**: The system shall accept `occasion` (e.g., Birthday, Anniversary, Game Night), `budget` (numeric positive float), `guest_count` (integer >= 1), and `venue_type` (e.g., At Home / Backyard / Rented Hall / Park).
* **FR-PARTY-02**: The system shall subdivide the budget into distinct spending allocations:
  * Catering & Refreshments (~40–50%)
  * Venue & Rentals (~15–25%)
  * Decorations & Ambience (~15–20%)
  * Entertainment, Music & Favors (~10–15%)
* **FR-PARTY-03**: The system shall calculate `per_guest_cost = budget / guest_count` and present per-person catering guidelines.
* **FR-PARTY-04**: The system shall generate specific actionable purchase/rental checklists with individual line item costs.

#### 3.3 Module 3: Jewelry & Wardrobe Planner
* **FR-JEWEL-01**: The system shall accept `budget` (positive float), `occasion` (e.g., Wedding, Gala, Daily Casual, Formal Interview), and `style_preference` (e.g., Minimalist Silver, Royal Antique Gold, Contemporary Gemstone).
* **FR-JEWEL-02**: The system shall support an optional multipart image file upload (`image/png`, `image/jpeg`, `image/webp` up to 10MB) representing the user's intended outfit.
* **FR-JEWEL-03**: When an outfit image is provided, the multimodal vision engine shall analyze primary fabric colors, neckline geometry, and formality level, matching suitable metals and gem accents.
* **FR-JEWEL-04**: The system shall return categorized items: Earrings, Necklace, Bracelets/Bangles, and Rings, alongside styling justification notes.

#### 3.4 Module 4: Authentication & User Accounts
* **FR-AUTH-01**: The system shall provide endpoints for user registration (`POST /register`), login (`POST /login`), logout (`POST /logout`), and token issuance (`POST /token`).
* **FR-AUTH-02**: Passwords shall be cryptographically hashed using salt-hashed bcrypt prior to storage in the database.
* **FR-AUTH-03**: The system shall verify authentication credentials and issue a signed JWT access token.
* **FR-AUTH-04**: The endpoints `/session-info` and `/session-data` shall return the currently authenticated user identity and session validity.

#### 3.5 Module 5: Recommendation History
* **FR-HIST-01**: The system shall persist every successfully generated recommendation linked to the authenticated user's ID.
* **FR-HIST-02**: The endpoint `GET /history` shall return a list of past recommendations with creation timestamps, planner category, budget, and summary tags.
* **FR-HIST-03**: The endpoint `GET /recommendations-details` (and `GET /recommendations-details/{id}`) shall retrieve the complete JSON payload of a previously saved recommendation.
* **FR-HIST-04**: Authenticated users shall have the ability to delete entries from their history.

---

### 4. Non-Functional Requirements

#### 4.1 Performance & Latency
* Local endpoints (authentication, history queries) shall respond in < 100 milliseconds.
* AI recommendation generation shall complete within 3.5 to 8.0 seconds depending on upstream LLM latency.
* Fallback heuristic generation shall execute in < 200 milliseconds.

#### 4.2 Security & Protection
* Passwords must meet minimum entropy requirements (minimum 6 characters).
* API keys must be loaded exclusively via server-side environment variables (`.env`).
* Cross-Site Scripting (XSS) protections enforced through Jinja2 template auto-escaping and sanitized DOM rendering.
* CORS headers configured to prevent unauthorized cross-origin tampering.

#### 4.3 Reliability & Availability
* The system shall exhibit 100% uptime resilience: In the event of an upstream Gemini API outage, rate limit HTTP 429, or invalid API key, the system shall seamlessly degrade to high-quality deterministic sample data without crashing.

#### 4.4 Usability & Accessibility
* Responsive design catering to viewports from 360px (mobile) to 3840px (4K ultra-wide).
* Color contrast ratio meeting WCAG 2.1 AA standards (minimum 4.5:1 for normal text).

