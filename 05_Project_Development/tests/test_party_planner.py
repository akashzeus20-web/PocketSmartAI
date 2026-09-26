def test_generate_party_plan_valid(client):
    """TC-11: Generate valid party plan."""
    payload = {
        "occasion": "30th Birthday Bash",
        "budget": 1500.0,
        "guest_count": 25,
        "venue_type": "Home / Backyard"
    }
    response = client.post("/generate-party", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["budget"] == 1500.0
    assert data["total_estimated_cost"] <= 1500.0
    assert "allocations" in data
    assert "catering_and_drinks" in data["allocations"]
    assert "checklist" in data
    assert len(data["checklist"]) >= 3

def test_party_planner_per_guest_calc(client):
    """TC-12: Verifies correct per-guest financial metric calculation."""
    payload = {
        "occasion": "Team Dinner",
        "budget": 1000.0,
        "guest_count": 20,
        "venue_type": "Rented Community Hall"
    }
    response = client.post("/generate-party", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["per_guest_cost"] == 50.00
    assert data["total_estimated_cost"] <= 1000.0

def test_party_planner_zero_guests(client):
    """TC-13: Rejects guest count of zero."""
    payload = {
        "occasion": "Solo Gathering",
        "budget": 500.0,
        "guest_count": 0,
        "venue_type": "Home"
    }
    response = client.post("/generate-party", json=payload)
    assert response.status_code == 422

