elementos = []

# Originalmente input guarda las respuestas como string
# x = input('Que te gusta comer? ')

# y = int(input('Edad: '))

# elementos.append(x)
# elementos.append(y)

# print(elementos)



# COMO ABRIR ARCHIVOS
# Read mode
file = open("./comidas.txt", mode='r')
# Leer el archivo complett
# print(file.read())

# Leer linea por linea
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# Leer todas las lineas
# print(file.readlines())
file.close()

# WRITE MODE
with open('./deportes.txt', mode='w') as file:
    deportes = []
    for i in range(3):
        deportes.append(input(f'Dime el deporte {i+1}: '))
    
    file.writelines(f'{deportes[0]}\n')
    file.writelines(f'{deportes[1]}\n')
    file.writelines(f'{deportes[2]}\n')