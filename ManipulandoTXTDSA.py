import os
# MANIPULANDO TXT

texto = "Cientista de Dados é a profissão que mais tem crescido em todo o mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatísca e Machine Learning.\n"
texto += "E claro, em Big Data."

print(texto)

arquivo = open(os.path.join("arquivos/cientista.txt"), "w")

for palavra in texto.split():
    arquivo.write(palavra+" ")

arquivo.close()

arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)


#  EXPRESSÃO WITH

with open('arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)



with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])


arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)



