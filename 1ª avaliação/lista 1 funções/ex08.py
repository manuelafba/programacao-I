def detectar_maior_string(lista):
    """
    Detectar a maior string em uma lista e retornar seu tamanho e índice

    Arumentos:
    - lista: lista de strings

    Retorno: o tamanho da maior string e seu índice na lista
    """

    maiortamanho = len(lista[0])
    indice = 0

    for item in lista:
        if len(item) > maiortamanho:
            maiortamanho = len(item)
            indice = lista.index(item)

    return maiortamanho, indice

lista_de_strings = ["AAA", "AAAAA", "A", "AAAAA"]
resultado, indice = detectar_maior_string(lista_de_strings)
print(f"O tamanho da maior string é {resultado} e está no índice {indice}")