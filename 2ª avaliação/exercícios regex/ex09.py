# Escreva um programa para encontrar todas as ocorrências de palavras que iniciam com letra maiúscula.
import re

palavras = "Gato, dados, estrela, Lua"

regex = re.compile(r"\b[A-Z]\w*")

for item in regex.finditer(palavras):
    print(item)