# Teste-Backend-FastAPI

Projeto desenvolvido para avaliação técnica de back-end, utilizando **FastAPI**, **PostgreSQL**, **Docker** e **Testes Automatizados**.

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker + Docker Compose](https://www.docker.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Adminer](https://www.adminer.org/)

---

## 🛠️ Como Executar

### 𞿖️ Usando Docker (recomendado)

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/teste-backend-fastapi.git
cd teste-backend-fastapi
```

2. Copie o arquivo de exemplo de variáveis de ambiente:

```bash
cp .env.example .env
```

**Conteúdo do `.env.example`:**

```env
FIRST_SUPERUSER=admin@example.com
FIRST_SUPERUSER_PASSWORD=123456
```

3. Suba os containers:

```bash
docker-compose up --build
```

4. Acesse:

- API FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger)
- Adminer (Gerenciador de banco de dados): [http://localhost:8080](http://localhost:8080)

---

### 💻 Rodar Localmente (sem Docker)

1. Instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure o arquivo `.env` baseado no `.env.example`.

3. Rode o servidor:

```bash
uvicorn app.main:app --reload
```

(O banco de dados PostgreSQL precisa estar rodando na sua máquina.)

---

## 🔐 Autenticação

Utilizamos **JWT Token** para proteger as rotas privadas.

Para fazer login:

```
POST /api/v1/auth/login
```

Credenciais padrão:

```json
{
  "username": "admin@example.com",
  "password": "123456"
}
```

---

## 📚 Endpoints Principais

### 🧑‍💼 Usuários

| Método | Endpoint                  | Descrição                 |
| :----- | :------------------------ | :------------------------ |
| POST   | `/api/v1/users/`          | Criar novo usuário        |
| GET    | `/api/v1/users/`          | Listar usuários           |
| GET    | `/api/v1/users/{user_id}` | Buscar usuário específico |

### 𞿖️ Produtos

| Método | Endpoint                        | Descrição                 |
| :----- | :------------------------------ | :------------------------ |
| POST   | `/api/v1/products/`             | Criar produto             |
| GET    | `/api/v1/products/`             | Listar produtos           |
| GET    | `/api/v1/products/{product_id}` | Buscar produto específico |

### 🏢 Empresas

| Método | Endpoint                         | Descrição                 |
| :----- | :------------------------------- | :------------------------ |
| POST   | `/api/v1/companies/`             | Criar empresa             |
| GET    | `/api/v1/companies/`             | Listar empresa do usuário |
| GET    | `/api/v1/companies/{company_id}` | Buscar empresa específica |

### 🏷️ Etiquetas (Validade)

| Método | Endpoint                                  | Descrição                            |
| :----- | :---------------------------------------- | :----------------------------------- |
| GET    | `/api/v1/validade/expired-labels`         | Listar etiquetas vencidas            |
| GET    | `/api/v1/validade/near-expiration-labels` | Listar etiquetas perto do vencimento |

---

## 🧪 Testes Automatizados

Para rodar os testes:

```bash
pytest -v
```

Para gerar um relatório de cobertura:

```bash
pytest --cov=app tests/
```

---

## 📂 Estrutura de Pastas

```
app/
├── api/
│   ├── deps.py
│   └── v1/
├── crud/
├── db/
├── models/
├── schemas/
├── core/
├── scripts/
├── main.py
tests/
docker-compose.yml
Dockerfile
.env.example
requirements.txt
```

---

## 🧵 Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch com a sua feature:

```bash
git checkout -b minha-feature
```

3. Faça commit das suas alterações:

```bash
git commit -m 'feat: Minha nova feature'
```

4. Envie para o seu repositório:

```bash
git push origin minha-feature
```

5. Abra um Pull Request! 🚀

---

## 📝 Licença

Este projeto está sob a licença MIT.
