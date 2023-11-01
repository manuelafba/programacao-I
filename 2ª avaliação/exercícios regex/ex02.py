# Escreva um programa para remover de uma string tudo o que não for espaço ou letra.

import re

string = 'Oi, tudo bem? 1234'

saida = re.sub(r'[^a-zA-Z\s]', '', string)

print(saida)