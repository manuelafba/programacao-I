# [x for x: colecao if filtro(x)]
# x = mapeamento
# for x: colecao = iteracao
# if filtro(x) = filtro (opcional)
lista = ['a', 'b', 'c']
lista_abc = [item.upper() for item in lista]
print(lista_abc)

def construir_lista_palindromo(lista):
    return [x for x, y in zip(lista, lista[:-1]) if x == y] # Se x e y forem iguais, para cada x e y, adicione x na lista

def mapear_listas(lista1, lista2, lista3):
    return [max(item)+min(item) for item in zip(lista1, lista2, lista3)] # Não tem a terceira parte pois não precisa de filtro

def mapear_inteiro(item):
    import math as m
    x1 = str(item)
    idx = x1.index('.') 
    x2 = int(x1[idx+1:]) 

    if x2 % 2 == 0: 
        return m.floor(item)
    else:
        return m.ceil(item)
    
def transformar_real_inteiro(lista): 
    """
    Construir uma lista de números inteiros a partir de uma lista de números reais, considerando a seguinte regra: Se o valor decimal for par, obtenha um número inteiro que seja o maior inteiro menor que o número real em análise. Se o valor decimal for ímpar, obtenha um número inteiro que seja o menor inteiro maior que o número real em análise
    Argumento: lista: uma lista de números reais
    Retorno: uma lista de números inteiros
    """
    return [mapear_inteiro(item) for item in lista]

def calcular_tamanho_nomes(lista):
    return [len(item) for item in lista]
