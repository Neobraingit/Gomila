# Vamos a leer un string por teclado y vamos a devolver  un diccionario con la cantidad de apariciones de cada caracter en el string

string = input('Introduce un string')
letras = {}
contador = []

for i in string:
    if i not in contador and i != ' ':
        letras[i] = string.count(i)
        
print (letras)