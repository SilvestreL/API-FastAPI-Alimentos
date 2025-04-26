import subprocess
import os
import argparse

# Define o diretório raiz do projeto
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def run(cmd):
    env = os.environ.copy()
    env["PYTHONPATH"] = PROJECT_DIR
    subprocess.run(cmd, shell=True, check=True, cwd=PROJECT_DIR, env=env)


def reset_database():
    print("\n✨ Resetando o banco de dados...\n")
    run(
        'docker exec -i postgres_fastapi psql -U postgres -d postgres -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"'
    )


def create_tables():
    print("\n✨ Criando tabelas...\n")
    run("python -m app.scripts.create_tables")


def seed_db():
    print("\n✨ Populando Admin + Empresa...\n")
    run("python -m app.scripts.seeds.seed_db")


def seed_products(n):
    print(f"\n✨ Populando {n} Produtos...\n")
    run(f"python -m app.scripts.seeds.seed_products {n}")


def seed_etiquetas(n):
    print(f"\n✨ Populando {n} Etiquetas...\n")
    run(f"python -m app.scripts.seeds.seed_etiquetas {n}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--products", type=int, default=20)
    parser.add_argument("--etiquetas", type=int, default=20)
    args = parser.parse_args()

    print("\n🚀 Iniciando reset completo do banco de dados...\n")

    reset_database()
    create_tables()
    seed_db()
    seed_products(args.products)
    seed_etiquetas(args.etiquetas)

    print("\n✅ Reset e população concluídos com sucesso!\n")


if __name__ == "__main__":
    main()
