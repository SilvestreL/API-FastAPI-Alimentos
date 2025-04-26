from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    nome: str
    descricao: str
    unidade_medida: str
    metodo_conservacao: str
    status: str


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int
    company_id: Optional[int]


class Config:
    from_attributes = True
