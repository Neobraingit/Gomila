### MÉTODOS PARA TRABAJAR CON STRINGS ###

s= 'Soy fan del Heavy Metal'
s = s.lower() # Convertimos el string todo a minúsculas
print (s)

s = s.upper() # Convertimos todo en mayúsculas
print (s)

print (s.count('H')) # Nos cuenta cuantas veces aparece un caracter
print (s.count('METAL')) # Nos cuenta cuantas veces aparece un string
print (s.capitalize()) # La primera letra del string se convertirá en mayúsculas
print (s.title()) # Convertirá todas las letras iniciales de cada palabra en mayúsculas
print (s.swapcase()) # Convierte las mayúsculas en minúsculas y viceversa
print (s.replace('ME', 'le')) # cambia un caracter o string por otro que le indiquemos
print (s.split('Y'))  # Rompe el string por el caracter que le indiquemos
print (s.strip()) # Elimina los espacios al principio y al final del string
print (s.rstrip()) # Elimina los espacios al final del string
print (s.lstrip()) # Elimina los espacios sobrantes al principio del string
print (s.find('Y')) # Busca el caracter o string que le indiquemos y nos dará su índice en la primera posición en la que aparece. Podemos darle parámetros para indicar donde empieza y finaliza la búsqueda (start, end)
print (s.index('HEAVY')) # Busca la primera vez en la que aparece un string o caracter
print (s.rindex('S')) # Nos busca el caracter y nos devuelve la primera y la última posición en la que fue encontrado
print (len(s)) # Nos muestra el número de caracteres de un string contando también los espacios
print (type(s)) # Nos muestra la clase de dato con el que estamos trabajando

### Input ###
# Nos sirve para que el ususario introduzca un string o un valor de tipo numérico o booleano 
print ('¿Cuál es tu grupo preferido? ')
grupo = (input())
print ('Tu grupo preferido es, {}'.format(grupo))

