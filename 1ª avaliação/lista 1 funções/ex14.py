def buscar_linearmente_lista_ordenada(lista, elemento):
    """
    Ordena uma lista de inteiros e realiza uma busca linear 

    Argumentos: lista: uma lista de números inteiros 
    elemento: o número a ser buscado na lista
    
    Retorno: comparacoes: o número total de comparações realizadas durante a busca até o número ser encontrado
    True se o elemento foi encontrado, caso contrário, o retorno será False
    """
    comparacoes = 0

    for item in sorted(lista):
        comparacoes += 1
        if item == elemento:
            return comparacoes, True
        
    return comparacoes, False

comparacoes, resultado = buscar_linearmente_lista_ordenada([1, 2, 4, 9, 3, 5], 4)
print(f"{resultado}, {comparacoes} comparações")