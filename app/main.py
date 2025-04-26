from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api_v1_router import router as api_v1_router

# Cria o app
app = FastAPI(
    title="Sistema de Gestão de Produtos e Etiquetas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# CORS Settings (liberar frontend ou Postman sem erro de CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque "*" por seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas
app.include_router(api_v1_router, prefix="/api/v1")

# Rodar: uvicorn app.main:app --reload
