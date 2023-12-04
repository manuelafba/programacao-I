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

    
