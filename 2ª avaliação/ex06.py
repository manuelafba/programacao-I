# Escreva um programa para reconehcer uma string contendo somente zeros e uns e que não tenha dois uns consecutivos.

import re

msg = input("Digite uma string contendo apenas zeros e uns e que não tenha dois uns consecutivos: ")

regex = re.compile(r"[01]+$")  

if regex.fullmatch(msg) and not re.search(r"11", msg):
    print("String válida")
else:
    print("String inválida")
