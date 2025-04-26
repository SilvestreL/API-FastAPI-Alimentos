from sqlmodel import Session, select
from app.models.produto import Product
from app.schemas.produto import ProductCreate


def create_product(
    session: Session, product_in: ProductCreate, company_id: int
) -> Product:
    product = Product.from_orm(product_in)
    product.company_id = company_id
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def get_product(session: Session, product_id: int) -> Product:
    return session.get(Product, product_id)


def get_products_by_company(session: Session, company_id: int) -> list[Product]:
    return session.exec(select(Product).where(Product.company_id == company_id)).all()
