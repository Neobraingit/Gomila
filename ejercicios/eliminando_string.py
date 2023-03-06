# Con un buble for, vamos a recorrer un string dado y vamos a imprimir todas menos la indicada por el usuario

s = 'Esto es un string'.lower()
letra = input('Indícame que letra no quieres imprimir: ')
for i in s:
    if i == letra:
            continue
    else:
        print (i, end = ' ')
            