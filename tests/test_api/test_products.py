import pytest


@pytest.fixture
def token(client):
    # Faz o login para obter o token
    login_data = {
        "username": "admin@example.com",
        "password": "123456",
    }
    response = client.post("/api/v1/auth/login", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]


def test_create_product(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    product_data = {
        "nome": "Produto Teste",
        "descricao": "Descrição de teste",
        "unidade_medida": "kg",
        "metodo_conservacao": "refrigerado",
        "status": "ativo",
    }
    response = client.post("/api/v1/products/", json=product_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Produto Teste"
    assert data["unidade_medida"] == "kg"


def test_get_products(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/v1/products/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Verifica se retornou uma lista
