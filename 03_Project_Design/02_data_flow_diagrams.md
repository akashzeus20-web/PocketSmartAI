# Phase 3: Data Flow Diagrams (DFD)
## PocketSmart AI — DFD Level 0, Level 1, and Level 2 Models

---

### 1. DFD Level 0: Context Diagram

```mermaid
flowchart TD
    User([End User / Client Browser])
    System[0.0 PocketSmart AI Platform]
    Gemini[Google Gemini 1.5 Flash Vision / Text API]
    DB[(SQLite Storage)]

    User -->|1. Credentials & Auth Requests| System
    User -->|2. Planning Parameters: Budget, Style, Room, Occasion, Outfit Image| System
    System -->|3. Auth Token, Session Info, HTML Pages, Curated Plans| User

    System -->|4. Prompt Payload & Multimodal Image Pixels| Gemini
    Gemini -->|5. Structured JSON Recommendations| System

    System -->|6. User Profiles, Hashes, Session Records, Plan JSON| DB
    DB -->|7. Fetched User Data, Query History Records| System
```

---

### 2. DFD Level 1: System Operational Decomposition

```mermaid
flowchart TD
    User([User])
    subgraph PSA ["PocketSmart AI Backend Engine"]
        P1["1.0 Authentication & Session Management"]
        P2["2.0 Request Validation & Pre-Allocation"]
        P3["3.0 AI Inference & Prompt Engineering"]
        P4["4.0 Heuristic Fallback & Mock Synthesis"]
        P5["5.0 Post-Generation Budget Audit"]
        P6["6.0 History Persistence & Query Service"]
    end
    DB[(SQLite Database)]
    Gemini[Google Gemini API]

    User -->|Register / Login| P1
    P1 -->|Store Credentials / Fetch User| DB
    P1 -->|JWT Token / Auth Context| User

    User -->|Plan Request: Home/Party/Jewelry| P2
    P2 -->|Validated Params & Budget Limits| P3

    P3 -->|Structured Multimodal Prompt| Gemini
    Gemini -->|Structured JSON Output| P5

    P3 -.->|API Unavailable / No Key / Exception| P4
    P4 -->|Pre-Calculated Curated Plan| P5

    P5 -->|Audited & Balanced Plan| P6
    P6 -->|Save Recommendation Record| DB
    P6 -->|Deliver Itemized Plan to Client| User

    User -->|Query /history & /details| P6
    P6 -->|Read User History| DB
```

---

### 3. DFD Level 2: Jewelry Planner Multimodal Process

```mermaid
flowchart TD
    User([User])
    subgraph JewelryFlow ["Process 3.3: Multimodal Jewelry Planning"]
        P3_3_1["3.3.1 Parse Form Data & Image Bytes"]
        P3_3_2["3.3.2 Image Verification & Resizing (Pillow)"]
        P3_3_3["3.3.3 Assemble Vision Prompt with Style & Budget"]
        P3_3_4["3.3.4 Execute Multimodal Inference"]
        P3_3_5["3.3.5 Extract Matching Palette & Pieces"]
        P3_3_6["3.3.6 Enforce Strict Budget Sum Constraint"]
    end
    Gemini[Gemini Vision Model]

    User -->|Budget, Occasion, Style, Outfit Image| P3_3_1
    P3_3_1 --> P3_3_2
    P3_3_2 --> P3_3_3
    P3_3_3 --> P3_3_4
    P3_3_4 -->|Image + Prompt| Gemini
    Gemini -->|Color harmony + JSON item list| P3_3_5
    P3_3_5 --> P3_3_6
    P3_3_6 -->|Harmonized Jewelry Plan| User
```

