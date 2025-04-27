from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from datetime import date, timedelta
from app.models.etiqueta import Etiqueta
from app.db.session import get_session
from app.api.deps import get_current_user
from app.models.usuario import User

router = APIRouter()


@router.get("/expired-labels", response_model=list[Etiqueta])
def listar_etiquetas_vencidas(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Lista etiquetas vencidas apenas da empresa do usuário logado.
    """
    hoje = date.today()
    etiquetas = session.exec(
        select(Etiqueta).where(
            Etiqueta.company_id == current_user.company_id,
            Etiqueta.data_validade < hoje,
        )
    ).all()
    return etiquetas


@router.get("/near-expiration-labels", response_model=list[Etiqueta])
def listar_etiquetas_proximas(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """
    Lista etiquetas próximas do vencimento (3 dias) da empresa do usuário logado.
    """
    hoje = date.today()
    daqui_3_dias = hoje + timedelta(days=3)
    etiquetas = session.exec(
        select(Etiqueta).where(
            Etiqueta.company_id == current_user.company_id,
            Etiqueta.data_validade.between(hoje, daqui_3_dias),
        )
    ).all()
    return etiquetas
