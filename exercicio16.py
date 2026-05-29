"""
Exercício 16 Decomposição de Jornada para Fechamento de Folha

Um técnico de som trabalhou em um set de filmagem por um total de 1527 minutos. Para o fechamento do contrato, o RH precisa que o tempo seja discriminado, separando as horas completas dos minutos excedentes, pois as horas e os minutos possuem valores de pagamento distintos.
O impacto esperado é a transparência e conformidade com os acordos sindicais. Para este contrato, cada hora completa trabalhada é paga a R$ 60,00 e cada minuto excedente é paga a R$ 1,20. O impacto esperado é conseguir definir com precisão o valor que deverá ser pago.

Tarefa:

A partir do total de 1527 minutos, calcule a quantidade de horas inteiras trabalhadas e a quantidade de minutos restantes. Em seguida, calcule o valor total referente às horas e o valor total referente aos minutos excedentes.

Exiba no terminal devidamente sinalizada:

Horas trabalhadas
Minutos excedentes
Valor pago pelas horas
Valor pago pelos minutos
Valor total a receber
"""

valor_minutos = 1527

valor_horas = 1527 // 60

minutos_excedentes = 1527 % 60

pagamento_horas = valor_horas * 60
pagamento_minutos = minutos_excedentes * 1.20

total_receber = pagamento_horas + pagamento_minutos

print(f"Horas trabalhadas: {valor_horas}")
print(f"Minutos excedentes: {minutos_excedentes}")
print(f"Pagamento pelas horas: {pagamento_horas}")
print(f"Pagamento pelos minutos: {pagamento_minutos}")
print(f"Pagamento total à receber: {total_receber}")