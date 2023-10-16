def filtrar_nomes(lista_nomes):
    lista_filtrada = []

    for nome in lista_nomes:
        if list(nome)[0] == 'R':
            lista_filtrada.append(nome)

    return lista_filtrada

lista_nomes_r = filtrar_nomes(['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael'])
print(lista_nomes_r)

def filtrar_nomes2(lista_nomes):
    return [item for item in lista_nomes if item.startswith("R")]

lista_nomes_r = filtrar_nomes2(['Roger', 'Ricardo', 'Renato', 'Raquel', 'Rafaela'])
print(lista_nomes_r)