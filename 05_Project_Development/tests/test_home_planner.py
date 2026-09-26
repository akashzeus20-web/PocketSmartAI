def test_generate_home_plan_valid(client):
    """TC-08: Generate valid home plan."""
    payload = {
        "budget": 2000.0,
        "room_type": "Living Room",
        "style": "Scandinavian Minimalist",
        "required_items": ["Sofa", "Coffee Table", "Floor Lamp", "Area Rug"]
    }
    response = client.post("/generate-home", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["budget"] == 2000.0
    assert data["total_estimated_cost"] <= 2000.0
    assert len(data["items"]) > 0
    for item in data["items"]:
        assert "estimated_price" in item
        assert "vendor_link" in item
        assert "link_type" in item

def test_home_planner_budget_ceiling(client):
    """TC-09: Verifies that items never exceed the provided budget ceiling."""
    payload = {
        "budget": 350.0,
        "room_type": "Bedroom",
        "style": "Bohemian Chic",
        "required_items": ["Bed Frame", "Nightstand", "Pendant Light", "Rug", "Plant Stand"]
    }
    response = client.post("/generate-home", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total_estimated_cost"] <= 350.0
    assert data["remaining_budget"] >= 0.0

def test_home_planner_negative_budget(client):
    """TC-10: Rejects non-positive or negative budget."""
    payload = {
        "budget": -500.0,
        "room_type": "Living Room",
        "style": "Industrial"
    }
    response = client.post("/generate-home", json=payload)
    assert response.status_code == 422

def test_home_planner_authenticated_persistence(client, auth_headers):
    """TC-10b: Authenticated home planning automatically persists record to DB."""
    payload = {
        "budget": 1800.0,
        "room_type": "Dining Room",
        "style": "Modern Japandi",
        "required_items": ["Dining Table", "Chairs"]
    }
    response = client.post("/generate-home", json=payload, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None

