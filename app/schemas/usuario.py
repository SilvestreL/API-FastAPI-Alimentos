from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str  # administrator, company_administrator, company_employee


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    company_id: Optional[int]


class Config:
    from_attributes = True
