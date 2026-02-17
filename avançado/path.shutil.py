import shutil
from pathlib import Path

# shutil.copy2("teste.txt", "backup/teste.txt")

# shutil.copytree("meus_arquivos", "backup2" dirs_exist_ok=True)

# teste = Path("aaa.txt")
# shutil.move(teste, "meus_arquivos")

# shutil.rmtree("backup2")

# shutil.make_archive("teste", "zip", "teste")

# shutil.unpack_archive('teste.zip')

# -------------------------------------exercicios
# 1

# imagens = Path("imagens")
# imagens.mkdir(exist_ok=True, parents=True)
# img1 = Path('imagens/imagem1.png')
# img2 = Path('imagens/imagem2.png')
# img1.mkdir(exist_ok=True, parents=True)
# img2.mkdir(exist_ok=True, parents=True)
# backup = Path('backup')
# backup.mkdir(exist_ok=True, parents=True)
# shutil.copytree('imagens', 'backup', dirs_exist_ok=True)

# 2

# texto = Path('relatorio.txt')
# backup = Path('backup')
# backup.mkdir(exist_ok=True, parents=True)
# if texto.exists():
#     print('existe!')
#     shutil.move(texto, 'relatorios_antigo/relatorio_backup.txt')
# else:
#     print('deu ruim')

# 3
# extraido = Path('extraido')
# extraido.mkdir(exist_ok=True, parents=True)
# shutil.unpack_archive('arquivos_secretos.zip', extraido)
# shutil.copytree('arquivos_secretos', 'extraido')
# for arquivo in extraido.iterdir():
#     print(arquivo.stem)


    