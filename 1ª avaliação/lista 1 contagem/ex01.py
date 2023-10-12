def verificar_tamanho_embalagem(lista_tamanhos):
    cont = 0

    for item in lista_tamanhos:
        if item < 7:
            cont += 1
    return cont

embalagens = verificar_tamanho_embalagem([8, 18, 4, 20, 1, 12])
print(f"Existem {embalagens} embalagens fora do padrão estabelecido pela Sociedade Brasileira dos Caramelos")