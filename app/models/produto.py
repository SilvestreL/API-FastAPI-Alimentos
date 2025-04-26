from sqlmodel import SQLModel, Field
from typing import Optional


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    unidade_medida: str
    metodo_conservacao: str
    status: str
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
