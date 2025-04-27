from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.usuario import UserCreate, UserRead
from app.crud.crud_usuario import create_user, get_user, get_users
from app.api.deps import get_current_user
from app.models.usuario import User

router = APIRouter()


@router.post("/", response_model=UserRead)
def create(
    user_in: UserCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    # O usuário novo herda o company_id do usuário logado
    return create_user(session, user_in, company_id=current_user.company_id)


@router.get("/{user_id}", response_model=UserRead)
def read(
    user_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    user = get_user(session, user_id)
    if not user or user.company_id != current_user.company_id:
        raise HTTPException(
            status_code=404, detail="Usuário não encontrado"
        )  # Proteção pelo company
    return user


@router.get("/", response_model=list[UserRead])
def read_all(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return get_users(session, company_id=current_user.company_id)
