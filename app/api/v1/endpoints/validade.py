from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from datetime import date, timedelta
from app.models.etiqueta import Etiqueta
from app.db.session import get_session

router = APIRouter()


@router.get("/expired-labels", response_model=list[Etiqueta])
def listar_etiquetas_vencidas(session: Session = Depends(get_session)):
    hoje = date.today()
    etiquetas = session.exec(
        select(Etiqueta).where(Etiqueta.data_validade < hoje)
    ).all()
    return etiquetas


@router.get("/near-expiration-labels", response_model=list[Etiqueta])
def listar_etiquetas_proximas(session: Session = Depends(get_session)):
    hoje = date.today()
    daqui_3_dias = hoje + timedelta(days=3)
    etiquetas = session.exec(
        select(Etiqueta).where(Etiqueta.data_validade.between(hoje, daqui_3_dias))
    ).all()
    return etiquetas
