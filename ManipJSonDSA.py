#CRIANDO UM DICIONARIO
import json

dict = {'nome': "Guido van rossum",
        'linguagem': 'Python',
        'similar': ['c', 'Modula-3', 'lisp'],
        'users': 1000000}

for k,v in dict.items():
        print(k,v)

print(json.dumps(dict))

with  open('arquivos/dados.json', 'w') as arquivo:
        arquivo.write(json.dumps(dict))


with  open('arquivos/dados.json', 'r') as arquivo:
        texto = arquivo.read()
        data = json.loads(texto)

print(data)
print(data['nome'])

from urllib.request import urlopen

response = urlopen("https://vimeo.com/138768424").read().decode('utf8')
data = json.loads(response)[0]


