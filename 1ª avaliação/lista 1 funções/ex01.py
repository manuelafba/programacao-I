def concatenar_listas(lista1, lista2):
    """
    Faz o mapeamento para obter uma lista em que cada elemento seja a concatenação dos elementos de mesmo índice de duas listas de strings

    Argumentos: 
    - lista1, lista2: listas de strings
    
    Retorno: uma lista de strings, cada uma com o elemento de seu índice correspondente
    """
    lista_concatenada = []
    for item in zip(lista1, lista2):
        lista_concatenada.append(item)

    return lista_concatenada

lista_concatenada =  concatenar_listas(['a', 'b', 'c'], ['d', 'e', 'f'])
print(lista_concatenada)

def concatenar_listas2(lista1, lista2):
    return [item for item in zip(lista1, lista2)]

lista_concatenada =  concatenar_listas2(['aa', 'bb', 'cc'], ['dd', 'ee', 'ff'])
print(lista_concatenada)