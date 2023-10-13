def filtar_nomes(lista_nomes, prefixo):
    nomes = []

    for nome in lista_nomes:
        if nome[:len(prefixo)] == prefixo:
            nomes.append(nome)

    return nomes

nomes = filtar_nomes(['Boris', 'Samara', 'Sabrina', 'Carlos', 'Samarone'], 'Sa')
print(nomes)