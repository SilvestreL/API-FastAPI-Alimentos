from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str
    role: str  # administrator, company_administrator, company_employee
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
