# Vamos a convertir  los números impares del 0 al 30 en una lista y mostrar con el formato 'El valor {} ocupa el índice {}

lista = list(range(1, 30, 2))
for i in range(len(lista)):
    print ('El valor {} ocupa el índice {}'.format (lista[i], i))
    