### DICCIONARIOS ###

# Se acceden a los objetos por clave y no por índice. Necesitan clave : valor.Admiten todo tipo de dato y se pueden modificar. No puede haber dos claves iguales

dic1 = {'Nombre': 'Marcos', 'Apellido': 'Carmona', 'Edad': 48}
print(dic1)

# Elementos de un diccionario

print(dic1['Nombre'])  # Esto nos devuelve el valor de la clave dada
print(dic1.keys())  #  Nos dice todas las claves del diccionario
print(dic1.values())  # Nos dice todos los valores del diccionario
dic1['Nombre'] = 'Javier'  # Cambiamos el valor de la clave Nombre
print(dic1)

# Podemos introducir datos a través de un formulario
usuario = {}
print('Introduce tu nombre: ')
usuario['Nombre'] = str(input())
print('Introduce tu edad: ')
usuario['Edad'] = int(input())
print(usuario)

# Tamaño de diccionario

print(len(usuario))  # Nos dice el tamaño de un diccionario


# Bucle y diccionarios

for i in usuario:
    print(i)

# Diccionarios y listas

# Un diccionario puede contener listas y viceversa

diccionario = {'Nombre': ['Marcos', 'Eva', 'David', 'Marta']}
print(diccionario['Nombre'])


# Más métodos de diccionarios

nombres = {'Nombre': 'Marcos', 'Apellidos': 'Carmona García', }

print(nombres.clear())  # Borra todo el diccionario

nombres2 = {'Nombre': 'Marcos', 'Apellidos': 'Carmona García', }

print(nombres2.copy())  # Devuelve una copia del diccionario original

# Devuelve como clave un iterable que le pasemos
dic3 = nombres2.fromkeys([1, 2, 3, 4], [5, 6, 7, 8])
print(dic3)

print(nombres2.get('Nombre'))  # Devuelve el valor de una clave que le pasemos

# Recibe como parámetro una clave, la elimina y devuelve su valor
print(nombres2.pop('Nombre'))

# Añadimos una clave valor o también funciona como el método .get()
print(nombres2.setdefault('z', 6))

# Actualiza el diccionario con otro diccionario que le pasemos
print(nombres2.update(dic4={'Nombre': 'David'}))

# Convertir a diccionario con dict()

l = [['x', 2], ['y', 3]]
dict(l) # Creamos un diccionario a partir de una lista que debe tener dos elementos para hacer clave y valor
print(l)


