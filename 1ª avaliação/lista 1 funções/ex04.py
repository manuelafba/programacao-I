def filtrar_por_tipo(lista, tipo):
    """
    Filtrar uma lista de listas para construir outra lista apenas com números inteiros

    Argumentos: 
    - lista: lista de listas
    - tipo: inteiro
    
    Retorno: lista filtrada apenas com inteiros
    """
    lista_resultante = []
    for item in lista:
        if type(item) == tipo:
            lista_resultante.append(item)
    
    return lista_resultante

def filtrar_inteiros(lista, tipo):

    lista_filtrada = []

    for item in lista:
        lista_filtrada.append(filtrar_por_tipo(item, int))
    return lista_filtrada

lista = filtrar_inteiros([[1, 2, 3.3], ['A', 5, '7']], int)
print(lista)

def filtrar_por_tipo2(lista):
    return [item for item in lista if type(item) == int]

def filtrar_inteiros2(lista):
    return [filtrar_por_tipo2(item, int) for item in lista]

lista = filtrar_inteiros([[1, 2, 3.3], ['A', 5, '7']], int)
print(lista)


