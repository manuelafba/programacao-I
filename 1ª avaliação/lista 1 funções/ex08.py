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

def detectar_maior_string2(lista):
     return [max((len(item), i) for i, item in enumerate(lista))]

lista_de_strings = ["AAA", "AAAAA", "A", "AAAA"]
resultado = detectar_maior_string2(lista_de_strings)
print(resultado)