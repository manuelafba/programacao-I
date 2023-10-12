def calcular_alunos_por_conceito(lista_conceitos):
    conceitos = {
        'E': 0,
        'B': 0,
        'R': 0,
        'I': 0
    }

    for conceito in lista_conceitos:
        for key in conceitos:
            if conceito == key:
                conceitos[key] += 1
    return conceitos

lista_conceitos = calcular_alunos_por_conceito(['E', 'E', 'B', 'B', 'R', 'E', 'B', 'R', 'I', 'I', 'R', 'R', 'I'])
print(lista_conceitos)