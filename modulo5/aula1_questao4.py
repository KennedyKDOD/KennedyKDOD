import datetime

data_hora_atual = datetime.datetime.now()

# Formata a data no formato dd/mm/aaaa
data_formatada = data_hora_atual.strftime("%d/%m/%Y")

# Formata a hora no formato hh:mm
hora_formatada = data_hora_atual.strftime("%H:%M")

# Exibe a data e hora formatadas
print("Data:", data_formatada)
print("Hora:", hora_formatada)
