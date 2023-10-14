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
        soma = sum(lista[item])
        proxima_soma = sum(lista[item + 1])
        
        if soma > proxima_soma:
            lista_filtrada.append(lista[item])
    
    return lista_filtrada

lista_de_lista_inteiros = filtrar_listas([[6, 2, 3], [4, 5, 6], [7, 8, 9]])
print(lista_de_lista_inteiros)
