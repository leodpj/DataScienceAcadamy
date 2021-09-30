import csv

with open("arquivos/numeros.csv", "w") as arquivo:
    writer =csv.writer(arquivo)
    writer.writerow(('primeira', 'segunda', 'terceira'))
    writer.writerow((55,93,76))
    writer.writerow((62,14,86))


with open("arquivos/numeros.csv", 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print('Números de colunas:', len(x))
        print(x)


# GERANDO UMA LISTA COM DADOS CSV

with open("arquivos/numeros.csv", 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

for linha in dados[1:]:
    print(linha)



