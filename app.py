# Perguntas para o usuário
aparelho = input("Qual o nome do aparelho? ")
potencia = float(input("Qual a potência em Watts (W)? "))
horas_dia = float(input("Quantas horas ele é usado por dia? "))

# Conta matemática
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Mostra o resultado na tela
print("-" * 30)
print(f"Aparelho: {aparelho}")
print(f"Consumo mensal: {consumo_mensal:2f}kWh/mês")
print("-" * 30)
