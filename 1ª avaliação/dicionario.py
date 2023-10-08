# não é indexado, é referenciado pelas chaves
# {chave: elemento, chave: elemento, chave: elemento} - determinada pelos dois pontos

cadastros = [ 
    {
        'nome': 'Renato',
        'email': 'renato@email.com',
        'saldo': 108
    },
    {
        'nome': 'JOSÉ',
        'email': 'jose@email.com',
        'saldo': 1024
    },
    {
        'nome': 'Maria',
        'email': 'maria@email.com',
        'saldo': 56
    }
]

print(cadastros[0]['nome']) # nome do primeiro dicionário
print(cadastros[1]['nome']) # nome do segundo dicionário
