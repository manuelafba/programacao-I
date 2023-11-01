# Escreva um programa para reconhecer as strings que sejam sequências de letras A e de tamanho par.

import re

msg = 'aaaaaa'

saida = len(msg) % 2 == 0 and\
    re.compile(r'[a]+')

if saida:
    print("Ok")
else:
    print("Fail")