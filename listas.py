import funcoes as f # importar o arquivo em que as funções foram criadas

cadastros = [ 
    {
        'nome': 'renato',
        'email': 'renato@email.com',
        'saldo': 108
    },
    {
        'nome': 'JOSé',
        'email': 'jose@email.com',
        'saldo': 1024
    },
    {
        'nome': 'mariA',
        'email': 'maria@gmail.com',
        'saldo': 56
    },
    {
        'nome': 'João',
        'email': 'joao@gmail.com',
        'saldo': 344
    }
]

lista = [1, 2, 'A', 'C', 4, 'D']
lista_reversa = f.criar_lista_reversa([2, 5, 3, 7, 9, 8])
lista_index_impar = f.criar_lista_index_impar([2, 5, 3, 7, 9, 8])
lista_primeira_metade = f.criar_lista_primeira_metade([2, 5, 3, 7, 9, 8])
lista_segunda_metade = f.criar_lista_segunda_metade([2, 5, 3, 7, 9, 8])
soma_lista = f.somar_lista([2, 5, 3, 7, 9, 8])
maior_valor_lista = f.maior_valor_da_lista([5, 9])
lista_nomes = f.filtrar_nomes(cadastros)
lista_nomes_formatados = f.formatar_nomes(lista_nomes, 'CAIXA_ALTA')

lista_nomes = ['Maria', 'José', 'Joao', 'Pedro']
lista_emails = ['maria@gmail.com', 'jose@email.com', 'joao@gmail.com', 'pedro@email.com']

cadastros = f.criar_lista_cadastros(lista_nomes, lista_emails)
print(cadastros)

lista_inteiros = f.criar_lista_inteiros([2.24, 5.16, 2.1, 3.9])
print(lista_inteiros)

print(lista_reversa)
print(lista_index_impar)
print(lista_primeira_metade)
print(lista_segunda_metade)
print(soma_lista)
print(maior_valor_lista)
print(f.filtrar_por_tipo(lista, int))
print(f.filtrar_por_tipo(lista, str))
print(f.filtrar_por_tipo(lista, float))
print(lista_nomes)
print(lista_nomes_formatados)