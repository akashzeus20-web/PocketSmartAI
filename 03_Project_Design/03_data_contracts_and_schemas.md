# Phase 3: Data Contracts & API Schemas
## PocketSmart AI — OpenAPI & JSON Schema Contracts

---

### 1. Authentication Endpoints

#### 1.1 `POST /register`
* **Request Content-Type**: `application/json`
* **Request Schema**:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "username": { "type": "string", "minLength": 3, "maxLength": 50 },
    "email": { "type": "string", "format": "email" },
    "password": { "type": "string", "minLength": 6 }
  },
  "required": ["username", "email", "password"]
}
```
* **Response Status**: `201 Created`
```json
{
  "status": "success",
  "message": "User registered successfully",
  "user_id": 1,
  "username": "alex"
}
```

#### 1.2 `POST /login` & `POST /token`
* **Request Content-Type**: `application/x-www-form-urlencoded` or `application/json`
* **Response Status**: `200 OK`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsIn...",
  "token_type": "bearer",
  "expires_in": 86400,
  "user": {
    "id": 1,
    "username": "alex",
    "email": "alex@example.com"
  }
}
```

#### 1.3 `GET /session-info` & `GET /session-data`
* **Headers**: `Authorization: Bearer <token>` (or cookie session)
* **Response Status**: `200 OK`
```json
{
  "authenticated": true,
  "user_id": 1,
  "username": "alex",
  "email": "alex@example.com",
  "session_active": true
}
```

---

### 2. Planner Endpoints

#### 2.1 `POST /generate-home`
* **Request Content-Type**: `application/json`
* **Request Schema**:
```json
{
  "budget": 2000.0,
  "room_type": "Living Room",
  "style": "Scandinavian Minimalist",
  "required_items": ["Sofa", "Coffee Table", "Floor Lamp", "Area Rug"]
}
```
* **Response Schema**:
```json
{
  "id": 101,
  "category": "home",
  "title": "Scandinavian Minimalist Living Room Plan",
  "budget": 2000.0,
  "total_estimated_cost": 1890.0,
  "remaining_budget": 110.0,
  "is_sample_data": false,
  "items": [
    {
      "name": "Nordic 3-Seater Fabric Sofa",
      "category": "Key Furniture",
      "quantity": 1,
      "estimated_price": 950.0,
      "description": "Clean lines, solid oak legs, neutral gray fabric.",
      "vendor_link": "https://www.ikea.com/sample/nordic-sofa",
      "link_type": "mock_sample"
    },
    {
      "name": "Round Oak Coffee Table",
      "category": "Key Furniture",
      "quantity": 1,
      "estimated_price": 280.0,
      "description": "Minimalist circular low coffee table with matte finish.",
      "vendor_link": "https://www.target.com/sample/oak-table",
      "link_type": "mock_sample"
    }
  ],
  "budget_breakdown": {
    "furniture": 1230.0,
    "lighting": 260.0,
    "decor": 400.0
  },
  "design_tips": [
    "Position the floor lamp in the corner to create soft ambient layering.",
    "Use natural wool textures to enhance Scandinavian warmth."
  ],
  "created_at": "2026-09-26T21:40:00Z"
}
```

#### 2.2 `POST /generate-party`
* **Request Content-Type**: `application/json`
* **Request Schema**:
```json
{
  "occasion": "30th Birthday Bash",
  "budget": 1500.0,
  "guest_count": 25,
  "venue_type": "Backyard / Outdoor Patio"
}
```
* **Response Schema**:
```json
{
  "id": 102,
  "category": "party",
  "title": "30th Birthday Bash (25 Guests)",
  "budget": 1500.0,
  "total_estimated_cost": 1420.0,
  "per_guest_cost": 56.80,
  "remaining_budget": 80.0,
  "is_sample_data": false,
  "allocations": {
    "catering_and_drinks": 675.0,
    "venue_and_rentals": 300.0,
    "decorations": 250.0,
    "entertainment_and_favors": 195.0
  },
  "items": [
    {
      "name": "Artisan Sliders & Finger Food Platter",
      "category": "Catering",
      "quantity": 25,
      "estimated_price": 450.0,
      "description": "Gourmet sliders, veggie skewers, and mini tacos.",
      "vendor_link": "https://sample-catering.local/sliders",
      "link_type": "mock_sample"
    }
  ],
  "checklist": [
    "Confirm outdoor string lighting and extension cords.",
    "Arrange ice buckets 3 hours prior to kickoff."
  ]
}
```

#### 2.3 `POST /generate-jewelry`
* **Request Content-Type**: `multipart/form-data`
  * `budget`: float (required)
  * `occasion`: string (required)
  * `style_preference`: string (required)
  * `image`: binary file (optional; JPEG/PNG/WEBP)
* **Response Schema**:
```json
{
  "id": 103,
  "category": "jewelry",
  "title": "Gala Evening Jewelry Collection",
  "budget": 500.0,
  "total_estimated_cost": 465.0,
  "remaining_budget": 35.0,
  "vision_analysis": {
    "image_processed": true,
    "detected_colors": ["Emerald Green", "Gold undertone"],
    "neckline_detected": "Sweetheart / Off-shoulder",
    "aesthetic_profile": "Opulent formal evening attire"
  },
  "recommended_metal": "18k Yellow Gold or Warm Vermeil",
  "items": [
    {
      "name": "Teardrop Emerald & Gold Chandelier Earrings",
      "category": "Earrings",
      "quantity": 1,
      "estimated_price": 220.0,
      "description": "Matches emerald green gown with brilliant warm accents.",
      "vendor_link": "https://www.bluenile.com/sample/emerald-drops",
      "link_type": "mock_sample"
    }
  ],
  "styling_advice": "Because your dress has a sweetheart neckline, keep the necklace delicate to keep focal attention on the statement chandelier earrings."
}
```

---

### 3. History Endpoints
* `GET /history`: Returns array of user's past recommendations summary.
* `GET /recommendations-details?id=101` or `GET /recommendations-details/{id}`: Returns complete JSON payload.
* `DELETE /history/{id}`: Deletes recommendation.

