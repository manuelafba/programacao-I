def filtrar_strings_menores_10(lista_strings):
    """
    Construir uma lista de strings em ordem alfabética apenas com strings com tamanhos inferiores a 10

    Argumentos: 
    - lista_strings: lista de strings
    
    Retorno: lista de strings com tamanhos menores que 10 em ordem alfabética
    """
    lista_resultante = []
    for item in lista_strings:
        if len(item) < 10:
            lista_resultante.append(item)

    return sorted(lista_resultante)

lista = filtrar_strings_menores_10(['AAAAAAAAAAAAAAA', 'cccccc', 'a', 'bb',])
print(lista)

def filtrar_strings_menores_10_2(lista_strings):
    return [item for item in lista.sort() if len(item) < 10]

lista = filtrar_strings_menores_10_2(['AAAAAAAAAAAAAAA', 'cccccc', 'a', 'bb',])
print(lista)
