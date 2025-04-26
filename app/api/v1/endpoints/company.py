from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.company import CompanyCreate, CompanyRead
from app.crud.crud_company import create_company, get_company, get_companies

router = APIRouter()


@router.post("/", response_model=CompanyRead)
def create(company_in: CompanyCreate, session: Session = Depends(get_session)):
    return create_company(session, company_in)


@router.get("/{company_id}", response_model=CompanyRead)
def read(company_id: int, session: Session = Depends(get_session)):
    return get_company(session, company_id)


@router.get("/", response_model=list[CompanyRead])
def read_all(session: Session = Depends(get_session)):
    return get_companies(session)
