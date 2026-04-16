from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados (usando SQLite)
DATABASE_URL = "sqlite:///meubanco.db"

# Criar a engine e a sessão
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
db = SessionLocal()