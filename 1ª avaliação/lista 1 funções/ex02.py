def detectar_numero_primo(numero):
    """
    Verifica se o número é primo a partir da quantidade de divisores

    Argumentos: 
    - numero: número inteiro

    Retorno: Valor booleano True se o número for primo ou False caso não seja
    """
    for divisor in range(2, numero):
        if (numero % divisor == 0):
            return False
    return True

def calcular_proximo_primo(item):
    item += 1
    while not detectar_numero_primo(item):
        item += 1
    return item

def construir_lista_primos(lista):
    for item in lista:
        return [calcular_proximo_primo(item)]
    
lista_numeros = construir_lista_primos([12, 65, 78, 43, 21])
print(lista_numeros)

def construir_lista_primos2(lista):
    return [calcular_proximo_primo(item) for item in lista]

lista_numeros = construir_lista_primos2([12, 65, 78, 43, 21])
print(lista_numeros)