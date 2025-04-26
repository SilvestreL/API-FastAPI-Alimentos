from fastapi import APIRouter
from app.api.v1.endpoints import company, usuario, produto, auth

router = APIRouter()

router.include_router(company.router, prefix="/companies", tags=["Companies"])
router.include_router(usuario.router, prefix="/users", tags=["Users"])
router.include_router(produto.router, prefix="/products", tags=["Products"])
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
