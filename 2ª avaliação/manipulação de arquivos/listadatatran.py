def ler_datatran2020():
    with open(r"C:\Users\desk\Documents\Github\programacao-I\2ª avaliação\manipulação de arquivos\datatran2020.csv", 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        colunas = data[0]
        bd = dict()
        for id, coluna in enumerate(colunas):
            bd[coluna] = [item[id] for item in data[1:]]
    return bd

def colunas():
    with open(r"C:\Users\desk\Documents\Github\programacao-I\2ª avaliação\manipulação de arquivos\datatran2020.csv", 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        print(*data[0], sep='\n')

def questao01():
    base = ler_datatran2020()
    lista = base['fase_dia']
    valores = set(lista) # criar uma coleção que não permite valores duplicados
    print(valores)

def questao02(): 
    base = ler_datatran2020()
    lista = base["fase_dia"]
    chaves = set(lista)
    bd = dict()
    for chave in chaves:
        bd[chave] = 0
        for item in lista:
            if item == chave:
                bd[chave] += 1
    print(bd)

def questao03():
    base = ler_datatran2020()
    lista = base["uf"]
    chaves = set(lista)
    bd = dict()
    for chave in chaves:
        bd[chave] = 0
        for item in lista:
            if item == chave:
                bd[chave] += 1
    print(bd)

def questao04(): 
    base = ler_datatran2020()
    lista_uf = base['uf']
    lista_mortes = base['mortos']
    mortes = 0
    for x, y in zip(lista_uf, lista_mortes):
        if x == 'PA':
            mortes += int(y)
    print(f"Mortes no estado do Pará: {mortes}")


def questao05():
    base = ler_datatran2020()
    lista_uf = base["uf"]
    lista_tipopista = base['tipo_pista']
    chaves = set(lista_uf)
    bd = dict()
    for chave in chaves:
        bd[chave] = 0
        for x, y in zip(lista_uf, lista_tipopista):
            if x == chave and y == 'Dupla':
                bd[chave] += 1
    uf_acidentes = sorted(bd.items(), key=lambda x: x[1], reverse=True) # ordenar o dicionário de acordo com os maiores valores
    ufsmaisacidentes = uf_acidentes[:3]
    for uf, acidente in ufsmaisacidentes:
        print(f'{uf}: {acidente}')

def questao06():
    base = ler_datatran2020()
    lista_ilesos = base['ilesos']
    lista_feridos = base['feridos']
    acidentes = 0
    for x, y in zip(lista_feridos, lista_ilesos):
        if int(x) > int(y):
            acidentes += 1
    print(acidentes)

def questao07():
    base = ler_datatran2020()
    lista_ufs = base["uf"]
    lista_ufsnorte = ['AC', 'AM', 'AP', 'PA', 'TO', 'RO', 'RR']
    chaves = set(lista_ufsnorte)
    bd = dict()
    for chave in chaves:
        bd[chave] = 0
        for item in lista_ufs:
            if item == chave:
                bd[chave] += 1
    with open('acidentesnorte.csv', 'w', encoding='utf-8') as resposta:
        resposta.write(f'{bd}\n')

def questao08():
    pass





    
