def verificar_frequencia_sequencia(lista_sequencias, sequencia):
    return lista_sequencias.count(sequencia)

lista_sequencias = ['TACG', 'GAGC', 'ATUC', 'TAGC', 'GAGC']
sequencia = 'GAGC'
frequencia = verificar_frequencia_sequencia(lista_sequencias, sequencia)
print(f"A frequência da sequência {sequencia} é {frequencia}")