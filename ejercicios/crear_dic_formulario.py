# Vamos a hacer que el usuario rellene una ficha de cliente  y crearemos un diccionario. Pediremos: nombre, apellidos, edad, dni
cliente = {}
print ('Dime tu nombre: ')
cliente['Nombre'] = str(input())
print ('Dime tus apellidos: ')
cliente['Apellidos'] = str(input())
print ('Dime tu edad: ')
cliente['Edad'] = int(input())
print ('Dime tu DNI')
cliente['DNI'] = str(input())

print (cliente)