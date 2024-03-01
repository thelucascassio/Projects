#2. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o primeiro nome da pessoa.
nome = input("Digite seu nome completo: ")
chamar = nome.split()
print("Bem vindo ao Python,", chamar[0])