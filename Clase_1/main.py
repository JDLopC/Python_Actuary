# ### TIPOS DE VARIABELS PARA PYTHON (Datos) https://www.w3schools.com/python/python_datatypes.asp
# Link para revisar todos los operadores lógicos de python https://www.w3schools.com/python/python_operators.asp


# # Strings, integers, floats, boolean, none, complex

# str


my_var = 'Daniel es el profesor de el taller'

var2 = 'abcdefghi'
# String slicing

print(my_var[0:7])

print(var2[-1])


## String formating

edad = 20

# Link para revisar las "f strings" https://www.freecodecamp.org/espanol/news/tutorial-de-f-strings-en-python-formato-de-cadenas-en-python-explicado-con-ejemplos/


# F string, nos permite incluir variables numericas en nuestros string
print(f'Fer tiene {edad} años')
print('Fer tiene 19 años')

# int

entero = 19

print(type(entero))

entero = '19'

print(type(entero))


# Math operators

suma = 5 + 4 # 9

resta = 7 - 1 # 6

div = 10 / 2 # 5

mult = 2*3 # 6

exp = 2**2 # 4

divfloor = 10 // 2

div2 = 18 / 5
divfloor2 = 18 // 5

modulo = 10 % 2
modulo = 15 % 2
print(modulo)

print(div2, divfloor2)

print(suma, resta, div, mult, exp, divfloor)

# float

flotante = 5.5

print(type(flotante))

# bool

booleano = True
booleano2 = False

print(type(booleano))
print(type(booleano2))


## Logical and comparison operators

print(5 > 6)
print(5 <= 6)
print('a' == 'b')
print('a' == 'a')
print('a' == 'A')

print((8 % 2) == 0)
print((15 % 2) == 0)

print(5 != 7)
print(5 != 5)












































colors = ['red', 'green', 'blue', 'purple', 'brown', 'white', 'black', 'blue']