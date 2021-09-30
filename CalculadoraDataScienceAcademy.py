
operacao = str(input(""" Qual operacão voce gostaria de realizar
         1 - Somar
         2 - Subtração
         3 - Multiplicação
         4 - Divição

Digite uma opção (1/2/3/4): """))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operacao == "1":
    print("{} + {} = {} ".format(num1, num2, num1 + num2))
elif operacao == "2":
    print("{} - {} = {} ".format(num1, num2, num1 - num2))
elif operacao == "3":
    print("{} * {} = {} ".format(num1, num2, num1 * num2))
elif operacao == "4":
    print("{} / {} = {} ".format(num1, num2, num1 / num2))
else:
    print("A opção invalida")
