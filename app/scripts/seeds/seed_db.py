from app.db.session import get_session
from app.core.security import get_password_hash
from app.models.company import Company
from app.models.usuario import User


def seed():
    session = next(get_session())

    # Verifica se já existe uma empresa
    company = session.exec(Company).first()
    if not company:
        company = Company(nome="Empresa Exemplo")
        session.add(company)
        session.commit()
        session.refresh(company)

    # Verifica se já existe um usuário
    user = session.exec(User).filter(User.email == "admin@example.com").first()
    if not user:
        user = User(
            name="Admin",
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            role="administrator",
            company_id=company.id,
        )
        session.add(user)
        session.commit()

    print("✅ Banco populado com sucesso!")


if __name__ == "__main__":
    seed()
