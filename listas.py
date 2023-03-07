### LISTAS ###

# Las listas son heterogéneas y sus elementos pueden ser modificados y van entre corchetes

list = ['Marcos', 'Eva', 48, 44] # Pueden tener diferentes tipos de datos
print (list)
print (len(list)) # Nos dice la longitud de la lista
print (type(list)) # Nos dice el tipo de dato que es

# Elementos de una lista: cada elemento tiene su propio índice

nombres = ['Marcos', 'Eva', 'David', 'Marta']
print (nombres[1]) # Accedemos al índice número uno
print (nombres[0]) # Accedemos al índice número cero
print (nombres[-1]) # Accedemos al último índice de la lista
print (nombres[0:3]) # Accedemos a la colección de elementos indicada

# Si intentamos acceder a un índice que no existe Python nos devolverá un error

# Ademnás de acceder a los índices, podremos modificarlos 

nombres[0] = 'Mamá' # Modificamos el primer elemento usando su índice
print (nombres)
nombres.append('Alfredo') # Con .append() añadimos un elemento nuevo al final de la lista
print(nombres)
nombres.insert(2,'Benigno') # Con .insert() añdimos el elemento en el índice que queramos; solo tenemos que indicarlo
print (nombres)

# Bucles con listas

for i in range (len(nombres)): # Imprimimos todos los valores de una lista usando sus índices
    print (nombres[i])

# También se puede hacer así:

for i in nombres:
    print (i)
    

# Concatenación y repetición de listas

lista1 = ['Perro', 'Gato', 'Canario']
lista2 = ['León', 'Guepardo', 'Jirafa']
print (lista1 + lista2) # Aquí vemos como se concatenan dos listas dando como resultado una lista que contiene los items de las dos

print (lista2 * 3) # Aquí hacemos repetición de listas

# Más métodos de listas

print (lista1.count('Perro')) # Cuenta la cantidad de veces que aparece el elemtno indicado
lista1.extend('Pantera') # Añade un elemento iterable
print (lista1)
print (lista1.index('Perro')) # Nos muestra el índice donde aparece el valor que le metamos
lista1.pop() # Borra el último de la lista
print (lista1)
lista1.remove('Perro') # Borra el elemento pasado en su primera aparición
print (lista1)
lista1.sort() # Devuelve la lista ordenada
print (lista1)
lista1.reverse() # Nos devuelve la lista en orden inverso
print (lista1)


# Conversión a listas: para convertir un objeto a una lista hay que usar list()

print (list(range(0, 100, 10))) # Da error porque tenemos una lista llamada list más arriba, pero es así

# Listas anidadas













