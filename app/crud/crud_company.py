from sqlmodel import Session, select
from app.models.company import Company
from app.schemas.company import CompanyCreate


def create_company(session: Session, company_in: CompanyCreate) -> Company:
    company = Company.from_orm(company_in)
    session.add(company)
    session.commit()
    session.refresh(company)
    return company


def get_company(session: Session, company_id: int) -> Company:
    return session.get(Company, company_id)


def get_companies(session: Session) -> list[Company]:
    return session.exec(select(Company)).all()
