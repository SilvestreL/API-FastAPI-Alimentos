from faker import Faker
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.etiqueta import Etiqueta
from app.models.produto import Product
from app.models.company import Company

fake = Faker("pt_BR")


def seed_etiquetas(n=20):
    session: Session = next(get_session())

    # Verifica se existe pelo menos uma empresa
    company = session.exec(Company).first()
    if not company:
        print("❌ Nenhuma empresa encontrada! Rode o seed_db primeiro.")
        return

    produtos = session.exec(Product).all()
    if not produtos:
        print("❌ Nenhum produto encontrado! Rode o seed_products primeiro.")
        return

    for _ in range(n):
        produto = fake.random_element(produtos)
        etiqueta = Etiqueta(
            produto_id=produto.id,
            quantidade=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
            unidade_medida=produto.unidade_medida,
            data_producao=fake.date_between(start_date="-30d", end_date="today"),
            data_validade=fake.date_between(start_date="today", end_date="+30d"),
            metodo_conservacao=produto.metodo_conservacao,
            status=produto.status,
            company_id=company.id,
        )
        session.add(etiqueta)

    session.commit()
    print(f"✅ {n} etiquetas criadas com sucesso!")


if __name__ == "__main__":
    seed_etiquetas(n=20)
