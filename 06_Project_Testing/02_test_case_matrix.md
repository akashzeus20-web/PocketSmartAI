# Phase 6: 20-Case Test Matrix
## PocketSmart AI — Test Cases & Execution Specifications

---

| Test ID | Module | Test Description | Input Data | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Auth | Register valid new user | Unique username, valid email, strong password | HTTP 201 Created, user ID returned, password hashed | Passed |
| **TC-02** | Auth | Register duplicate username | Existing username | HTTP 400 Bad Request ("Username already registered") | Passed |
| **TC-03** | Auth | Register duplicate email | Existing email | HTTP 400 Bad Request ("Email address already registered") | Passed |
| **TC-04** | Auth | Successful login | Valid username & password | HTTP 200 OK, JWT bearer token, cookie set | Passed |
| **TC-05** | Auth | Login with incorrect password | Valid username, wrong password | HTTP 401 Unauthorized | Passed |
| **TC-06** | Auth | Check unauthenticated session | No Authorization header / no cookie | HTTP 200 OK, `authenticated: false` | Passed |
| **TC-07** | Auth | Check authenticated session | Valid Bearer token | HTTP 200 OK, `authenticated: true`, username matching | Passed |
| **TC-08** | Home | Generate home plan (valid) | Budget: $2000, Room: Living, Style: Scandinavian | HTTP 200 OK, items returned, `total <= 2000` | Passed |
| **TC-09** | Home | Budget ceiling enforcement | Budget: $500, extensive required items | HTTP 200 OK, `total_estimated_cost <= 500` | Passed |
| **TC-10** | Home | Reject negative budget | Budget: -$100 | HTTP 422 Unprocessable Entity | Passed |
| **TC-11** | Party | Generate party plan (valid) | Budget: $1500, Occasion: Birthday, Guests: 25 | HTTP 200 OK, allocations present, checklist present | Passed |
| **TC-12** | Party | Per-guest calculation | Budget: $1000, Guests: 20 | `per_guest_cost == 50.00`, `total <= 1000` | Passed |
| **TC-13** | Party | Reject zero guests | Guests: 0 | HTTP 422 Unprocessable Entity (`ge=1`) | Passed |
| **TC-14** | Jewelry | Generate jewelry (text only) | Budget: $300, Occasion: Wedding, Style: Gold | HTTP 200 OK, `total <= 300`, recommended metal present | Passed |
| **TC-15** | Jewelry | Generate jewelry with image | Budget: $400, sample JPEG outfit bytes | HTTP 200 OK, `image_processed: true`, vision analysis | Passed |
| **TC-16** | Jewelry | Reject invalid image type | `.txt` or `.exe` file upload | HTTP 400 Bad Request ("Unsupported image type") | Passed |
| **TC-17** | History | Protect history from guests | Unauthenticated `GET /history` | HTTP 401 Unauthorized | Passed |
| **TC-18** | History | Retrieve authenticated history | Authenticated `GET /history` | HTTP 200 OK, array of user's past recommendations | Passed |
| **TC-19** | History | Fetch recommendation details | Authenticated `GET /recommendations-details?id={id}` | HTTP 200 OK, complete JSON payload returned | Passed |
| **TC-20** | History | Delete recommendation | Authenticated `DELETE /history/{id}` | HTTP 200 OK, item deleted; subsequent query returns 404 | Passed |

