'''
Vamos a pedirle al usuario palabras o frases y le vamos a devolver el mismo modificado con métodos:
1) Devolver el string en mayúsculas
2) Devolver el string con todas las palabras empezando en mayúsculas
3) Devolver el string con todas las letras en minúsculas menos la tercera
4) Devolver el string en mayúsculas menos la primera y la última
5) Devolver el string donde las dos primeras letras sean sustituidas por cualquier otras
'''

string = input('Introduce un string: ')
print (string.upper())
print (string.title())
string = string[:2].lower() + string[2].upper() + string[3:].lower()
print (string)


palabra = input('Introduce una palabra: ')
palabra = palabra[0].lower() + palabra[0:(len(palabra) -1)].upper() + palabra[-1].lower()
print (palabra)

subs = 'pi'
word2 = input('Introduce una palabra y yo te las cambio por las letras {}: '.format(subs))
print (word2.replace(word2[:2], subs))




