def verificar_validade(lista_meses, mes):
    lista_produtos_na_validade = []

    for item in lista_meses:
        if item >= mes:
            lista_produtos_na_validade.append(item)

    return lista_produtos_na_validade

produtos_na_validade = verificar_validade([5, 4, 3, 11, 1, 1, 8 ,10, 11, 3, 4, 2, 10], 8)
print(f"Produtos na validade: {produtos_na_validade}")

def verificar_validade2(lista_meses, mes):
    return [item for item in lista_meses if item >= mes]

produtos_na_validade = verificar_validade2([2, 3, 4, 7, 1, 2, 1, 3], 3)
print(f"Produtos na validade: {produtos_na_validade}")
