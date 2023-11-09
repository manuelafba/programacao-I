import re

string = input("Escreva uma operação aritmética entre números inteiros: ")

saida = re.search(r'[0-9]', string) and\
    re.search(r'[+_*/=]', string) and\
    not re.search(r"[.,]", string)

if saida:
    print("String válida")
else:
    print("String inválida")