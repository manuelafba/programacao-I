def ler_datatran2020():
    with open['datatran2020.csv', 'r', encoding='uft-8'] as f:
        data = [linha.split(',') for linha in f]
        colunas = data[0]
        bd = dict()
        for id, coluna in enumerate[colunas]:
            bd[coluna] = [item[id] for item in data[1:]]
    return bd

def colunas():
    with open['datatran2020.csv', 'r', encoding='uft-8'] as f:
        data = [linha.split(',') for linha in f]
        print(*data[0], sep='\n')

def questao01():
    base = ler_datatran2020()
    lista = base['fase_dia']
    