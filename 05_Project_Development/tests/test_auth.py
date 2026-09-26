from backend.app.auth import verify_password

def test_register_user_success(client):
    """TC-01: Register valid new user."""
    payload = {
        "username": "sarah_connor",
        "email": "sarah@example.com",
        "password": "strongPassword123"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "sarah_connor"
    assert data["email"] == "sarah@example.com"
    assert "id" in data

def test_register_duplicate_username(client, test_user):
    """TC-02: Register duplicate username fails."""
    payload = {
        "username": test_user.username,
        "email": "another@example.com",
        "password": "password123"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 400
    assert "Username already registered" in response.json()["detail"]

def test_register_duplicate_email(client, test_user):
    """TC-03: Register duplicate email fails."""
    payload = {
        "username": "different_user",
        "email": test_user.email,
        "password": "password123"
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 400
    assert "Email address already registered" in response.json()["detail"]

def test_login_success(client, test_user):
    """TC-04: Successful login returns token."""
    payload = {
        "username": test_user.username,
        "password": "password123"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["user"]["username"] == test_user.username
    assert "access_token" in response.cookies

def test_login_invalid_password(client, test_user):
    """TC-05: Login with incorrect password returns 401."""
    payload = {
        "username": test_user.username,
        "password": "wrong_password"
    }
    response = client.post("/login", json=payload)
    assert response.status_code == 401

def test_session_info_unauthenticated(client):
    """TC-06: Check unauthenticated session."""
    response = client.get("/session-info")
    assert response.status_code == 200
    data = response.json()
    assert data["authenticated"] is False
    assert data["session_active"] is False

def test_session_info_authenticated(client, auth_headers, test_user):
    """TC-07: Check authenticated session."""
    response = client.get("/session-info", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["authenticated"] is True
    assert data["username"] == test_user.username
    assert data["session_active"] is True

def test_session_data_endpoint(client, auth_headers, test_user):
    """TC-07b: Check /session-data route explicitly."""
    response = client.get("/session-data", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["authenticated"] is True
    assert data["username"] == test_user.username

