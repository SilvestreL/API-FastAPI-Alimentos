from faker import Faker
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.produto import Product
from app.models.company import Company

fake = Faker("pt_BR")


def seed_products(n=10):
    session: Session = next(get_session())

    unidades = ["kg", "l", "un", "m²"]
    metodos = ["refrigerado", "congelado", "ambiente"]
    status_list = ["ativo", "inativo"]

    company = session.exec(Company).first()

    if not company:
        print("❌ Nenhuma empresa encontrada! Rode o seed_db primeiro.")
        return

    for _ in range(n):
        product = Product(
            nome=fake.word().capitalize(),
            descricao=fake.sentence(),
            unidade_medida=fake.random_element(unidades),
            metodo_conservacao=fake.random_element(metodos),
            status=fake.random_element(status_list),
            company_id=company.id,
        )
        session.add(product)

    session.commit()
    print(f"✅ {n} produtos criados com sucesso!")


if __name__ == "__main__":
    seed_products(n=20)
