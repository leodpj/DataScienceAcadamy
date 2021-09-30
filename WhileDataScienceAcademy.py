"""counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

x = 0
while x < 10:
    print("O valor de x nessa interação é:", x)
    print(" X ainda é menor que 10. somando 1 a x")
    x += 1
else:
    print("Loop concluido!")

num = int(input("Insira uma valor: "))

counter = 0
while counter < 100:
    if counter == num:
        break
    else:
        pass
    print(counter)
    counter = counter + 1


#o continuei pegas a letra
for verificador in "leonardo":
    if verificador == "a":
        continue
    if verificador == "e":
        continue
    if verificador == "i":
        continue
    if verificador == "o":
        continue
    print(verificador)

"""

#NUMEROS PRIMOS
for i in range(2, 30):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j = j + 1
        else:
            j = j + 1
    if counter == 0:
        print(str(i) + "é um numero primo")
        counter = 0
    else: counter = 0

