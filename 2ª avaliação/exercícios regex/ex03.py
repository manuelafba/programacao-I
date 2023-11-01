# Escreva um programa para classificar senhas, tal que:

# muito forte: senha com no mínimo 10 caracteres, contendo letra maiúscula, minúscula, dígito e pelo menos três caracteres especiais.
# forte: senha com no mínimo 8 caracteres, contendo letra maiúscula, minúscula, dígito e caracteres especiais.
# média: senha com no mínimo 6 caracteres, contendo pelo menos letra maiúscula, minúscula e dígito.
# fraca: senha com no mínimo 6 caracteres que não seja senha classificada com força média.
# inválida: toda senha que não é fraca.
import re 

senha = input("Digite sua senha: ")

if len(senha) >= 10 and\
    re.search(r"[0-9]", senha) and\
    re.search(r"[a-z]", senha) and\
    re.search(r"[A-Z]", senha) and\
    re.search(r"[!@#$%&*=]{3,}", senha):
    print("Senha muito forte")

elif len(senha) >= 8 and\
    re.search(r"[0-9]", senha) and\
    re.search(r"[a-z]", senha) and\
    re.search(r"[A-Z]", senha) and\
    re.search(r"[!@#$%&*=]+", senha):
    print("Senha forte")

elif len(senha) >= 6 and\
    re.search(r"[0-9]+", senha) and\
    re.search(r"[a-z]+", senha) and\
    re.search(r"[A-Z]+", senha):
    print("Senha média")

elif len(senha) >= 6:
    print("Senha fraca")

else:
    print("Senha inválida")
    
