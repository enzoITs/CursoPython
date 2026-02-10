from datetime import datetime

agora = datetime.now()
# print(agora)
# print(agora.day)
# print(agora.month)
# print(agora.hour)
# print(agora.second)

# aniversario = datetime(2009, 12, 15)
# print(aniversario)
# print(aniversario.day)

# print(agora.strftime("hoje é dia %d do mes %m do ano %Y")) 
# print(agora.strftime("Agora é %H horas"))

# data_str = "15/12/2026"
# data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
# print(data_convertida)

# --------------------exercicios-------------------------

# 1
# horario = agora.hour
# if horario < 12:
#     print('Bom dia')
# elif horario < 18:
#     print('Boa tarde')
# else:
#     print('Boa noite')

# 2
# mes = agora.month
# restante = 12 - mes
# print(restante)

# 3
# def assinatura():
#     nome = input('Digite sua assinatura: ')
#     print(agora.strftime(f"Assinatura gerada por {nome} em %d de %B de %Y às %H:%M"))

# assinatura()

# ---------------------------------------
