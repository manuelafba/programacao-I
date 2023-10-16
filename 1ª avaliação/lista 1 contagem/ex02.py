def verificar_alunos_acima_da_media(lista_notas, media):
    cont = 0
    
    for item in lista_notas:
        if item > media:
            cont += 1
    
    return cont

alunos_acima_da_media = verificar_alunos_acima_da_media([8, 8.5, 10, 7.5, 3, 5.5, 4, 3.5], 8)
print(f"{alunos_acima_da_media} alunos obtiveram notas acima da média")

def verificar_alunos_acima_da_media2(lista_notas, media):
    return sum(1 for item in lista_notas if item > media)

alunos_acima_da_media = verificar_alunos_acima_da_media2([3.5, 6, 7.5, 8, 9, 9, 5, 10, 7.5, 8], 7)
print(f"{alunos_acima_da_media} alunos obtiveram notas acima da média")