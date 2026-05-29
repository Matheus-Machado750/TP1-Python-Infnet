"""
Exercício 11 Otimização de Carga e Estabilidade de Frete

Um operador logístico trabalha com o transporte de insumos industriais em caminhões de pequeno porte. Cada saca de polímero pesa exatamente 65kg, e o veículo possui um limite de carga útil de 550kg.
O impacto esperado é garantir que o caminhão nunca ultrapasse sua capacidade máxima, transportando apenas unidades inteiras para evitar o deslocamento perigoso da carga durante o trajeto.

Tarefa:

Com base na capacidade de 550 kg e no peso unitário de 65kg, desenvolva um código que calcule o número máximo de sacas que podem ser embarcadas em um caminhão sem exceder o limite, bem como a porcentagem de ocupação do peso do caminhão.
O resultado deve ser armazenado em uma variável que represente a capacidade real e outra com a porcentagem, ambas exibidas no console.
"""

saca_polimero = 65

capacidade_caminhao = 550

quant_max_sacas = capacidade_caminhao // saca_polimero

capacidade_preenchida = saca_polimero * quant_max_sacas

porcentagem = capacidade_preenchida // 5.5
#550 dividido por 100, que resulta na porcentagem do valor total (o número de baixo da fração)

print(f"A quantia máxima de sacas é {quant_max_sacas}")
print(f"A porcentagem ocupada do caminhão é de {porcentagem}%")