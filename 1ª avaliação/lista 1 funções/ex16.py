from random import randint

def verificar_frequencia_lista(lista, valor_referencia):
    return lista, valor_referencia, lista.count(valor_referencia)

lista_aleatoria = [randint(1, 100) for _ in range(1000)]
valor_referencia = randint(1, 100)
print(verificar_frequencia_lista(lista_aleatoria, valor_referencia))