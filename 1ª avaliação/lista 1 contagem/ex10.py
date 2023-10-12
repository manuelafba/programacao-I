def filtar_nomes(lista_nomes):
    lista_filtrada = []

    for nome in lista_nomes:
        if list(nome)[0] == 'R':
            lista_filtrada.append(nome)

    return lista_filtrada

lista_nomes_r = filtar_nomes(['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael'])
print(lista_nomes_r)