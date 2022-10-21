# Fizz Buzz
# por si lo quieren resolver por su cuenta otra vez
# https://leetcode.com/problems/fizz-buzz/

# Hacer una función, hace n iteraciones
# Imprima esos números
# Los números que sean divisibles entre 3 Fizz
# Los números que sean divisibles entre 5 Buzz
# Los números que sean divisibles entre 15 FizzBuzz
# 1 2 Fizz 4 Buzz


def FizzBuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print('FizzBuzz', end=' ')
            continue
        if i % 3 == 0:
            print('Fizz', end=' ')
            continue
        if i % 5 == 0:
            print('Buzz', end=' ')
            continue
        print(i, end=' ')
        
FizzBuzz(100)