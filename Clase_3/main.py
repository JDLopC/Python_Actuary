

a = 5

b = 4

c = 15

# if (a < b) or (a<c):
    # print('A menor que b y que c')


# if (a == b):
#     print('Los numeros son iguales')
# else:
#     print('Los numeros no son iguales')

# if (a == b):
#     print('Los numeros son iguales')
# elif (a > b):
#     print('a mayor que b')
# else:
#     print('a menor que b')
    




palabra = 'hot dog' # Objeto iterable

# for i in palabra:
#     print(i)
#     print(type(i))


lista = [21, 21.0, 19, 20, 19, 19, 19, 21, 21]

# for i in lista:
#     print(i, end=' ')
#     print(i*2)
    
import random as rnd

aleatorios = []
for i in range(100):
    aleatorios.append(rnd.randint(1, 100))
# print(aleatorios)

# list comprehension
# ale = [random.randint(1,100) for _ in range(100)]



bandera = True

numeros = [1, 3, 5, 7]

# while bandera:
#     # valor = rnd.randint(0,20)
#     valor = rnd.choice(numeros)
#     print(valor)
    
#     if valor % 2 == 0:
#         bandera = False
        
value = rnd.choice(numeros)

while value <= 8:
    print(value)
    value += 1