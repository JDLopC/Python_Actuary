### TIPOS DE ESTRUCTURAS DE DATOS DEFAULT EN PYTHON

# Lists, tuples, dictionaries, sets, ranges

# list []

colores:list = ['red', 'brown', 'blue', 'purple']

# colores[0] = 'Red'
# print(colores)

# colores[1] = ['brown1', 'brown2']
# print(colores)

# print(colores)
# print(type(colores))
# print(colores[1])
# print(type(colores[1]))
# print(colores[0][2])
# print(colores[0].upper())

# Métodos para nuestras listas

# print(colores)
# colores.append('black')
# print(colores)
# colores.pop()
# colores.pop()
# print(colores)

# objetos = ['Cano', 21, 'Calistenia']
# print(objetos)
# print(type(objetos[0]))
# print(type(objetos[1]))
# print(type(objetos[2]))

gustos = [
    ['Cano', 21, 'Calistenia'],
    ['Dani', 21, 'Futbol']
]
# gustos.append(['Cano', 21, 'Calistenia'])
# gustos.append(['Dani', 21, 'Futbol'])
gustos.append(['Vicepresi', 19, 'Programar'])
gustos.append(['Angy', 21, 'Bailar'])

gustos[0][2] = 'Calistenia x2'


# print(gustos)
# print(gustos[0], '\n')
# print(gustos[0][2])

# tuple ()
# Las tuplas también son indexadas
# Las tuplas no son modificables

comida:tuple = ('crangreburger', 'ensalada', 'pechuga de pollo')

# print(comida)
# print(type(comida))

# comida[0] = 'Burger' # No se puede realizar, manda error

# dict {:}

cumple = {
    'Cano': 2000,
    'Karen': 2001,
    'Fer': 2002
}

#print(cumple['Kare']) # Esto genera error de tipo de llave

# print(cumple.get('Fernanda'))
# Cuando no escribimos bien 
# la llave, nos regresa un dato tipo None

# Agregar elementos al diccionario

cumple.update({
    'Armando': 2003,
    'Kevin': 2000
})

cumple.update({
    2000: ['Cano', 'Kevin']
})


# print(cumple.get(2000))
# print(cumple.get('Kevin'))

# set conjunto {1, 2, 3, 4, 1}
# No tiene indice
# No permite datos repetidos
# No tiene orden

equipos = {'Paris', 'Manches', 'Barca', 'Madrid', 'Barca'}

equipos.add('Bayern')
equipos.add('Paris')
# print(equipos)

# print('green' in colores)
# print('green' not in colores)

# print('Paris' in equipos)

e_eliminados = {'Paris'}

# e_restantes = equipos - e_eliminados

# print('Madrid' not in (equipos - e_eliminados))


