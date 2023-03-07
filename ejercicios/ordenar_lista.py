# Vamos a pedir al usuario que ingrese 10 números, los guardaremos en una lista y la mostraremos ordenada

l = []
for i in range(10):
    print ('Introduce un número: ')
    l.append(input())
    
l.sort()
print (l)