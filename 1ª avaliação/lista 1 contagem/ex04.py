def calcular_media_pares(lista_numeros):
    lista_pares = []
    media = 0

    for item in lista_numeros:
        if item % 2 == 0:
            lista_pares.append(item)
            media = sum(lista_pares) // len(lista_pares)

    return media

media = calcular_media_pares([3, 5, 4, 6, 3, 2, 8, 10])
print(f"A média entre os números pares da lista é {media}")
