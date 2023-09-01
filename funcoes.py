def criar_lista_reversa(lista): # dois pontos sinalizam que a próxima linha será o início do escopo da função
    return lista[::-1]

def criar_lista_index_impar(lista):
    return lista[1::2]

def criar_lista_primeira_metade(lista):
    fim = len(lista)//2
    return lista[:fim]

def criar_lista_segunda_metade(lista):
    inicio = len(lista)//2
    return lista[inicio:]

def somar_lista(lista):
    total = 0
    for valor in lista:
        total = total + valor
    return total # return fora do escopo do for e dentro do escopo da função

def maior_valor_da_lista(lista):
    maior = lista[0]
    for valor in lista[1:]:
        maior = (maior + valor + abs(maior - valor))//2
    return maior
