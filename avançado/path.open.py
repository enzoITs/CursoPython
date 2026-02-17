from pathlib import Path
from  datetime import datetime
# arquivo = open('avançado/arquivo.txt')
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

# with open('avançado/arquivo.txt') as arquivo:
#     print(arquivo.readlines())
 
# with open('avançado/arquivo.txt', 'w', encoding='utf-8') as arquivo:
#     arquivo.write('Olá, mundo')

# with open('avançado/arquivo.txt', 'a', encoding='utf-8') as arquivo:
#     arquivo.write('Bom dia\n')

# with open('avançado/arquivo.txt', 'r+', encoding='utf-8') as arquivo:
#     arquivo.write('Olá, mundo\n')
#     arquivo.write('Texto que vem depois\n')
#     print(arquivo.read())

# -------------------exercicios
# 1

# relatorio = Path('relatorio.txt')
# agora = datetime.now()
# agora_convertido = datetime.strftime(agora, '%d/%m/%Y')

# with relatorio.open('w', encoding='utf-8') as arquivo:
#     arquivo.write('Estou aprendendo python!\n')
#     arquivo.write(agora_convertido)

# 2

# a = Path("mensagem.txt")

# with a.open("r", encoding="utf-8") as arquivo:
#     texto = arquivo.read()
#     palavras = texto.split()   # separa por espaço
#     contador = len(palavras)

# print(contador)

# 3
# registro = Path('acesso.log')

# palavra = input('digite uma palavra chave: ')

# with registro.open('r', encoding='utf=8') as arquivo:
#     linhas = arquivo.readlines()
#     for linha in linhas:
#         if palavra.lower() in linha.lower():
#             print(linha)




    