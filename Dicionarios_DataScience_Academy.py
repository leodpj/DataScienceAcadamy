estudantes_lst = ["Matheus", 24, "Fernanda", 22, "Ana", 26, "Cristiano", 25]
print(estudantes_lst)
estudantes_dic = {"Matheus":24, "Fernanda":22, "Ana":26, "Cristiano":25}

print(estudantes_dic["Matheus"])
estudantes_dic["Leo"] = 44
print(estudantes_dic["Leo"])
print(estudantes_dic)

estudantes = {"Matheus":24, "Fernanda":22, "Ana":26, "Cristiano":25}
print(estudantes)
print(len(estudantes))
print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

estudantes2 = {"Maria":27, "Erika":28, "Milton":28}
print(estudantes2)
estudantes.update(estudantes2)
print(estudantes)


dic1 = {}
dic1["Key_one"] = 2
print(dic1)

dic1[10] = 5
print(dic1)

dic1[8.2] = "python"
print(dic1)

dict1 = {}
dict1["teste"] = 10
dict1["key"] = "teste"
print(dict1)


dict2 = {}
dict2["key1"] = "Big Data"
dict2["key2"] = 10
dict2["key3"] = 5.6
print(dict2)

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]

print(a, b, c)


dict3 = {'key1':1230, 'key2':[22,453,73.4], 'key3':['leite', 'maça', 'batata']}
print(dict3)
print(dict3["key2"])
print(dict3["key3"][0].upper())


var1  = dict3["key2"][0] - 2
print(var1)

dict3['key2'][0] -= 2
print(dict3)




dict_aninhado = {"key1":{"key2_aninhada":{"key3_aninhada":"Dict_aninhada em Python"}}}

print(dict_aninhado)
print(dict_aninhado["key1"]["key2_aninhada"]["key3_aninhada"])












































