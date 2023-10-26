def cadastrar():
        nome = input("Digite seu nome: ")
        nascimento = input("Digite seu nascimento: ")
        sexo = input("Digite seu sexo: ")
        cpf = int(input("Digite seu cpf: "))
        rg = int(input("Digite seu nome: "))
        telefone = int(input("Digite seu nome: "))
        
        return validar_cadastro()
        #if not cpf.isdigit() or not rg.isdigit() or not telefone.isdigit():
        #    raise Exception("CPF, RG e Telefone devem ser númericos")
        #elif type(nome, nascimento, sexo) != str:
        #    raise Exception("CPF, RG e Telefone devem ser formados apenas por letras )
