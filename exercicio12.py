"""
Exercício 12 Sincronização de Turnos e Manutenção Preventiva

Uma planta petroquímica opera em ciclos ininterruptos de produção que duram 8 dias.
Após um período de 125 dias de operação contínua, o engenheiro de manutenção precisa identificar em qual estágio do ciclo atual (de 0 a 7) a planta se encontra para agendar uma parada técnica, que deve ser feita apenas no fim do ciclo.
O impacto esperado é a precisão no cronograma de manutenção preditiva.

Tarefa:

Considerando o total de 125 dias decorridos e a periodicidade de 8 dias, escreva um programa que determine a fase atual da operação dentro do ciclo e com quantos dias decorridos ao todo poderemos ter a parada técnica.
Exiba com duas variáveis o valor resultante que indica o dia atual do ciclo e a quantidade total de dias decorridos até a parada.
"""

duracao_ciclo = 8

periodo_total = 125

dia_ciclo = periodo_total % duracao_ciclo

dias_faltantes = duracao_ciclo - dia_ciclo

print(f"Estamos no dia {dia_ciclo} do ciclo, e o total de dias decorridos até a parada será de {periodo_total + dias_faltantes}")