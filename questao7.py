usuarios = []

while True:
 opcao = input("Deseja cadastrar um novo usuário? (s/n) ")

 if opcao == "n":
     break

 elif opcao == "s":
     nome = input("Digite o nome do usuário: ")
     idade = input("Digite a idade do usuário: ")
     email = input("Digite o e-mail do usuário: ")
     usuario = {"nome": nome, "idade": idade, "email": email}

     usuarios.append(usuario)

 else:
     print("Opção inválida, tente novamente.")

print("\nUsuários cadastrados:")

for usuario in usuarios:
 print(f"\n- Nome: {usuario['nome']}\n- Idade: {usuario['idade']}\n- E-mail: {usuario['email']}")