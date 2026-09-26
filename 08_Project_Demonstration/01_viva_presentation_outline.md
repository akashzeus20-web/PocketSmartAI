# Phase 8: Viva Presentation Outline & Evaluation Defense Guide
## PocketSmart AI — Oral Defense & Demonstration Script

---

### 1. Slide-by-Slide Defense Script

| Slide # | Slide Title | Visual Assets | Speaking Script / Key Talking Points | Duration |
| :---: | :--- | :--- | :--- | :---: |
| **01** | Title & Research Context | Project Logo, Team Details, Tech Stack Badges | "Distinguished evaluators, welcome to the presentation of PocketSmart AI—an intelligent context-aware budget planning system that bridges the gap between generative AI creativity and deterministic fiscal constraints." | 1.0 min |
| **02** | Problem Statement | Choice overload chart & math error breakdown | "Modern consumers struggle with multi-item budget planning across home decor, events, and jewelry. LLMs typically fail here because they hallucinate prices and violate budget ceilings." | 1.5 min |
| **03** | Proposed Architecture | High-level system architecture & DFD | "Our solution couples Google Gemini 1.5 Flash multimodal models with Python FastAPI and deterministic post-processors, ensuring total cost never exceeds user budget." | 2.0 min |
| **04** | Core Vertical 1: Home Interior | UI Screenshots & item cards with links | "The Home Interior Planner splits funds across furniture (60%), lighting (15%), and decor (25%), providing sample vendor links and practical styling advice." | 1.5 min |
| **05** | Core Vertical 2: Party Planner | Allocation bar graph & per-head cost | "For event organizers, our party engine calculates per-guest metrics and distributes funds across catering, venue rentals, decor, and entertainment with a 5-step prep checklist." | 1.5 min |
| **06** | Core Vertical 3: Jewelry Vision | Image input + palette extraction card | "In the Jewelry module, users upload an outfit photograph. Gemini Vision analyzes neckline geometry and fabric undertones to recommend coordinating metals and gems." | 2.0 min |
| **07** | Security & Session Management | JWT flow & SQLite schema | "We adhere to industry security standards: bcrypt password hashing, signed JWT tokens, session endpoints (`/session-info`, `/session-data`), and full CRUD history." | 1.5 min |
| **08** | Testing & Validation | 20-Case Test Matrix (100% Pass) | "Our automated Pytest suite validates 20 rigorous test cases covering edge cases, negative budgets, image validation, and upstream failover in 7 seconds." | 1.5 min |
| **09** | Live Demonstration | Browser walkthrough on localhost:8000 | [Live Demonstration of all 3 planners and history inspection] | 3.5 min |
| **10** | Conclusion & Q&A | Summary table & Future Scope | "Thank you. We are now open for your questions and technical defense." | 1.0 min |

---

### 2. Anticipated Viva Examination Questions & Answers

#### Q1: "Why not just use ChatGPT or vanilla Gemini directly via a prompt?"
* **Answer**: "While standard chatbots can generate creative ideas, they lack arithmetic rigor and stateful persistence. They regularly produce shopping lists whose sums exceed the user's budget ceiling by 20% to 40%. PocketSmart AI embeds the LLM within deterministic mathematical guardrails that audit every line item, recalculate totals, scale prices if needed, and save structured records to a private relational database."

#### Q2: "What happens if the Gemini API is down, has network latency, or the API key runs out of quota?"
* **Answer**: "Our architecture implements the Circuit Breaker / Fallback pattern. If the Gemini API returns an error (HTTP 429, timeout, or missing key), the backend automatically and transparently engages `MockService`. This deterministic heuristic engine delivers realistic, fully compliant recommendations tagged as `[Algorithmic Market Estimate]`, guaranteeing 100% uptime."

#### Q3: "How does the system ensure privacy when users upload outfit images?"
* **Answer**: "Uploaded images are validated in-memory using Pillow, resized, and transmitted via encrypted HTTPS directly to the vision inference API. No user images are sold or permanently archived to unauthenticated public directories."

#### Q4: "How are passwords and session tokens safeguarded?"
* **Answer**: "We utilize one-way salt-hashed bcrypt with 12 rounds of computational work. Passwords are never stored or logged in plain text. Session tokens are signed HMAC-SHA256 JWTs transmitted via both Authorization headers and HTTP-only cookies to prevent cross-site scripting (XSS) extraction."

