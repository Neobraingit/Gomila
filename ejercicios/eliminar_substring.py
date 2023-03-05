''' Dado un string, vamos a pedir al usuario que introduzca una palabra perteneciente a dicho string y vamos a obtener el
substring sin la palabra indicada usando el método .find() y la función .len()'''

string = 'El camino está cerrado pero seguro que podemos encontrar una alternativa'
print ('Este el string original: ', end= '')
print (string)

print ('Introduce la palabra que quieres eliminar: ')
palabra = input('Palabra: ')

idx = string.find(palabra)
substring = string[:idx] + string[idx + len(palabra):]
print (substring)