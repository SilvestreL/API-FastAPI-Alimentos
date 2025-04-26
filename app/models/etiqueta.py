from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional


class Etiqueta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    produto_id: int = Field(foreign_key="product.id")
    quantidade: float
    unidade_medida: str
    data_producao: date
    data_validade: date
    metodo_conservacao: str
    status: str
    company_id: int = Field(foreign_key="company.id")
