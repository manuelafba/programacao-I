def verificar_distancia_hamming(sequencia1, sequencia2):
    distancia = 0

    for x, y in zip(sequencia1, sequencia2):
        if x != y:
            distancia += 1

    return distancia

sequencia1 = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
sequencia2 = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
print(verificar_distancia_hamming(sequencia1, sequencia2))


