# Escreva um programa para encontrar todas as ocorrências de palavras que inicie com letra maiúscula.
import re

palavras = 'Estrela, gato, dados, Lua'

regex = re.compile(r"^[A-Z]")
saida = regex.findall(palavras)

print(saida)