def busca_binaria(lista_inteiros, numero_buscado):
    """
    Realizar uma busca binária em uma lista ordenada de números inteiros

    Argumentos: lista_inteiros: uma lista de números inteiros que será ordenada
    numero_buscado: o número a ser buscado na lista
    
    Retorno: comparacoes: o número total de comparações realizadas durante a busca até o número ser encontrado
    True se o elemento foi encontrado, caso contrário, o retorno será False
    """
    lista_ordenada = sorted(lista_inteiros)
    comparacoes = 0
    inicio, fim = 0, len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        numero_meio = lista_ordenada[meio]
        comparacoes += 1

        if numero_meio == numero_buscado:
            return comparacoes, True
        elif numero_meio > numero_buscado:
            fim = meio - 1
        else:
            inicio = meio + 1

    return comparacoes, False

comparacoes, resultado = busca_binaria([1, 2, 4, 9, 3, 5], 4)
print(f"{resultado}, {comparacoes} comparações")