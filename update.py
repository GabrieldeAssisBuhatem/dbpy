from models import Session
from models import Usuario
import os
print(os.path.abspath("meubanco.db"))


def atualizar_usuario(usuario_id, novo_nome, novo_email, nova_senha):
   
    db = Session()  # Criar uma única sessão para todas as operações

    try:
        # Buscar o usuário pelo ID
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuario:
            usuario.nome = novo_nome  # Atualizar o nome
            print(f"Nome do usuário atualizado para: {usuario.nome}")
        else:
            print(f"Usuário com ID {usuario_id} não encontrado.")
            return  # Se o usuário não for encontrado, sai da função

        # Atualizar o email se ambos os parâmetros forem fornecidos
        if novo_email:  # Verifica se ambos foram passados
            usuario.email = novo_email  # Atualiza o email do usuário
            print(f"E-mail atualizado para: {usuario.email}")
        else:
            print(f"Faltou digitar e-mail.")

        # Atualizar a senha se ambos os parâmetros forem fornecidos
        if nova_senha:  # Verifica se ambos foram passados
            usuario.senha = nova_senha  # Usando o nome correto da coluna
            print("Senha atualizada.")
        else:
            print(f"Senha não digitada.")

        # 🔥 IMPORTANTE: Confirmar as mudanças no banco de dados
        db.commit()
    
    except Exception as e:
        db.rollback()  # Se der erro, desfaz as mudanças
        print(f"Erro ao atualizar: {e}")

    finally:
        db.close()  # Fechar a conexão

# Atualizar o nome do usuário com ID 1 e o email e senha dele
atualizar_usuario(usuario_id=1, novo_nome="mestre chico",novo_email="amantedelinux@gmail.com",nova_senha="54321")

# Atualizar o nome do usuário com ID 2, mas agora passando os IDs corretamente
atualizar_usuario(usuario_id=2, novo_nome="Maria Atualizada",novo_email="aaaaa@gmail.com",nova_senha="novaSenha456")    

