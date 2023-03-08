# Dado un diccionario, vamos a solicitar al usuario una clave que quiera eliminar y vamos a eliminarla. Mostraremos el diccionario actualizado

diccionario = {'Nombre' : 'Marcos', 'Apellidos' : 'Carmona García', 'edad' : 48}

print ('Dime la clave que quieres eliminar: ')
clave = input()

diccionario.pop(clave)
print (diccionario)