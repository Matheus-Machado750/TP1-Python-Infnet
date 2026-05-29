"""
Exercício 14 Auditoria de Desempenho e Eficiência de Ativos

O gestor de um parque industrial monitora o tempo de uso de braços robóticos em minutos para calcular o custo de depreciação. Um equipamento registrou 345 minutos de atividade, enquanto outro registrou 3 horas e 08 minutos.
Para o dashboard da diretoria, ambos os dados precisam ser convertidos para horas em formato decimal. O impacto esperado é a padronização dos indicadores de desempenho (KPIs) para análise de ROI.

Tarefa:

Crie um sistema que receba o registro de 345 minutos e realize a transformação para a grandeza de horas decimais.
O resultado deve refletir a fração exata do tempo de uso para que o custo por hora seja aplicado posteriormente.
Exiba o valor convertido.
"""

valor_minutos = 345

valor_transformado = valor_minutos / 60

print(valor_transformado)