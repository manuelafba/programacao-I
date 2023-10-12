def verificar_ganhadores_brinde(lista_numeros):
    cont = 0

    for item in lista_numeros:
        if lista_numeros.index(item) + 1 == item:
            cont += 1

    return cont

ganhadores = verificar_ganhadores_brinde([3, 2, 5, 4, 8, 6, 7, 10, 12, 13, 11])
print(f"{ganhadores} convidados irão ganhar brindes")