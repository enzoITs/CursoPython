# pessoa = {
#     'nome':'Enzo',
#     'idade': 16,
#     'cidade':'Marilia',
#     'profissoes':['la1', 'sla2', 'sal3']
# }

# print(pessoa)
# print(pessoa['cidade'])
# print(pessoa['idade'])
# print(pessoa['nome'])

# pessoa['idade'] = 30
# del pessoa['cidade']

# print(pessoa)
# print(pessoa['profissoes'][1])

# print(pessoa.keys())
# print(pessoa.values())

# valores = list(pessoa.values())
# print(valores[2])

# print(pessoa.items())

# print(pessoa.get('macaco', 'nao tem')

# pessoa.pop('idade')
# print(pessoa)

# exerciciso 

# livro = {
#     'titulo',
#     'autor',
#     'ano'
# }

# print(livro['titulo'])
# print(livro['autor'])
# print(livro['ano


# -0-------0-0-0-0-0-0-0--0-0-0-0-0-0-0-0

# usuarios = {
#     'nome': input('Digite seu nome: '),
#     'idade': int(input('digite sua idade: '))
# }

# if usuarios['idade'] >= 18:
#     print(f'Acesso liberado para {usuarios["nome"]}')
# else:
#     print(f'Acesso negado para {usuarios["nome"]}')

# -0-0-0-0-0-0-0-0-0-0-0-

contas = {
    'usuario': 'admin',
    'senha': '123'
}

entradas = {
    'usuario': input('Digite o usuario: '),
    'senha': input("Digite a senha: ")
}

if contas['usuario'] == entradas['usuario'] and contas['senha'] == entradas['senha']:
    print("Login bem-sucedido")
else:  
    print("Usuário ou senha incorretos")

