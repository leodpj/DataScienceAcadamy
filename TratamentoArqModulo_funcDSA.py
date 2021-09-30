

# LENDO ARQUIVOS
arq1 = open("arquivos/arquivo1.txt", "r")
print(arq1.read())
print(arq1.tell())
print(arq1.seek(0,0))
print(arq1.read(10))

# GRAVANDO ARQUIVOS

arq2 = open("arquivos/arquivo1.txt", "w")

arq2.write("Testando gravação de arquivos em Python")
arq2.close()

# LENDO NOVAMENTE PARA VERIFICAR A ALTERAÇÃO
arq2 = open("arquivos/arquivo1.txt", "r")
print(arq2.read())

#ACRESCENTANDO INFORMAÇÃO
arq2 =open("arquivos/arquivo1.txt", "a")
arq2.write(" Acrencentando conteúdo")
print(arq2.tell())
arq2.close()

# LENDO NOVAMENTE PARA VERIFICAR A ALTERAÇÃO
arq2 = open("arquivos/arquivo1.txt", "r")
print(arq2.seek(0,0))
print(arq2.read())

##================================================================================

#AUTOMATIZAR PROCESSO DE GRAVAÇÃO

fileName = input("Digite o nome do arquivo: ")
fileName = fileName + ".txt"

corpo = input("Digite para o corpo do arquivo: ")
arq3 = open(fileName, "w")

arq3.write(corpo)
arq3.close()

arq3 = open(fileName, "r")
print(arq3.read())
arq3.close()


# DIVISÃO POR LINHA

f =  open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
print(rows)



# DIVISÃO POR COLUNA
f =  open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)


# CONTANDO AS LINHAS

f =  open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0
for row in full_data:
    count += 1

print(count)

# CONTANDO NUMEROS DE COLUNAS

f =  open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0

for column in first_row:
    count = count + 1

print(count)






























