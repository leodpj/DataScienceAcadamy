"""
def primeiraFunc():
    print("Hello World")

primeiraFunc()

def segundaFunc(none):
    print("Hello %s" %(none))

segundaFunc("Aluno")

def funcLeitura():
    for i in range(0,5):
        print("Numero" + str(i))

funcLeitura()



num = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero: "))

def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: " , firstnum + secondnum)

addNum(num, num2)



# VARIAVEIS LOCAIS E GLOBAIS
var_global = 10

def multiply(num1, num2):
    var_global = num1 * num2
    print(var_global)

multiply(5, 25)

print(var_global)


var_global = 10
def multiply(num1, num2):
    var_local = num1 * num2
    print(var_local)

multiply(5, 25)

print(var_local)


## FUNCOES BUILT-IN

print(abs(-56))
print(abs(23))
print(bool(0))
print(bool(1))


## FUNCOES STR, INT, FLOAT

idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Voce pode acessar o Facebook")

print(int("26"))
print(float("123.345"))
print(str(14))
print(len([23,34,45,46]))
array = ["a", "b", "c"]
print(max(array))
print(min(array))
array = ["a", "b", "c", "d", "A", "B", "C", "D"]
print(max(array))
print(min(array))
print(array)

lista = [23, 23, 34, 45]

lista2 = [10, 5, 8]

lista_total = lista + lista2
print(lista_total)
print(sum(lista_total))


import math

def numPrimo(num):
    # VERIFICAR SE UM NUMERO É PRIMO.
    if (num % 2) == 0 and num > 2:
        return "Este número é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
        return "Este número é primo"


print(numPrimo(541))

def split_string(text):
    return text.split(" ")
texto = "Essa função será bastante útil para separar grandes volumes de dados."

print(split_string(texto))

# COLOCANDO O TEXTO DENTRO DE UMA VARIAVEL
token = split_string(texto)
print(token)

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_strng = lowercase(caixa_baixa)
print(lowercased_strng)
"""

def printVarInfo( arq1, *vartuple ):
    print("O parâmetro passado foi: ", arq1)
    for item in vartuple:
        print("O parâmentro passado foi: ", item)
    return;

printVarInfo(10)
printVarInfo("Chocolate", "Morango", "Banana", "Maça")



