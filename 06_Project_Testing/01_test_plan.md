# Phase 6: Comprehensive Test Plan
## PocketSmart AI — Verification & Validation Strategy

---

### 1. Test Objectives & Scope
The test suite validates the reliability, security, accuracy, and fault tolerance of the **PocketSmart AI** web service.
Specific focus areas:
1. **Budget Enforcement**: Strict verification that `total_estimated_cost <= budget` across all planners.
2. **Authentication & Session Lifecycle**: Password hashing, JWT token verification, `/session-info`, and protected routes.
3. **Multimodal Robustness**: Image upload validation (valid image vs. invalid file types vs. text-only fallback).
4. **Resilience & Fallback**: Guaranteed response delivery even when Gemini API key is missing, invalid, or experiencing rate limits.
5. **History & Persistence**: Correct storage, retrieval via `/recommendations-details`, and deletion of recommendation records.

---

### 2. Test Environment
* **Platform**: Windows 11 / x64, Python 3.11.
* **Test Framework**: `pytest` 8.0+ and `pytest-asyncio`.
* **HTTP Test Client**: `httpx.AsyncClient` / `starlette.testclient.TestClient`.
* **Database**: In-memory SQLite (`sqlite:///:memory:`) for isolated, idempotent test runs.

---

### 3. Pass / Fail Criteria
* **Unit & Integration Suite**: 100% of all 20 test cases must PASS without unhandled exceptions.
* **HTTP Status Code Conformity**:
  * 200 OK for successful queries.
  * 201 Created for account creation.
  * 400 Bad Request for duplicate credentials or malformed inputs.
  * 401 Unauthorized for unauthenticated access to protected routes.
  * 404 Not Found for non-existent recommendation IDs.
  * 422 Unprocessable Entity for invalid schema types.

