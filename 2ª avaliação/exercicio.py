def validar_cadastro(nome, nascimento, sexo, cpf, rg, telefone):
    if not cpf.isdigit() or not rg.isdigit() or not telefone.isdigit():
        raise Exception("CPF, RG e Telefone devem ser númericos")
    elif type(nome, sexo) != str:
        raise Exception("Nome e sexo devem ser formados apenas por letras")
    elif len(cpf) != 11:
         raise Exception("CPF inválido")
    elif nascimento < 1900:
         raise Exception("Nascimento inválido")
    cadastros.append({'Nome': nome, 'Nascimento': nascimento, 'Sexo': sexo, 'CPF': cpf, 'RG': rg, 'Telefone': telefone}) 
    return cadastros

def cadastrar(cadastros):
        nome = input("Digite seu nome: ")
        nascimento = input("Digite seu nascimento: ")
        sexo = input("Digite seu sexo: ")
        cpf = int(input("Digite seu cpf: "))
        rg = int(input("Digite seu nome: "))
        telefone = int(input("Digite seu nome: "))
        
        return validar_cadastro(nome, nascimento, sexo, cpf, rg, telefone, cadastros)

def listar(cadastros):
     for item in cadastros:
          print('Nome: ',item['nome'])
          print('Nascimento: ',item['nascimento'])
          print('Sexo: ',item['sexo'])
          print('CPF: ',item['cpf'])
          print('RG: ',item['rg'])
          print('Telefone: ',item['telefone'])
          

opcao = '1'
cadastros = []
try:
        while opcao in ['1', '2']:
                opcao = input("Digite [1] para fazer um novo cadastro ou [2] para listar todos os cadastros: ")
                if opcao == 1:
                        cadastrar(cadastros)
                if opcao == 2:
                        listar()
except Exception as e:
      print(e)
