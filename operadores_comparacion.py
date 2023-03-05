### OPERADORES COMPARACIÓN ###

# > mayor que
# < menor que
# == igual que
# >= mayor o igual que
# <= menor o igual que
# != diferente que

# Las siguientes operaciones nos daran como resultado un valor booleano

print (7 == 7.0)
print (3.14 > 9)  # En estas 3 operaciones usamos los operadores de comparación
print (7 != '7')

# Supongamos que para entrar en una empresa tenemos que tener 16 años o más, pero menos de 40

edad = int(input('Introduce tu edad: '))
if edad > 16 and edad < 40:
    print ('Puedes acceder a la empresa...')
else:
    print ('No puedes acceder a la empresa...')
    
# Comparación de strings

print ('Mallorca' < 'Dubai') # Esto nos dará False por el orden alfabético de los strings

# Métodos de strings

# Si el string comienza por la cadena o caracter indicado nos devuelve True
cadena = 'Mi nombre es Marcso'
print (cadena.startswith('M'))  

# Si el string termina con el caracter o cadena indicado nos devuelve True
cadena2 = 'Mi edad es 48'
print (cadena2.endswith('8'))  

# Si todos los caracteres del string son alfanuméricos nos devuelve True
cadena3 = 'Mi apellido es Carmona362'
print (cadena3.isalnum()) # En este caso nos da False por que los espacios en blanco no son considerados alfanuméricos

# Si todos los caracteres pertenecen al alfabeto nos devuelve True
cadena4 = 'migatasellamaPelusa'
print (cadena4.isalpha())

# Si todos los caracteres des string son dígitos nos devuelve True
cadena5 = '123455'
print (cadena5.isdigit())

# Si todos los caracteres son espacios en blanco nos devuelve True
cadena6 = '    '
print (cadena6.isspace())

# Si todos los caracteres son minúscula nos devuelve True
cadena7 = 'migatasellamadune'
print (cadena7.islower())

# Si todos los caracteres son mayúsculas nos devuelve True
cadena8 = 'MELLAMOMARCOS'
print (cadena8.isupper())

# Si los caracteres empiezan todos en mayúsculas nos devuelve True
cadena9 = 'Me Llamo Marcos'
print (cadena9.istitle())