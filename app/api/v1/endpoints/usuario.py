from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.usuario import UserCreate, UserRead
from app.crud.crud_usuario import create_user, get_user, get_users

router = APIRouter()


@router.post("/", response_model=UserRead)
def create(user_in: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user_in)


@router.get("/{user_id}", response_model=UserRead)
def read(user_id: int, session: Session = Depends(get_session)):
    return get_user(session, user_id)


@router.get("/", response_model=list[UserRead])
def read_all(session: Session = Depends(get_session)):
    return get_users(session)
