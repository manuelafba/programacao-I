# Escreva um programa para reconhecer uma string contendo somente zeros e uns e que tenha pelo menos três ocorrências do dígito um.

import re

string = input("Digite uma string com 0 e 1: ")

if re.search(r'[1]{3,}', string) and\
    re.fullmatch(r'^[01]+$', string):
    print("String válida")
else:
    print("String inválida")
