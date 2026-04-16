from models import Session
from models import Usuario

def excluir_usuario(usuario_id):
    db = Session()

    usuario =  db.query(Usuario).filter(Usuario.id == usuario_id ).first()

    if usuario:
        db.delete(usuario)
        db.commit()
        print(f"Usuário com id {usuario_id} foi excluido,")
    else:
        print(f"Usuário com id {usuario_id} não encontrado.")

    return usuario
    
excluir_usuario(2)