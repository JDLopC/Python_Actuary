import json as js

string = '''
{
    "personas": [
        {
            "nombre": "Juan Daniel",
            "numero": "733-3849-3348",
            "correos": ["juan.daniel@gmail.com", "juan.lopezco@outlook.com"],
            "tiene_licencia": false
        },
        {
            "nombre": "Maria de la Rosa",
            "numero": "338-5588-3349",
            "correos": ["maria@gmail.com", "ma.rosa@outlook.com"],
            "tiene_licencia": true
        }
    ]
}
'''

data = js.loads(string)

# print(type(data))

# print(data['personas'][0]['nombre'])
# print(data['personas'][0]['numero'])

# GENERAR STRING VALIDO TIPO JSON

diccionario = {
    'name': 'Diego',
    'novia': True,
    'name_novia': 'Mariel',
    'edad': 19
}

# x = js.dumps(diccionario, indent=2)
# print(type(diccionario))
# print(x)
# print(type(x))

lista = ['Roberto', 'Angy', 'Fernanda', 'Derek', 129, 18.5, True]

# y = js.dumps(lista, indent=2)
# print(y)

ciudades = {
    'Acapulco': ['Juan', 'Fernanda'],
    'cdmx': ['Diego', 'Mariel', 'Angy', 'Alvaro', 'Pedro']
}


with open('./nativos_por_ciudad.json', mode='w') as file:
    js.dump(ciudades, file, indent=2)