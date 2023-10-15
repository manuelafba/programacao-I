# refazer
def filtrar_listas(lista):
    """
    Filtrar uma lista de listas de números inteiros para obter uma lista de listas onde a soma dos elementos da lista de uma determinada posição é maior que a soma dos elementos da lista da próxima posição.
    
    Argumentos:
    - lista: lista de listas de números inteiros

    Retorno: lista filtrada de inteiros
    """

    lista_filtrada = []

    for item in range(len(lista) - 1):
        if sum(lista[item]) > sum(lista[item + 1]):
            lista_filtrada.append(lista[item])
    
    return lista_filtrada

lista_de_lista_inteiros = filtrar_listas([[1, 2, 7], [7, 3, 9], [3, 2, 0]])
print(lista_de_lista_inteiros)

def filtrar_listas2(lista):
    return [lista[item] for item in range(len(lista) - 1) if sum(lista[item]) > sum(lista[item + 1])]

lista_de_lista_inteiros = filtrar_listas2([[1, 2, 7], [7, 3, 9], [3, 2, 0]])
print(lista_de_lista_inteiros)
