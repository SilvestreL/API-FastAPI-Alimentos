from app.db.session import engine
from sqlmodel import (
    SQLModel,
)
from app.models import usuario, company, produto, etiqueta


def create_tables() -> None:
    print("Creating tables...")
    SQLModel.metadata.create_all(engine)
    print("Done!")


if __name__ == "__main__":
    create_tables()
