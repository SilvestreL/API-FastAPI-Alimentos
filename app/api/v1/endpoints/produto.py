from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.produto import ProductCreate, ProductRead
from app.crud.crud_produto import create_product, get_product, get_products_by_company

# Aqui você poderia colocar uma dependência que pega o current_user para puxar o company_id também
router = APIRouter()


@router.post("/", response_model=ProductRead)
def create(product_in: ProductCreate, session: Session = Depends(get_session)):
    company_id = 1  # depois trocar para pegar do JWT!
    return create_product(session, product_in, company_id)


@router.get("/{product_id}", response_model=ProductRead)
def read(product_id: int, session: Session = Depends(get_session)):
    return get_product(session, product_id)


@router.get("/", response_model=list[ProductRead])
def read_all(session: Session = Depends(get_session)):
    company_id = 1  # depois trocar para pegar do JWT!
    return get_products_by_company(session, company_id)
