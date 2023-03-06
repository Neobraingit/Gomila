edad = 20
nombre = 'Marcos'
if edad >= 18:
    if nombre.startswith('M') or nombre.startswith('m'):
     print ('Hola {}, tu edad es {} años, así que eres mayor de edad'.format(nombre, edad))
else:
    print ('No eres mayor de edad')