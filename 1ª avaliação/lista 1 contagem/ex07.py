def verificar_ganhadores_brinde(lista_numeros):
    cont = 0

    for item in lista_numeros:
        if lista_numeros.index(item) + 1 == item:
            cont += 1

    return cont

ganhadores = verificar_ganhadores_brinde([3, 2, 5, 4, 8, 6, 7, 10, 12, 13, 11])
print(f"{ganhadores} convidados irão ganhar brindes")

def verificar_ganhadores_brinde2(lista_numeros):
    return sum(1 for item in lista_numeros if lista_numeros.index(item) + 1 == item)

ganhadores = verificar_ganhadores_brinde2([5, 4, 8, 9, 10, 12, 4, 3, 7, 4])
print(f"{ganhadores} convidados irão ganhar brindes")