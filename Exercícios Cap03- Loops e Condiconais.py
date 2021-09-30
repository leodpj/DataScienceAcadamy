# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia = input("insira o dia da semana: ")

if dia == "sabado":
    print("Hoje é dia de descanso! ")
elif dia == "domingo":
    print("Hoje é dia de descanso e ir para igreja: ")
else:
    print("Dia de trabalhar vagabundo :) ")


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

frutas = ["morango", "uva", "maça", "caja", "banana"]

if "morango" in frutas:
    print("Morango")
else:
    print("Não existe essa fruta na lista!")


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista
tp = ("Casa", "Apartamento", "Fazenda", "Chacará")
lista = tp * 2
print(lista)


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 150, 2):
    print(i)


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela

temperatura = int(input("Insira a temperaatura: "))

if temperatura <= 0:
    print("Frio extremo, {}º vá para casa e não saiu sem necessidade ".format(temperatura))

elif temperatura >= 1 and temperatura < 10:
    print("A temperatura atual é de {}º ainda continua muito baixa use agasalho ".format(temperatura))

elif temperatura >= 10 and temperatura < 15:
    print("A temperatura atual é de {}º use agasalho ".format(temperatura))

elif temperatura >= 15 and temperatura < 25:
    print("A temperatura atual é de {}º é considerada uma temperatura agradavel".format(temperatura))

elif temperatura >= 25 and temperatura < 35:
    print("A temperatura atual é de {}º beba bastante agua é se possivel vá a praia ".format(temperatura))

else:
    print("a temperatura é de {} quase um deserto do Saara". format(temperatura))



# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

counter = 0
while counter < 100:
    print(counter)
    counter = counter + 1
    if counter == 23:
        break


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista

numeros = list()
i = 4
while (i <= 20):
    numeros.append(i)
    i = i+2
print(numeros)


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)

nums = range(5, 45, 2)
print(list(nums))



# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')



# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."

r = frase.count("r")
print("a letra "R" aparece %s na frase " %(r))













