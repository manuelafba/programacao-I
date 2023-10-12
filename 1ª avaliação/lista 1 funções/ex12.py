import math as m

def calcular_desvio_padrao(lista_reais):
    """
    Calcular o desvio padrão de uma lista de números reais

    Argumentos: lista_reais: uma lista de números reais
    
    Retorno: o desvio padrão dos números
    """
    media = sum(lista_reais) / len(lista_reais) # calcular média dos dados
    soma_diferenca_quadrados = sum((numero - media) ** 2 for numero in lista_reais) # subtrair cada valor da lista pela média, elevar ao quadrado e somar todos os valores
    divisao = soma_diferenca_quadrados / len(lista_reais) # dividir o resultado da soma pela quantidade de números
    desvio = m.sqrt(divisao) # tirar a raiz quadrada do resultado da divisão

    return desvio

desvio_padrao = calcular_desvio_padrao([2.5, 6.9, 5.3, 7.8])
print(desvio_padrao)