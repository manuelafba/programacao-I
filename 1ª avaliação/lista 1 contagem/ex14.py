def verificar_idades(lista_nomes, lista_idades, faixa_etaria):
    lista_participantes = []

    for idade, nome in zip(lista_idades, lista_nomes):
        if faixa_etaria[0] <= idade <= faixa_etaria[1]: # comparar as idades
            lista_participantes.append(nome)

    return lista_participantes

nomes = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
idades = [23, 45, 27, 60, 45]
faixa_etaria = [20, 30]
participantes = verificar_idades(nomes, idades, faixa_etaria)
print(participantes)