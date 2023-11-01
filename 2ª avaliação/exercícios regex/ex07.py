# Escreva um programa para informar o índice inicial e final de todas as substrings que tenham o prefixo R$
import re

strings = "R$1328, 57486, R$9587"

regex = re.compile(r'^[R$]+')

saida = regex.search(strings)

print(saida.span())