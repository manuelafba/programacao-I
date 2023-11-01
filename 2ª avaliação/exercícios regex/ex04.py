# Escreva um programa para encontrar todas as ocorrências de telefones celulares que tenha ou não ddd especificado e que usem ou não hífen.

import re

numeros = "(91) 91234-5678, 9987654321, 55678909"

regex = re.compile(r'\(?\d{0,2}\)?[-.\s]?\d{5}[-.\s]?\d{4}') # \(? paraparênteses opcionais, \d{0,2} para 0 até 2 dígitos no DDD, [-.\s]? para ponto, hífen ou espaço opcionais, \d{5} para verificar os 5 primeiros dígitos, \d{4} para verificar os 4 últimos dígitos 
saida = regex.findall(numeros)

print(saida)