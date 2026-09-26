# Phase 2: Agile User Stories & Acceptance Criteria
## PocketSmart AI — Product Backlog & Story Epics

---

### Epic 1: User Account Lifecycle & Security

#### US-101: User Self-Registration
* **As a** new visitor to PocketSmart AI,
* **I want to** register an account using my username, email, and password,
* **So that** my personal budget recommendations are privately saved.
* **Acceptance Criteria**:
  * *Scenario 1: Valid registration*
    * **Given** a unique username, valid email, and password with >= 6 characters,
    * **When** I submit the registration form,
    * **Then** my password is salt-hashed with bcrypt, a new user row is created in SQLite, and I receive a 201 Created status with a redirect to login.
  * *Scenario 2: Duplicate email or username*
    * **Given** an existing username or email,
    * **When** I submit registration,
    * **Then** the system returns HTTP 400 with a clear error: "Username or email already registered."

#### US-102: Authentication & Token Issuance
* **As a** registered user,
* **I want to** authenticate with my credentials and receive a JWT token,
* **So that** I can make authenticated requests to protected planner endpoints.
* **Acceptance Criteria**:
  * Valid credentials return a signed JWT token with expiry (default: 24 hours).
  * The endpoints `/session-info` and `/session-data` verify token validity and return current username.
  * Logging out clears client-stored tokens and invalidates the session context.

---

### Epic 2: Intelligent Home Interior Budget Planner

#### US-201: Multi-Item Budget Allocation
* **As a** homeowner redecorating a space,
* **I want to** provide my total budget, target room type, aesthetic style, and prioritized item list,
* **So that** I receive a balanced shopping list that doesn't exceed my budget.
* **Acceptance Criteria**:
  * **Given** a budget of \$1,800, room "Living Room", style "Mid-Century Modern", and items "Sofa, Coffee Table, Floor Lamp, Rug",
  * **When** I click "Generate Home Plan",
  * **Then** the system returns recommendations containing furniture, lighting, and decor whose total estimated price <= \$1,800.
  * Items are labeled clearly with category, estimated price, and mock vendor links.

---

### Epic 3: Event & Party Budget Planner

#### US-301: Proportional Headcount Budgeting
* **As a** party organizer,
* **I want to** provide the event type, budget, guest count, and venue type,
* **So that** the system automatically splits my funds into catering, venue, decor, and entertainment.
* **Acceptance Criteria**:
  * **Given** a budget of \$1,000 for a 20-person Birthday party at home,
  * **When** I generate the party plan,
  * **Then** the system outputs a categorized financial breakdown (e.g., Catering ~\$450, Decor ~\$200, Venue ~\$150, Entertainment ~\$150, Reserve ~\$50) and a per-guest allocation metric of \$50/head.

---

### Epic 4: Jewelry & Multimodal Outfit Matching

#### US-401: Multimodal Outfit Image Analysis
* **As a** fashion-conscious consumer attending an event,
* **I want to** upload a photo of my outfit alongside my budget,
* **So that** the AI analyzes my outfit's colors, textures, and neckline to suggest matching jewelry.
* **Acceptance Criteria**:
  * **Given** an uploaded JPEG/PNG dress photo and a budget of \$250,
  * **When** I submit the jewelry planner form,
  * **Then** the Gemini Vision API evaluates the image tones (e.g., navy blue, v-neck) and returns complementary jewelry (e.g., silver pendant, teardrop crystal earrings) totaling <= \$250.
  * The response includes specific styling commentary explaining why these metals and stones complement the garment.

---

### Epic 5: Recommendation Archiving & History

#### US-501: History Inspection & Detailed Retrieval
* **As an** authenticated user,
* **I want to** review my past saved recommendations and click into their full details,
* **So that** I can review items later or compare different options before purchasing.
* **Acceptance Criteria**:
  * Navigating to `/history` lists all past plans generated under the logged-in user.
  * Clicking "View Details" opens the exact stored breakdown with all item prices, links, and styling notes.

