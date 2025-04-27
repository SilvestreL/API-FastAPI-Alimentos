from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.company import CompanyCreate, CompanyRead
from app.crud.crud_company import create_company, get_company, get_companies
from app.api.deps import get_current_user
from app.models.usuario import User

router = APIRouter()


@router.post("/", response_model=CompanyRead)
def create(
    company_in: CompanyCreate,
    session: Session = Depends(get_session),
):
    """
    Cria uma nova empresa (não precisa autenticação obrigatória).
    """
    return create_company(session, company_in)


@router.get("/{company_id}", response_model=CompanyRead)
def read(
    company_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Retorna uma empresa se for a mesma do usuário logado.
    """
    company = get_company(session, company_id)
    if not company or company.id != current_user.company_id:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return company


@router.get("/", response_model=list[CompanyRead])
def read_all(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Lista apenas a empresa do usuário atual.
    """
    companies = get_companies(session)
    # Só retorna a empresa do usuário
    return [company for company in companies if company.id == current_user.company_id]
