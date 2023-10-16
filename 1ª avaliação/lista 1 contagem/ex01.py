def verificar_tamanho_embalagem(lista_tamanhos):
    cont = 0

    for item in lista_tamanhos:
        if item < 7:
            cont += 1
    return cont

embalagens = verificar_tamanho_embalagem([7, 6, 5, 4, 3, 6, 7, 8, 20, 3, 12])
print(f"Existem {embalagens} embalagens fora do padrão estabelecido pela Sociedade Brasileira dos Caramelos")

def verificar_tamanho_embalagem2(lista_tamanhos):
    return sum(1 for item in lista_tamanhos if item < 7)

embalagens = verificar_tamanho_embalagem2([8, 18, 4, 20, 1, 12])
print(f"Existem {embalagens} embalagens fora do padrão estabelecido pela Sociedade Brasileira dos Caramelos")