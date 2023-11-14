def menu():
    op = int(input("1 - Cadastrar\n2- Listar\nAperte qualquer outra tecla para sair: "))
    return op

def cadastrar():
    nome = input("Digite seu nome: ")
    telefone = int(input("Digite seu telefone: "))
    email = input("Digite seu email: ")

    with open('bd_cadastro.txt', 'a', encoding="utf-8") as f:
        f.write(f"{nome}, {telefone}, {email}")
        f.write('\n')

    return nome, telefone, email


def listar():
    with open('bd_cadastro.txt', 'r', encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)


def main():
    while True:
        op = menu()
        if op  == 1:
            cadastrar()
        elif op == 2:
            listar()
        else:
            break

main()
