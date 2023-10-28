def validar_cadastro(nome, nascimento, sexo, cpf, rg, telefone, cadastros):

    if not cpf.isdigit() or not rg.isdigit() or not telefone.isdigit():
        raise Exception("CPF, RG e Telefone devem ser numéricos")
    if type(nome) != str or type(sexo) != str:
        raise Exception("Nome e sexo devem ser formados apenas por letras")
    if len(cpf) != 11:
        raise Exception("CPF inválido")
    if len(rg) != 7:
        raise Exception("RG inválido")
    if nascimento < 1900 or nascimento > 2023:
        raise Exception("Nascimento inválido")

    cadastros.append({'Nome': nome, 'Nascimento': nascimento, 'Sexo': sexo, 'CPF': cpf, 'RG': rg, 'Telefone': telefone})
    return cadastros


def cadastrar(cadastros):
    dados = {
        "Nome": input("Digite seu nome: "),
        "Nascimento": input("Digite seu nascimento: "),
        "Sexo": input("Digite seu sexo: "),
        "CPF": input("Digite seu CPF: "),
        "RG": input("Digite seu RG: "),
        "Telefone": input("Digite seu telefone: ")
    }

    return validar_cadastro(dados['Nome'], dados['Nascimento'], dados['Sexo'], dados['CPF'], dados['RG'], dados['Telefone'], cadastros)

def listar_cadastros(cadastros):
    if len(cadastros) == 0:
        print("Nenhum cadastro foi encontrado")
    for item in cadastros:
        print('Nome: ', item['Nome'])
        print('Nascimento: ', item['Nascimento'])
        print('Sexo: ', item['Sexo'])
        print('CPF: ', item['CPF'])
        print('RG: ', item['RG'])
        print('Telefone: ', item['Telefone'])

opcao = '1'
cadastros = []

try:
    while opcao in ['1', '2']:
        opcao = input("Digite [1] para fazer um novo cadastro ou [2] para listar todos os cadastros: ")
        if opcao == '1':
            cadastros = cadastrar(cadastros)
        elif opcao == '2':
            listar_cadastros(cadastros)
except Exception as e:
    print(e)
