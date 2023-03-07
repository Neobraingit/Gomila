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







