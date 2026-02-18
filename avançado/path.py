from pathlib import Path

# caminho = Path(r"teste.txt")
# caminho_absoluto = path(r"C:\Users\mitob\Documents\Obsidian")
# caminho_absoluto = caminho.absolute()
# print(caminho)

# caminho = Path("teste.txt")
# if caminho.exists():
#     print("existe")
# else:
#     print("nao")    

# if caminho.is_file():
#     print('é arquivo')
# elif caminho.is_dir():
#     print("é pasta")
# else:
#     print('deu ruim')

# nova_pasta = Path("NovaPasta/outra/eoutra")
# nova_pasta.mkdir(exist_ok=True, parents=True)

# arquivo = Path("teste3.txt")
# novapasta = Path("NovaPasta")

# arquivo.unlink()
# novapasta.rmdir()

# arquivo = Path("teste.txt")
# print(arquivo.read_text())
# arquivo.write_text("teste", encoding="utf-8")

# pasta = Path()
# for arquivo in pasta.iterdir():
#     print(arquivo)

# pasta = Path("teste")
# for arquivo in pasta.glob("*.pdf"):
#     print(arquivo)

# # ----------------------------exercicios
# 1
# novapasta = Path("dados/entrada")
# novapasta1 = Path("dados/saida")
# novapasta2 = Path("relatorios")
# novapasta.mkdir(exist_ok=True, parents=True)
# novapasta1.mkdir(exist_ok=True, parents=True)
# novapasta2.mkdir(exist_ok=True, parents=True)

# 2
# texto1 = Path("dados/entrada/dados1.txt")
# texto2 = Path("dados/entrada/dados2.txt")
# texto3 = Path("dados/entrada/dados3.txt")
# texto1.mkdir(exist_ok=True, parents=True)
# texto2.mkdir(exist_ok=True, parents=True)
# texto3.mkdir(exist_ok=True, parents=True)

# 3

# pastas = Path("dados/entrada")

# for arquivo in pastas.glob("*.txt"):
#     print(arquivo.name)


