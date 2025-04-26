from sqlmodel import Session
from app.models.usuario import User
from app.models.company import Company
from app.core.security import get_password_hash
from app.db.session import engine


def init_db() -> None:
    with Session(engine) as session:
        # Verifica se já existe uma empresa
        company = session.query(Company).first()
        if not company:
            company = Company(nome="Empresa Padrão")
            session.add(company)
            session.commit()
            session.refresh(company)

        # Verifica se já existe um usuário admin
        admin = session.query(User).filter(User.email == "admin@example.com").first()
        if not admin:
            admin = User(
                name="Admin Master",
                email="admin@example.com",
                hashed_password=get_password_hash("123456"),
                role="administrator",
                company_id=company.id,
            )
            session.add(admin)
            session.commit()
