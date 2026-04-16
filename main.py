from database import engine
from models import Base

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
