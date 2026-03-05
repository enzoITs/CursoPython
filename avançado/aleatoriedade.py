import random

# inteiro_aleatorio = random.randint(1, 1000)

# float_aleatorio = random.uniform(1, 20)

# cartas = ['As', 'Rei', 'Rainha', 'Valete']
# carta_aleatoria = random.choice(cartas)

# cartas = ['As', 'Rei', 'Rainha', 'Valete']
# carta_aleatoria = random.choices(cartas, k=2)

# cartas = ['As', 'Rei', 'Rainha', 'Valete']
# carta_aleatoria = random.sample(cartas, k=2)

# ------------------------------exercicios

convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]

premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

pessoa_sorteada = random.sample(convidados, k=5)
premio_sorteado = random.sample(premios, k=5)

i = 0
while i < 5:
    convidado = pessoa_sorteada[i]
    premio = premio_sorteado[i]
    print(f'{convidado} ganhou {premio}')
    i+=1