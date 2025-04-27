from sqlmodel import Session, select
from app.models.usuario import User
from app.schemas.usuario import UserCreate
from app.core.security import get_password_hash


def create_user(session: Session, user_in: UserCreate, company_id: int) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed_password,
        role=user_in.role,
        company_id=company_id,  #  salva o company_id do criador
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_email(session: Session, email: str) -> User:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def get_user(session: Session, user_id: int) -> User:
    return session.get(User, user_id)


def get_users(session: Session, company_id: int) -> list[User]:
    statement = select(User).where(User.company_id == company_id)  # Filtra pela empresa
    return session.exec(statement).all()
