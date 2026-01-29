# 1. Banco de Dados (Sempre no topo)
lista_de_alunos = {
    "nome": ['enzo'],
    "idade": [16],
    "nota": [10]
}

# 2. Definição das Funções
def adicionar_aluno():        
    add_nome  = input('Digite o nome do aluno: ')
    add_idade = int(input('Digite a idade do aluno: '))
    add_nota = float(input('Digite a nota do aluno: '))
    
    # Validação: Só adiciona se a nota for de 0 a 10
    if add_nota < 0 or add_nota > 10:
        print('⚠️ Nota inválida! O aluno não foi adicionado. Digite de 0 a 10.')
    else:
        lista_de_alunos["nome"].append(add_nome)
        lista_de_alunos["idade"].append(add_idade)
        lista_de_alunos["nota"].append(add_nota)
        print("✅ Aluno adicionado com sucesso!")

def ver_lista():
    # Verifica se a lista não está vazia
    if not lista_de_alunos["nome"]:
        print('📂 A lista está vazia.')
    else:
        print("\n--- LISTA DE ALUNOS ---")
        for i in range(len(lista_de_alunos["nome"])):
            print(f"Nome: {lista_de_alunos['nome'][i]} | Idade: {lista_de_alunos['idade'][i]} | Nota: {lista_de_alunos['nota'][i]}")

def remover_alunos():
    nome_aluno = input('Digite o nome do aluno para remover: ')
    if nome_aluno in lista_de_alunos["nome"]:
        numA = lista_de_alunos["nome"].index(nome_aluno)
        lista_de_alunos["nome"].pop(numA)
        lista_de_alunos["idade"].pop(numA)
        lista_de_alunos["nota"].pop(numA)
        print(f"🗑️ Aluno {nome_aluno} removido.")
    else:
        print('❌ Aluno não encontrado!')

def procurar_aluno():
    nome_a = input('Digite o nome do aluno: ')
    if nome_a in lista_de_alunos["nome"]:
        idx = lista_de_alunos["nome"].index(nome_a)
        print(f"🔍 Aluno encontrado: {lista_de_alunos['nome'][idx]}, {lista_de_alunos['idade'][idx]} anos, Nota: {lista_de_alunos['nota'][idx]}")
    else:
        print('❌ Aluno não encontrado!')

def media_notas():
    notas = lista_de_alunos["nota"]
    if notas:
        media = sum(notas) / len(notas)
        print(f'📊 A média de todos os alunos é {media:.2f}')
    else:
        print("Não há notas cadastradas.")

# 3. Menu Interativo (Onde o programa "começa" de fato)
while True:
    print("\n" + "-"*30)
    print("      SISTEMA DE ALUNOS")
    print("-"*30)
    print("[1] Adicionar Aluno")
    print("[2] Ver Lista Completa")
    print("[3] Pesquisar por Aluno")
    print("[4] Remover Aluno")
    print("[5] Mostrar a Média das Notas")
    print("[0] Sair")
    
    try:
        opcao = int(input("\nDigite a sua opção: "))
        
        if opcao == 1:
            adicionar_aluno()
        elif opcao == 2:
            ver_lista()
        elif opcao == 3:
            procurar_aluno()
        elif opcao == 4:
            remover_alunos()
        elif opcao == 5:
            media_notas()
        elif opcao == 0:
            print("Encerrando... Até logo!")
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Erro: Por favor, digite apenas números.")

print(aaaaa)