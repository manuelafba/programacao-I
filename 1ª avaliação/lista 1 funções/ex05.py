def filtrar_strings(lista_strings, lista_inteiros):
    """
    Filtrar uma lista de strings e retornar uma outra lista de strings com elementos onde seus tamanhos são iguais ou menores ao número de índice correspondente em uma lista de inteiros

    Argumentos: lista_strings: lista de strings
    lista_inteiros: lista de inteiros
    
    Retorno: lista filtrada de strings
    """
    lista_filtrada = []

    for string, tamanho in zip(lista_strings, lista_inteiros):
        if len(string) <= tamanho:
            lista_filtrada.append(string)
        
    return lista_filtrada
    
lista_resultante = filtrar_strings(['AAAA', 'BB', 'CCC'], [2, 5, 3])
print(lista_resultante)

def filtrar_strings2(lista_strings, lista_inteiros):
    return [string for string, tamanho in zip(lista_strings, lista_inteiros) if len(string) <= tamanho]

lista_resultante = filtrar_strings2(['AAAA', 'BB', 'CCC'], [2, 5, 3])
print(lista_resultante)

       