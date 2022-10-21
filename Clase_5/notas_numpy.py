import numpy as np
import pandas as pd

# import random as rnd
# aleatorios = []
# for _ in range(100):
#     aleatorios.append(rnd.randint(1,3))
# print(aleatorios)

# import math
# elevados = []
# for element in aleatorios:
#     elevados.append(math.exp(element))
# print(elevados)

ale = np.random.randint(1,5,100)

print(ale)

power = np.exp(ale)

seno = np.sin(ale)

hiperbolic_tangent = np.tanh(ale)

print(power)
