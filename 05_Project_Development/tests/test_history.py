def test_history_unauthenticated_fails(client):
    """TC-17: Guest / unauthenticated request to /history returns 401."""
    response = client.get("/history")
    assert response.status_code == 401

def test_history_authenticated_lifecycle(client, auth_headers):
    """TC-18, TC-19, TC-20: Create recommendation, list history, view details, and delete."""
    # 1. Generate a home plan while authenticated so it gets persisted
    payload = {
        "budget": 1200.0,
        "room_type": "Studio Apartment",
        "style": "Industrial Loft",
        "required_items": ["Desk", "Task Chair", "Desk Lamp"]
    }
    create_res = client.post("/generate-home", json=payload, headers=auth_headers)
    assert create_res.status_code == 200
    rec_id = create_res.json()["id"]
    assert rec_id is not None

    # 2. TC-18: Retrieve history list
    hist_res = client.get("/history", headers=auth_headers)
    assert hist_res.status_code == 200
    items = hist_res.json()
    assert len(items) >= 1
    found = any(i["id"] == rec_id for i in items)
    assert found is True

    # 3. TC-19: Retrieve details via /recommendations-details?id=...
    det_res = client.get(f"/recommendations-details?id={rec_id}", headers=auth_headers)
    assert det_res.status_code == 200
    det_data = det_res.json()
    assert det_data["id"] == rec_id
    assert det_data["category"] == "home"
    assert "details" in det_data
    assert det_data["budget"] == 1200.0

    # 4. TC-20: Delete recommendation record
    del_res = client.delete(f"/history/{rec_id}", headers=auth_headers)
    assert del_res.status_code == 200

    # Verify that it is now gone
    det_after_del = client.get(f"/recommendations-details?id={rec_id}", headers=auth_headers)
    assert det_after_del.status_code == 404

