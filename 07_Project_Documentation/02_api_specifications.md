# Phase 7: REST API Specifications
## PocketSmart AI — Endpoint Reference & Contract Catalog

---

### Base URLs
* **Local Development**: `http://127.0.0.1:8000`
* **Interactive Swagger UI**: `http://127.0.0.1:8000/docs`
* **Interactive ReDoc UI**: `http://127.0.0.1:8000/redoc`

---

### 1. Authentication Endpoints

#### `POST /register`
* **Description**: Creates a new user record.
* **Payload**:
```json
{
  "username": "alex_smith",
  "email": "alex@example.com",
  "password": "Password123"
}
```
* **Success Response (201 Created)**:
```json
{
  "id": 1,
  "username": "alex_smith",
  "email": "alex@example.com",
  "created_at": "2026-09-26T21:40:00Z"
}
```

#### `POST /login`
* **Description**: Verifies credentials, returns JWT bearer token, and sets HTTP-only session cookie.
* **Payload**:
```json
{
  "username": "alex_smith",
  "password": "Password123"
}
```
* **Success Response (200 OK)**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsIn...",
  "token_type": "bearer",
  "expires_in": 86400,
  "user": {
    "id": 1,
    "username": "alex_smith",
    "email": "alex@example.com",
    "created_at": "2026-09-26T21:40:00Z"
  }
}
```

#### `POST /token`
* **Description**: Standard OAuth2 Password form endpoint. Accepts `application/x-www-form-urlencoded` fields `username` and `password`.

#### `POST /logout`
* **Description**: Clears the session cookie.
* **Success Response (200 OK)**: `{"status": "success", "message": "Successfully logged out."}`

#### `GET /session-info` & `GET /session-data`
* **Description**: Inspects token or session cookie and returns user authentication status.
* **Success Response (200 OK)**:
```json
{
  "authenticated": true,
  "user_id": 1,
  "username": "alex_smith",
  "email": "alex@example.com",
  "session_active": true
}
```

---

### 2. AI Budget Planning Endpoints

#### `POST /generate-home`
* **Description**: Generates an interior furnishing plan within budget.
* **Payload**:
```json
{
  "budget": 2000.0,
  "room_type": "Living Room",
  "style": "Scandinavian Minimalist",
  "required_items": ["Sofa", "Coffee Table", "Floor Lamp", "Area Rug"]
}
```
* **Response (200 OK)**: Returns `HomePlannerResponse` with itemized prices, sample links, and design tips.

#### `POST /generate-party`
* **Description**: Computes proportional budget breakdown and checklist for gatherings.
* **Payload**:
```json
{
  "occasion": "30th Birthday Bash",
  "budget": 1500.0,
  "guest_count": 25,
  "venue_type": "Home / Backyard"
}
```
* **Response (200 OK)**: Returns `PartyPlannerResponse` with per-guest metrics, 4-pillar budget allocation, items, and prep checklist.

#### `POST /generate-jewelry`
* **Description**: Generates jewelry suggestions matching an occasion, with optional outfit image upload.
* **Content-Type**: `multipart/form-data`
  * `budget`: float
  * `occasion`: string
  * `style_preference`: string
  * `image`: binary file (optional)
* **Response (200 OK)**: Returns `JewelryPlannerResponse` with vision analysis, metal recommendation, and items.

---

### 3. History & Persistence Endpoints

#### `GET /history`
* **Description**: Retrieves array of past recommendation summaries for the authenticated user.
* **Headers**: `Authorization: Bearer <token>`
* **Response (200 OK)**: `[{"id": 1, "category": "home", "title": "...", "budget": 2000.0, ...}]`

#### `GET /recommendations-details`
* **Description**: Retrieves full recommendation payload by query parameter `?id={id}`.
* **Headers**: `Authorization: Bearer <token>`

#### `GET /recommendations-details/{id}`
* **Description**: Retrieves full recommendation payload by path parameter `{id}`.

#### `DELETE /history/{id}`
* **Description**: Deletes a saved recommendation record.

