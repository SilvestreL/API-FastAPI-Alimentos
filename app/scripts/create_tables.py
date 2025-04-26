from app.db.session import engine
from sqlmodel import SQLModel
from app.models.company import Company
from app.models.produto import Product
from app.models.usuario import User
from app.models.etiqueta import Etiqueta


def create_tables() -> None:
    print("Creating tables...")
    SQLModel.metadata.create_all(engine)
    print("Done!")


if __name__ == "__main__":
    create_tables()
