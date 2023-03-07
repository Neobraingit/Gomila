### DICCIONARIOS ###

# Se acceden a los objetos por clave y no por índice. Necesitan clave : valor.Admiten todo tipo de dato y se pueden modificar. No puede haber dos claves iguales

dic1 = {'Nombre' : 'Marcos', 'Apellido' : 'Carmona', 'Edad' : 48}
print (dic1)

# Elementos de un diccionario

print (dic1['Nombre']) # Esto nos devuelve el valor de la clave dada
print (dic1.keys()) # Nos dice todas las claves del diccionario
print (dic1.values()) # Nos dice todos los valores del diccionario
dic1['Nombre'] = 'Javier' # Cambiamos el valor de la clave Nombre
print (dic1)

# Podemos introducir datos a través de un formulario
usuario = {}
print ('Introduce tu nombre: ')
usuario['Nombre'] = str(input())
print ('Introduce tu edad: ')
usuario['Edad'] = int(input())
print (usuario)

# Tamaño de diccionario

print (len(usuario)) # Nos dice el tamaño de un diccionario


# Bucle y diccionarios

for i in usuario:
    print (i)
    
# Diccionarios y listas

# Un diccionario puede contener listas y viceversa

diccionario = {'Nombre' : ['Marcos', 'Eva', 'David', 'Marta']}
print (diccionario['Nombre'])


# Más métodos de diccionarios

