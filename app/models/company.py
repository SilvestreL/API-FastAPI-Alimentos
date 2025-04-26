from sqlmodel import SQLModel, Field
from typing import Optional


class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
