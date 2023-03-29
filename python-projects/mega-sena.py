import random

contador = 0
while contador <= 9:
    numeros = random.sample(range(1, 60), 6)
    contador += 1
    print(numeros)