# Phase 4: 12-Week Agile Project Schedule & Gantt Chart
## PocketSmart AI — Sprint Roadmap & Delivery Timeline

---

### 1. Gantt Timeline Diagram (Mermaid)

```mermaid
gantt
    title PocketSmart AI — 12-Week Sprint Schedule
    dateFormat  YYYY-MM-DD
    section Phase 1: Ideation
    Problem Statement & Scope        :done, des1, 2026-06-01, 7d
    Feasibility & Benchmarking       :done, des2, after des1, 7d
    section Phase 2: Requirements
    IEEE 830 SRS Specification       :done, req1, after des2, 7d
    Use Cases & Agile User Stories   :done, req2, after req1, 7d
    section Phase 3: Design
    System & DFD Architecture       :done, arch1, after req2, 7d
    Database ERD & UI/UX Wireframes  :done, arch2, after arch1, 7d
    section Phase 4: Planning
    WBS & Risk Mitigation Planning   :done, plan1, after arch2, 7d
    section Phase 5: Implementation
    Backend Core, Auth & Database    :active, dev1, after plan1, 7d
    Gemini AI & Multimodal Vision    :active, dev2, after dev1, 7d
    Planners (Home, Party, Jewelry)  :active, dev3, after dev2, 7d
    Frontend Templates & Dynamic UI  :active, dev4, after dev3, 7d
    section Phase 6: Testing
    20-Case Test Suite & Pytest Run  :test1, after dev4, 7d
    section Phase 7 & 8: Review
    Academic Thesis & User Manual    :doc1, after test1, 7d
    Viva Deck & Live Demonstration   :demo1, after doc1, 7d
```

---

### 2. Sprint-by-Sprint Milestone Table

| Sprint / Week | Phase Alignment | Major Deliverables & Milestones | Acceptance Milestone |
| :--- | :--- | :--- | :--- |
| **Week 1** | Phase 1: Ideation | Problem identification, user pain points, domain scope definition. | Milestone M1: Scope Approved |
| **Week 2** | Phase 1: Feasibility | Technical, economic, operational analysis; technology stack sign-off. | Milestone M2: Feasibility Confirmed |
| **Week 3** | Phase 2: Requirements | Draft IEEE Std 830 SRS, define functional/non-functional requirements. | Milestone M3: SRS Baseline Locked |
| **Week 4** | Phase 2: Modeling | Detailed use case specifications and Agile user story backlogs with Gherkin scenarios. | Milestone M4: Backlog Finalized |
| **Week 5** | Phase 3: Architecture | System architecture, DFD Levels 0, 1, 2, OpenAPI 3.1 contracts. | Milestone M5: Architecture Review |
| **Week 6** | Phase 3: DB & UX | Relational SQLite ERD, component design system, wireframe prototypes. | Milestone M6: Design Freeze |
| **Week 7** | Phase 4: Planning | WBS level 4 dictionary, risk register, fallback strategy definition. | Milestone M7: Execution Plan Active |
| **Week 8** | Phase 5: Core Backend | FastAPI framework initialization, JWT auth, password hashing, database models. | Milestone M8: Auth & DB Operational |
| **Week 9** | Phase 5: AI Integration | Google Gemini API integration, prompt templates, vision processing, fallback mocks. | Milestone M9: AI Pipeline Verified |
| **Week 10**| Phase 5: Web Frontend | Responsive Jinja2 views, AJAX form submissions, Chart.js graphs, session modals. | Milestone M10: Full Application Runnable |
| **Week 11**| Phase 6: Testing | 20-case test matrix execution, boundary budget checks, Pytest automated suite. | Milestone M11: 100% Tests Passing |
| **Week 12**| Phase 7 & 8: Delivery | Final Capstone Thesis/Report, User Manual, Viva Presentation Deck & Demo Scripts. | Milestone M12: Project Sign-Off |

