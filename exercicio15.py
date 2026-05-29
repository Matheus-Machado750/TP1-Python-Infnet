"""
Exercício 15 Telemetria Aeroespacial e Autonomia de Voo

Um drone de monitoramento ambiental realizou dois voos de mapeamento, um com duração de 3,77 horas, enquanto o outro foi de 214 minutos. No entanto, o sistema de telemetria de bateria processa o consumo de energia exclusivamente em segundos.
Para calcular a energia total que a bateria deve ter, considere que cada segundo do drone corresponde a 2,7 joules. O impacto esperado é o cálculo preciso da energia necessária para evitar a perda do equipamento durante o pouso, adicionando 15% de margem de segurança.

Tarefa:

A partir do tempo de ambos os voos, desenvolva o raciocínio lógico para converter o total integralmente para a unidade de segundos, e obter quanto de energia foi gasto nos voos.
Em seguida, considere a margem de segurança e armazene o resultado final em uma variável apropriada e exiba no terminal.
"""

voo1 = 3.77
voo2 = 214

voo1_segundos = voo1 * 3600
voo2_segundos = voo2 * 60

total_segundos = voo1_segundos + voo2_segundos

energia = total_segundos * 2.7

valor_final = energia * 1.15

print(valor_final)