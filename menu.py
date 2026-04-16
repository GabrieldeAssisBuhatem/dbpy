from crud import *
from database import db
condicao = "s"
while condicao == "s":

  
  print("---------------------------------------------------------------------------------------------")
  print("-----------------------------MENU DE ATUALIZAÇÃO DE USUÁRIO----------------------------------")
  print("---------------------------------------------------------------------------------------------")
  print("1 - Criar Usuario")
  print("2 - listar Usuario")
  print("3 - Atualizar todos os campos")
  print("4 - Excluir Usuario")
  print("5 - Esqueci minha senha")
  
  opcao = int(input("Digite a opção desejada:"))

  if opcao == 1:
    nome = input("Digite o nome do usuário:")
    email = input("Digite o email do usuário:")
    senha = input("Digite a senha do usuário:")
    adicionar_usuario(db,nome,email,senha)
  elif opcao == 2:
    lista = lista_user(db)
    for i in lista:
        print(i.id,i.nome,i.email)
  elif opcao == 3:
    id = int(input("digite o id do usuario:"))
    nome = input("digite o novo nome do usuario:")
    email = input("digite o novo email do usuario:")
    senha = input("digite a nova senha do usuario:")
    update_user(db,id,nome,email,senha)
    
  elif opcao == 4:
    id = int(input("digite o id do usuario:"))
    delete_user(db,id)
  
  elif opcao == 5:
    esqueci_senha(db)
    
    condicao = input("Deseja continuar? s/n:")

  print("Fim do programa")
