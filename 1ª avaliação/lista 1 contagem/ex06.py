def calcular_quantidade_itens_backlog(lista_complexidade, velocidade):
    soma_complexidades = 0
    cont = 0

    for item in lista_complexidade:
        if soma_complexidades + item <= velocidade:
            soma_complexidades += item
            cont += 1
        else:
            break  

    return cont

quantidade_itens = calcular_quantidade_itens_backlog([5, 3, 4, 7, 10, 2, 3, 13, 25, 1, 1, 8], 15)
print(f"{quantidade_itens} itens podem ser incluídos na sprint backlog")
