'''
Dado un string, con un bucle for, vamos a imprimirlo sin vocales y vamos a salir del bucle 
si la letra que indique el usuario aparece más de n veces, número que también nos proporciona el usuario
'''

s = 'Esto es un string'
letra = input('Indicame una letra: ')
numero = int(input('Indicame un número: '))
contador = 0
for i in s:
    if contador >= numero:
        print ('Se ha superado el número de apariciones')
        break
    if i == letra:
       contador += 1
    elif i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    
    print (i, end = ' ')

    