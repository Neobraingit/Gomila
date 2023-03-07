# Dada una lista, le pediremos al usuario que elemento quiere eliminar y lo eliminaremos

lista = ['Perro', 'Gato', 'Jirafa', 'Tigre']
print ('Dime que elemento quieres eliminar de la lista: ')
elemento = input()
lista.remove(elemento)
print (lista)