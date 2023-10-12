def verificar_numeros(lista_numeros):
    cont = 0
    lista_pares_idx_par = []

    for idx, numero in enumerate(lista_numeros[1:]):
        if numero % 2 == 0 and idx % 2 == 0:
            cont += 1
            lista_pares_idx_par.append(numero)

    return lista_pares_idx_par, cont

lista_numeros, quantidade = verificar_numeros([0, 0 ,1, 3, 2, 4, 5, 6, 1, 2, 7])
print(lista_numeros, quantidade)