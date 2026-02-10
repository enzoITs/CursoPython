from datetime import datetime, timedelta

# hoje = datetime.now()
# um_dia = timedelta(days=1)

# amanha = hoje + um_dia
# ontem, = hoje - um_dia
# print(amanha)

# prazo = datetime(2026, 12, 15)
# hoje = datetime.now()
# if hoje > prazo:
#     print("atraso")
# else:
#     print("No prazo")

# futuro = datetime(2026, 2, 21)
# dias_restantes = futuro - datetime.now()
# print(dias_restantes.days)

# aniversario = datetime(2026, 6, 27)
# hoje = datetime.now()
# if hoje < aniversario:
#     print("Nao passou")
# elif hoje == aniversario:
#     print("é hoje")
# elif hoje > aniversario:
#     print("Ja passou")


# ----------------------------------------------
# exercicios

# 1
# hoje = datetime.now()
# futuro = datetime(2026, 12, 31)
# restante = futuro - hoje
# print(f'faltam {restante.days} dias para o ano novo')

# 2
# evento = input('Digite a data do evento: ')
# data_evento = datetime.strptime(evento, "%d/%m/%Y")
# hoje = datetime.now()

# if hoje < data_evento:
#     print('Nao passou')
# elif hoje == data_evento:
#     print("é hoje")
# elif hoje > data_evento:
#     print('Ja passou')

# 3
# data_produto = input('Digite a data de fabricação do produto: ')
# validade_produto = datetime.strptime(data_produto, "%d/%m/%Y")
# validade = timedelta(days=180)
# validade_do_produto = validade_produto + validade
# hoje = datetime.now()
# print(f'Validade: {validade_do_produto}')
# if hoje < validade_do_produto:
#     print('Dentro da Validade')
# else:
#     print("Fora da validade")

# if hoje < validade_do_produto:
#     print(f'Faltam {validade_do_produto - hoje}')
# else:
#     print(f'Ja passou {hoje - validade_do_produto}')   




