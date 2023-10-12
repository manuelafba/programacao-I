def verificar_validade(lista_produtos, lista_meses, mes):
    lista_filtrada = []

    for produto, validade in zip(lista_produtos, lista_meses):
        if validade >= mes:
            lista_filtrada.append([produto, validade])
    
    return lista_filtrada

produtos = ['BB', 'AA', 'CC', 'DD', 'EE', 'FF']
validades = [2, 3, 4, 7, 1, 2]

print(verificar_validade(produtos, validades, 3))