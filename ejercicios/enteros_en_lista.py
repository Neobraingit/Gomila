'''
Vamos a pedirle al usuario la longitud de una lista y haremnos que introduzca  por teclado tantos números enteros como haya
indicado, que se guardarán en una lista. Al acabar, imprimiremos la lista
'''
n = int(input('Introduce el tamaño de la lista: '))
l = []

for i in range(n):
    print ('Introduce un número: ')
    l.append(int(input()))
    
print ('Tu lista es: ', l)
    