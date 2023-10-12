def reduzir_lista(lista):
    string_resultante = ''

    for item in lista:
        string_resultante += item
        if item != lista[-1]:
            string_resultante += ', '

    return string_resultante

string_resultante = reduzir_lista(['AAAAAAA', 'cupcake', 'gato'])
print(string_resultante)