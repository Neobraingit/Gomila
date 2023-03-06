s =  input('Escribe una frase: ').lower()

recorrido = 0 # Recorre la frase incrementándose abajo
vocales = 0 # Inicia el número de vocales incrementándose abajo
while recorrido < len(s):
    if s[recorrido] == 'a' or s[recorrido] == 'e' or s[recorrido] == 'i' or s[recorrido] == 'o' or s[recorrido] == 'u': # De cada string[itereacion(recorrido)]
        vocales += 1
    recorrido += 1
print ('En total hay {} vocales'.format(vocales))


        
