from sqlmodel import Session, select
from app.models.usuario import User
from app.schemas.usuario import UserCreate
from app.core.security import get_password_hash


def create_user(session: Session, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed_password,
        role=user_in.role,
        company_id=None,
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


def get_users(session: Session) -> list[User]:
    return session.exec(select(User)).all()
