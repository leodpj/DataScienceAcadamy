s = "Data Science Academy"
print(s)
print(s[::-1])
print(s[-5])
s = s + " A maior torcida do Nordeste"
print(s)
letra = "w"
print("O endereco {} o que significa?" .format(letra * 3))
print(s.split())
print(s.upper())
print(s.lower())

s = "seja bem vindo ao universo de python"

#COLOCAR PRIMEIRA EM MAIUSCULA
print(s.capitalize())
# CONTAR O OBJETO
print(s.count("e"))
#PROCURAR A POSIÇÃO DO OBJETO
print(s.find("p"))
#VERIFICAR SE É ESPAÇO
print(s.islower())
#VERIFICAR SE TERMINA COM A LETRA "O"
print(s.endswith("o"))


print("python " == "R")

print("python " == "python")