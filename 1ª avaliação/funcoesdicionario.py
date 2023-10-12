def calcular_saldo_medio(cadastros):
    saldo_medio = 0
    for elemento in cadastros:
        saldo_medio += elemento['saldo']  # atribuição composta sempre implica na atualização da variável
        
    return saldo_medio/len(cadastros)

def filtrar_email(cadastros):
    for elemento in cadastros.copy(): # se a função alterar o tamanho da lista, criar uma cópia
        if 'gmail' in elemento['email']: # verificar se algo está dentro da lista/String
            cadastros.remove(elemento) 
    return cadastros
