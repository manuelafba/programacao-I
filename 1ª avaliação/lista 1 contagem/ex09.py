def classfifcar_softwares(lista_vulnerabilidade):
    classes = {
        "Muito seguro": 0,
        "Quase seguro": 0,
        "Inseguro": 0,
        "Muito inseguro": 0
    }

    for vulnerabilidade in lista_vulnerabilidade:
        if vulnerabilidade == 0:
            classes["Muito seguro"] += 1
        elif 1 <= vulnerabilidade <= 3:
            classes["Quase seguro"] += 1
        elif 4 <= vulnerabilidade <= 5:
            classes["Inseguro"] += 1
        else:
            classes["Muito inseguro"] += 1
    
    return classes

lista_softwares = classfifcar_softwares([0, 0 ,1, 3, 2, 4, 5, 6, 1, 2, 7])
print(lista_softwares)
