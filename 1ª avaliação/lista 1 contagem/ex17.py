def verificar_pa(sequencia):
    razao = sequencia[1] - sequencia[0]

    for i in range(2, len(sequencia)):
        if sequencia[i] - sequencia[i - 1] != razao:
            return False

    return True

pa = verificar_pa([2, 4, 6, 8, 11, 12, 14])
print(pa)
