def test_login_success(client):
    login_data = {
        "username": "admin@example.com",  # OAuth2 exige username
        "password": "123456",
    }
    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_failure(client):
    login_data = {
        "username": "admin@example.com",
        "password": "senha_errada",
    }
    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 401
