import funcoesdicionario as f # importa o arquivo em que as funções foram criadas

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
        'email': 'maria@gmail.com',
        'saldo': 56
    },
    {
        'nome': 'João',
        'email': 'joao@gmail.com',
        'saldo': 344
    }
]

saldo_medio = f.calcular_saldo_medio(cadastros)
lista_filtrada = f.filtrar_email(cadastros)

print(saldo_medio)
print(lista_filtrada)
