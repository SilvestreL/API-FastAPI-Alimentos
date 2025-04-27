def test_create_user(client, get_token):
    """
    Testa a criação de um novo usuário.
    """
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}
    user_data = {
        "name": "Usuário Teste",
        "email": "testeuser@example.com",
        "password": "testesenha",
        "role": "user",
    }
    response = client.post("/api/v1/users/", json=user_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "testeuser@example.com"
    assert "id" in data


def test_get_user_by_id(client, get_token):
    """
    Testa a obtenção de um usuário específico.
    """
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}

    # Primeiro, cria um usuário para garantir que existe
    user_data = {
        "name": "Outro Usuário",
        "email": "outroteste@example.com",
        "password": "testesenha",
        "role": "user",
    }
    create_response = client.post("/api/v1/users/", json=user_data, headers=headers)
    assert create_response.status_code == 200
    created_user = create_response.json()

    user_id = created_user["id"]

    # Agora tenta buscar o usuário
    response = client.get(f"/api/v1/users/{user_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "outroteste@example.com"
    assert data["id"] == user_id


def test_get_all_users(client, get_token):
    """
    Testa a listagem de usuários.
    """
    token = get_token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/users/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
