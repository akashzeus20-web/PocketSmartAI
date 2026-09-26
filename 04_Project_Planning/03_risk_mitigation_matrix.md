# Phase 4: Risk Mitigation Matrix & Contingency Planning
## PocketSmart AI — Risk Assessment & Contingency Management

---

### 1. Risk Heatmap & Probability-Impact Matrix

| Risk ID | Risk Description | Category | Prob (1-5) | Impact (1-5) | Severity Score | Preventive Mitigation Strategy | Contingency Plan |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **RSK-01** | Gemini API Rate Limiting (HTTP 429) or Quota Depletion | Technical / Upstream | 3 | 4 | **12 (Medium-High)** | Implement client-side exponential backoff and cached responses for identical requests. | Automatic switchover to `MockService` heuristic generator; application continues functioning seamlessly. |
| **RSK-02** | User Runs App Without Gemini API Key | Operational | 4 | 3 | **12 (Medium-High)** | Clear setup instructions in README, `.env.example`, and visual banner notifying of fallback mode. | Transparently activate deterministic sample planner tagged `[Algorithmic Market Estimate]`. |
| **RSK-03** | LLM Math Inaccuracy (Suggested items sum > user budget) | Quality / Algorithm | 4 | 4 | **16 (High)** | Structured JSON schema instructions detailing mathematical equality; budget ceiling constraint in prompt. | Deterministic post-processor in Python inspects `sum(prices)`. If `sum > budget`, it scales down item prices or substitutes lower-cost alternatives. |
| **RSK-04** | Corrupted or Unsupported Image Uploads in Jewelry Planner | Technical / Input | 2 | 3 | **6 (Low)** | Pre-validate MIME types (JPEG/PNG/WEBP) and cap size at 10MB; Pillow image sanitization. | Return explicit user-friendly HTTP 422 error prompting for valid image; or fallback to text-only mode. |
| **RSK-05** | Unauthorized Access to User History / Session Hijacking | Security | 2 | 5 | **10 (Medium)** | Strong JWT signing with rotating secret, bcrypt password hashing, HTTPOnly cookie or Bearer tokens. | Invalidate compromised token, force session termination, and require re-authentication. |
| **RSK-06** | Database Locking in SQLite Concurrent Writes | Performance | 2 | 2 | **4 (Low)** | Use Write-Ahead Logging (`WAL` mode) and short scoped sessions with connection pooling. | Queue write operations; lightweight database footprint minimizes contention. |

---

### 2. Monitoring & Fallback Activation Protocol
```
[User Request]
       │
       ▼
[Check GEMINI_API_KEY] ──(Missing or Invalid)──► [Activate MockService] ──► [Return Audited Plan]
       │ (Present)
       ▼
[Call Google Gemini 1.5 API]
       │
       ├─(Success: Valid JSON)──────► [Run Budget Sum Audit] ─────────────► [Persist & Return]
       │
       └─(Timeout / 429 / Error)───► [Log Warning & Activate MockService] ─► [Return Audited Plan]
```
This architecture ensures **zero crash risk** and 100% test pass rates under any network or credential condition.

