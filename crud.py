from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import models
from database import SessionLocal
from models import Usuario
bd = SessionLocal()

def create_user(bd: Session, name, email, senha):
    db_user = models.Usuario(nome=name, email=email, senha=senha)
    bd.add(db_user)
    bd.commit()
    bd.refresh(db_user)
    return db_user
    
def read_user(bd: Session,user_id: int):
    return bd.query(models.Usuario).filter(models.Usuario.id == user_id).first()

def update_user(bd: Session, user_id: int,name,email,senha):
    db_user = bd.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if db_user:
        db_user.nome = name
        db_user.email = email
        db_user.senha = senha
        bd.commit()
        bd.refresh(db_user)
        print("😁informações do Usuario Atualizadas com sucesso!!👍")
        return db_user
    
def delete_user(bd: Session, user_id: int):
    db_user = bd.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if db_user:
        bd.delete(db_user)
        bd.commit()
        print("😒Usuario Deletado Com Sucesso!!")
        return db_user
    
def lista_user(bd: Session):
    return bd.query(models.Usuario).all()

def adicionar_usuario(bd: Session, name: str, email:str, senha: str):
    try:
        print("🔍 Verificando se este email já existe no banco...")
        usuario_existente = bd.query(models.Usuario).filter_by(email=email).first()
        
        if usuario_existente:
            print("⚠️ Um usuário com este email já existe.")
        else:
            novo_usuario = models.Usuario(nome=name, email=email, senha=senha)
            bd.add(novo_usuario)
            bd.commit()
            bd.refresh(novo_usuario)
            print("✅ Usuário adicionado com sucesso!")
            return novo_usuario
    except SQLAlchemyError as e:
        bd.rollback()
        print("❌ Erro ao adicionar usuário:", e)

def esqueci_senha(db: Session):
    print("🔐 Recuperação de senha")

    email = input("Digite o seu e-mail cadastrado: ").strip()
    usuario = db.query(Usuario).filter_by(email=email).first()

    if usuario:
        nova_senha = input("Digite sua nova senha: ").strip()
        confirmar = input("Confirme sua nova senha: ").strip()

        if nova_senha == confirmar:
            usuario.senha = nova_senha
            db.commit()
            print("✅ Senha redefinida com sucesso!")
        else:
            print("❌ As senhas não coincidem. Tente novamente.")
            esqueci_senha(db)
    else:
        print("❌ E-mail não encontrado no sistema.")



    
    
