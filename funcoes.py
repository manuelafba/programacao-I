# def, nome da função, (argumentos), dois pontos
import math as m
# ceil pra cime floor pra baixo

def criar_lista_reversa(lista): # Dois pontos sinalizam que a próxima linha será o início do escopo da função
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

def filtrar_por_tipo(lista, tipo):
    lista_filtrada = []
    for item in lista: 
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada

def filtrar_nomes(cadastros):
    lista_nomes = []
    for item in cadastros:
        lista_nomes.append(item['nome'])
    return lista_nomes

def formatar_caixa_alta(lista_nomes):
    lista_formatada = []
    for item in lista_nomes:
        lista_formatada.append(item.upper())
    return lista_formatada

def formatar_caixa_baixa(lista_nomes):
    lista_formatada = []
    for item in lista_nomes:
        lista_formatada.append(item.lower())
    return lista_formatada

def formatar_nomes(lista_nomes, opcao_formatacao):
    if opcao_formatacao == 'CAIXA_ALTA':
        return formatar_caixa_alta(lista_nomes)
    elif opcao_formatacao == 'CAIXA_BAIXA':
        return formatar_caixa_baixa(lista_nomes)
    else:
        return "O segundo argumento é inválido"

def criar_lista_cadastros(nomes, emails):
    lista_cadastros = []
    for nome, email in zip(nomes, emails): # A função zip serve para juntar duas listas em uma única lista com index correspondntes
        lista_cadastros.append({
                                'Nome': nome, 
                                'Email': email
                                })
    return lista_cadastros

def criar_lista_inteiros(lista_decimais):
    lista_inteiros = []
    for numero in lista_decimais:
        x1 = numero
        x2 = str(x1)
        idx = x2.index('.')
        x3 = x2[idx+1:]
        x4 = int(x3)
        if x4 % 2 == 0:
            lista_inteiros.append(m.floor(x1))
        else:
            lista_inteiros.append(m.ceil(x1))

    return lista_inteiros
        

#dada uma lista de numeros reais, faca um mapeamento para obter uma lista de inteiro tal que:
#se o valor decimal for par, obtenha um número inteiro que seja o maior inteiro menor que o número real em análise
#se o valor decimal for ímpar, obtenha um número inteiro que seja o menor inteiro maior que o número real em análise

#dada tres listas de numeros reais, faça um mapeamento para obter uma lista onde cada elemento seja igual a soma do maior e menor elemento de indices correspondentes das tres listas

#dada uma lista de numeros inteiros, construa a lista reversa e faça o filtro para obter somente os elementos que são iguais na lista original

#dada uma lista de string, faça uma redução para determinar o tamanho da maior string. retorne o valor encontrado, a string e o indice da lista que ela está