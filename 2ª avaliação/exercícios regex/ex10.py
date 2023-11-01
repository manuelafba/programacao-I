# Escreva um programa para reconhecer uma string contendo somente as letras A C T G e que as substrings AC ou TG apareçam pelo menos duas vezes não importando a ordem.
import re

string = input("Digite uma string contendo apenas as letras A C T G: ")

if re.search(r'[AC|TG]{2,}', string) and\
    re.fullmatch(r'^[ACTG]+$', string):
    print("String válida")
else:
    print("String inválida")