# Recursos para repasar:
# función zip() para iterar a través de varios objetos iterables al mismo tiempo
# https://realpython.com/python-zip-function/
# https://www.w3schools.com/python/ref_func_zip.asp

# Definir una función en python
# https://www.w3schools.com/python/python_functions.asp
# Este recurso tiene algunas cosas extras como los *args y los **kwargs que veremos 
# mas adelante pero lo pueden revisar si gustan

# Definir Clases, darles atributos y métodos; generar objetos a partir de esas clases.
# https://www.w3schools.com/python/python_classes.asp
# https://www.geeksforgeeks.org/python-classes-and-objects/
# https://docs.python.org/3/tutorial/classes.html Este último link es la documentación 
# oficial de python, esta siempre será el mejor recurso a revisar pero también puede ser 
# muy tardado leerla ya que tiene mucha información al detalle

lista = ['Dani', 'Diego', 'Johann', 'Roberto', 'Armando']
lista2 = [21, 19, 21, 21]
lista3 = ['Geminis', 'Leo', 'Tauro']

# Puede dar error de indice
# for i in range(len(lista)):
#     print(lista[i], lista2[i])


# for a in zip(lista, lista2, lista3):
    # print(a[0], a[1], a[2])


def Suma(x, y):
    z = []
    z.append(x+y)
    z.append(x*y)
    z.append(x**y)
    return z


# resultado = Suma(5, 10)
# print(resultado)

# print(Suma(5,10))
# print(type(Suma(5,10)))
# print(Suma(5.5,10.3))
# print(type(Suma(5.5,10.3)))



# OOP

class UsuarioPrimario:
    edad = 18
    nombre = 'Juan'
    nacionalidad = 'Mexicano'
    
    def Saludo(self):
        print('Hola, mi nombre es ', self.nombre)

user1 = UsuarioPrimario()

# print(user1.edad)
# print(user1.nombre)
# print(user1.nacionalidad)
# print(user1.Saludo())

class User:
    def __init__(self, nombre, edad, nationality):
        self.name = nombre
        self.age = edad
        self.nat = nationality
    
    def Hello(self):
        # print('Hi, my name is', self.name, ' and I am ', self.age, ' years old')
        print(f'Hi, my name is {self.name} and I am {self.age} years old')
    
user2 = User('Juan', '21', 'mxn')
user3 = User('Franchesco', '30', 'Italiano')
print(user2.Hello())
print(user3.Hello())