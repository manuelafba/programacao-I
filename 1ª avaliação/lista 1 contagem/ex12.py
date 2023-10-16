def verificar_saldos_positivos(lista_nomes, lista_saldos):
    lista_filtrada = []

    for nome, saldo in zip(lista_nomes, lista_saldos):
        if saldo > 0:
            lista_filtrada.append(nome)
    
    return lista_filtrada

nomes = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
saldos = [100, -500, -1, 1500, 90]

print(verificar_saldos_positivos(nomes, saldos))

def verificar_saldos_positivos2(lista_nomes, lista_saldos):
    return [nome for nome, saldo in zip(lista_nomes, lista_saldos) if saldo > 0]

nomes = ['Roger', 'Ricardo', 'Renato', 'Raquel', 'Rafaela']
saldos = [-120, -300, -956, 1200]

print(verificar_saldos_positivos2(nomes, saldos))