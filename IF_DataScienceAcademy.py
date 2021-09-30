"""idade = 12
nome = "Bob"
if idade >= 13 or nome =="Bob":
    print("Ok Bob, você está autorizado a entrar!")

dia = "Terça"
if dia == "Segunda":
    print("Hoje fará sol!")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado")

idade = 18
nome = "Bob"
if idade > 17 and nome == "Bob":
    print("Autorizado!")


disciplina = input('Digite o nome da disciplina: ')
nota_final = input("Digite nota final (entre 0 e 100): ")

if disciplina == "Geografia" and nota_final >= "70":
    print("Você foi Aprovado!")
else:
    print("Lamento, acho que você precisa estudar mais!")
"""

disciplina = input('Digite o nome da disciplina: ')
nota_final = input("Digite nota final (entre 0 e 100): ")
semestre = input("Digite o semestre (1 a 4): ")

if disciplina == "Geografia" and nota_final >= "50" and int(semestre) !=1:
    print("Você foi Aprovado em %s com média final %r!" %(disciplina, nota_final))
    print("Você foi Aprovado em {} com média final {}!".format (disciplina, nota_final))
else:
    print("Lamento, acho que você precisa estudar mais!")

