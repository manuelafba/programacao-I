def encontrar_menor_soma(lista1, lista2, lista3):
    """
    Encontrar a menor soma dos elementos de índices correspondentes nas três listas

    Argumentos:
    - lista1, lista2, lista3: listas de números 

    Retorno: a menor soma encontrada
    """
    somas = []
    for item in zip(lista1, lista2, lista3):
        somas.append(sum(item))
    
    return min(somas)

lista = encontrar_menor_soma([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(lista)

def encontrar_menor_soma2(lista1, lista2, lista3):
    somas = [sum(item) for item in zip(lista1, lista2, lista3)]
    return min(somas)

lista = encontrar_menor_soma2([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(lista)