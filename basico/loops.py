# contador = 1
# while contador <=5:
#     print('true')
#     contador+=1

# senha = ''
# while senha != 'python':
#     senha = input(f'Digite a senha: ')

# print('Senha correta')

# for numero in range(1, 6):
#     print(numero)

# frutas = ['uva', 'melancia', 'maçã']
# for fruta in frutas:
#     print(fruta)

# exercicios 

# contador = 10
# while contador > 0:
#     print(contador)
#     contador-=1

# -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0

# numeros = []
# for i in range(1, 6):
#     numero = int(input('Digite um numero: '))
#     numeros.append(numero)

# soma = 0
# for numero in numeros:
#     soma += numero

# print(soma)

# print(soma)

# 0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

# confrinho = 0
# while True:
#     dinheiro = float(input('Digite o valor adicionado: '))
#     confrinho += dinheiro
#     if dinheiro == 0:
#         break

# print(confrinho)
                        
# -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

# contador = 0
# while contador == 0:
#     opcao = int(input(''
#     'Escolha uma das opções'
#     '[1] Pizza'
#     '[2] Hambúrguer'
#     '[3] Sair'
#     ': '))

#     if opcao == 1:
#         continue
#     elif opcao == 2:
#         continue
#     elif opcao == 3:    
#         break


pizza = 0
hambúrguer = 0

while True:
    voto = int(input("Qual sua opção: \n1.Pizza\n2.Hambúrguer\n3.Sair\n"))
    match voto:
        case 1:
            pizza += 1
        case 2:
            hambúrguer += 1
        case 3:
            break

print(f'Pizza: {pizza}\nHamburguer: {hambúrguer}')



