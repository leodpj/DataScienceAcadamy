listadomercado = ["ovos, farinha, leite, maça"]
print(listadomercado[0])

listadomercado2 = ["ovos", "farinha", "leite", "maça"]
print(listadomercado2[0])

lista3 = [12, 100, "universidade"]

item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]

print(item1)
print(item2)
print(item3)

listadomercado2[2] = "chocolate"
print(listadomercado2)

del listadomercado2[2]
print(listadomercado2)

listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
print(listas)

a = listas[0]
print(a)

b = a[0]
print(b)

lista1 = listas[1]
print(lista1)

valor_1_0 = lista1[0]
print(valor_1_0)

valor_1_2 = lista1[2]
print(valor_1_2)

lista2 = listas[2]
print(lista2)

valor_2_0 = lista2[0]
print(valor_2_0)

a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10

e = d * listas[2][0]
print(e)

lista_s1 = [34, 32, 56]
lista_s2 = [21, 90,51]

lista_total = lista_s1 + lista_s2
print(lista_total)


#OPERACAO IN

lista_test_op = [100, 2, -5, 3.4]
print(10 in lista_test_op)
print(100 in lista_test_op)
print(len(lista_test_op))
print(max(lista_test_op))
print(min(lista_test_op))

listadomercado2 = ["ovos", "farinha", "leite", "maça"]
listadomercado2.append("carne")
print(listadomercado2)
listadomercado2.append("carne")
print(listadomercado2)
print(listadomercado2.count("carne"))

a = []
print(a)
print(type(a))
a.append(10)
print(a)
a.append(50)
print(a)

old_list = [1, 2, 5, 10]
new_list = []

for item in old_list:
    new_list.append(item)
print(new_list)

c = [20, 30]
c.append(60)
c.append(70)
print(c)
print(c.count(20))


cidades = ["Porto Velho" , "Manaus", "Rio Branco", "Campo Grande", "Macapá", "Brasília", "Boa Vista", "Cuiabá", "Palmas", "São Paulo" ,"Teresina", "Rio de Janeiro", "Belém", "Goiânia", "Salvador", "Florianópolis", "São Luís", "Maceió", "Porto Alegre", "Curitiba", "Belo Horizonte", "Fortaleza", "Recife", "João Pessoa", "Aracaju", "Natal", "Vitória"]
#cidades.extend(['Fortaleza','Palmas'])
#print(cidades)
#print(cidades.index('Salvador'))
#cidades.insert(2, "Aracaju")
#print(cidades)
#cidades.remove("Aracaju")
#print(cidades)
#cidades.reverse()
#print(cidades)
cidades.sort()
print(cidades)
cidades.reverse()
print(cidades)






















































