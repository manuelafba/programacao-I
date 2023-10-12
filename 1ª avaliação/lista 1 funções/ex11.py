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

def achar_idx_maior_primo(lista_inteiros):
    """
    Encontra o índice do maior número primo em uma lista

    Argumentos:
    - lista_inteiros: uma lista de números inteiros

    Retorno:
    - maior_primo: o maior número primo na lista
    - indice_maior_primo: o índice maior número primo na lista. O valor será -1 caso não exitam números primos na lista
    """
    lista_primos = []
    maior_primo = 0
    indice_maior_primo = 0

    for item in lista_inteiros:
        if detectar_numero_primo(item):
            lista_primos.append(item)
            maior_primo = max(lista_primos)
            indice_maior_primo = lista_inteiros.index(maior_primo)

    if len(lista_primos) == 0:
        return -1, -1
    
    return maior_primo, indice_maior_primo

lista = [6, 8, 10, 12]
maior_primo, indice_maior_primo = achar_idx_maior_primo(lista)
print(f"O maior primo da lista é {maior_primo} e está no índice {indice_maior_primo}")
