from pathlib import Path
from datetime import datetime, timedelta
import shutil

organizador = Path('projeto/organizador')
organizador.mkdir(exist_ok=True, parents=True)

shutil.unpack_archive('projeto/organizador.zip', 'projeto/organizador')
pdfs = Path('projeto/pdfs')
xlsxs = Path('projeto/xlsxs')
pngs = Path('projeto/pngs')
txts = Path('projeto/txts')
jpgs = Path('projeto/jpgs')
docxs = Path('projeto/docxs')
pdfs.mkdir(exist_ok=True, parents=True)
xlsxs.mkdir(exist_ok=True, parents=True)
pngs.mkdir(exist_ok=True, parents=True)
txts.mkdir(exist_ok=True, parents=True)
jpgs.mkdir(exist_ok=True, parents=True)
docxs.mkdir(exist_ok=True, parents=True)


agora = datetime.now()
log = Path('projeto/logs.txt')


pasta = Path('projeto/organizador')
for arquivo in pasta.glob("*.pdf"):
    shutil.move(arquivo, 'projeto/pdfs')
    with log.open('a',  encoding='utf-8') as arquivo:
        arquivo.write(f'{agora} || {arquivo.name} Arquivo PDF movido')

for arquivo in pasta.glob("*.xlsx"):
    shutil.move(arquivo, 'projeto/xlsxs')
    with log.open('a',  encoding='utf-8') as arquivo:
        arquivo.write(f'{agora} || {arquivo.name} Arquivo XLSX movido')
    
for arquivo in pasta.glob("*.png"):
    shutil.move(arquivo, 'projeto/pngs')
    with log.open('a',  encoding='utf-8') as arquivo:
        arquivo.write(f'{agora} || {arquivo.name} Arquivo PNG movido')

for arquivo in pasta.glob("*.txt"):
    shutil.move(arquivo, 'projeto/txts')
    with log.open('a',  encoding='utf-8') as arquivo:
        arquivo.write(f'{agora} || {arquivo.name} Arquivo TXT movido')

for arquivo in pasta.glob("*.jpg"):  
    shutil.move(arquivo, 'projeto/jpgs')
    with log.open('a',  encoding='utf-8') as arquivo:
        arquivo.write(f'{agora} || {arquivo.name} Arquivo JPG movido')

for arquivo in pasta.glob("*.docx"):
    shutil.move(arquivo, 'projeto/docxs')
    with log.open('a',  encoding='utf-8') as arquivo:
        arquivo.write(f'{agora} || {arquivo.name} Arquivo DOCX movido')    

      


