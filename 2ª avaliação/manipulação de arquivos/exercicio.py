def menu():
    op = int(input("1 - Cadastrar\n2- Listar\n3- Buscar por nome\nAperte qualquer outra tecla para sair: "))
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

def buscar_por_nome():
    lista_aux = []
    prefixo = input("Digite o prefixo do nome: ")
    with open('bd_cadastro.txt', 'r', encoding="utf-8") as f:
        for linha in f:
            if linha.startswith(prefixo):
                lista_aux.append(linha)
    print(sorted(lista_aux))


def main():
    while True:
        op = menu()
        if op  == 1:
            cadastrar()
        elif op == 2:
            listar()
        elif op == 3:
            buscar_por_nome()
        else:
            break

main()
