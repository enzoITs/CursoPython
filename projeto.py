lista_de_alunos = {
    "nome": ['enzo'],
    "idade": [16],
    "nota": [10]
}

def adicionar_aluno():        
    add_nome  = input('Digite o nome do aluno: ')
    add_idade = int(input('Digite a idade do aluno: '))
    add_nota = int(input('Digite a nota do aluno: '))
    lista_de_alunos["nome"].append(add_nome)
    lista_de_alunos["idade"].append(add_idade)
    lista_de_alunos["nota"].append(add_nota)
    if add_nota > 10 and add_nota < 0:
        print('Nota invalida, Digite uma nota de 0 a 10')

def ver_lista():
    print(lista_de_alunos)
    if lista_de_alunos["nome"] == "":
        print('Lista Vazia')

def remover_alunos():
    nome_aluno = input('Digite o nome do aluno')
    if nome_aluno in lista_de_alunos["nome"]:
        numA = lista_de_alunos["nome"].index(nome_aluno)
        lista_de_alunos["nome"].pop(numA)
        lista_de_alunos["idade"].pop(numA)
        lista_de_alunos["nota"].pop(numA)
    else:
        print('Aluno, nao encontrado!')

def procurar_aluno():
    nome_a = input('Digite o nome do aluno: ')
    if nome_a in lista_de_alunos["nome"]:
        numB = lista_de_alunos["nome"].index(nome_a)
        print(lista_de_alunos["nome"][numB])
        print(lista_de_alunos["idade"][numB])
        print(lista_de_alunos["nota"][numB])
    else:
        print('Aluno, nao encontrado!')
adicionar_aluno()
remover_alunos()
print(lista_de_alunos)
