import math
import random

# print(math.sqrt(49))
# print(math.ceil(3.123123123123))

# numero_aleatorio = random.randint(1, 10)
# print(numero_aleatorio)

# ------------Exercicios

num_aleat = random.randint(1, 20)

while True:
    escolha = int(input('Tente acertar um numero de 1 a 20!: ')) 
    if escolha > num_aleat:
        print('Muito alto')
    elif escolha < num_aleat:
        print('Muito baixo')
    elif escolha == num_aleat:
        print('Acertou!!!!')
        break