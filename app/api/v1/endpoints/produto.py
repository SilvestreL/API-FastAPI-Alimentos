from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.produto import ProductCreate, ProductRead
from app.crud.crud_produto import create_product, get_product, get_products_by_company
from app.api.deps import get_current_user
from app.models.usuario import User

router = APIRouter()


@router.post("/", response_model=ProductRead)
def create(
    product_in: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not current_user.company_id:
        raise HTTPException(status_code=400, detail="Usuário sem empresa associada.")

    return create_product(session, product_in, current_user.company_id)


@router.get("/{product_id}", response_model=ProductRead)
def read(
    product_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    product = get_product(session, product_id)
    if not product or product.company_id != current_user.company_id:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return product


@router.get("/", response_model=list[ProductRead])
def read_all(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return get_products_by_company(session, current_user.company_id)
