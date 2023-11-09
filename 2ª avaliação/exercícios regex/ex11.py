import re

telefone = input("Digite seu telefone nesse formato: (XX) 9XXXX-XXXX")

saida = re.fullmatch("\(\d{2})\s9\d{4}-\d{4}", telefone)

# sub('[()\s-]', "", tel)

if saida:
    print("Telefone válido")
else:
    print("Telefone inválido")