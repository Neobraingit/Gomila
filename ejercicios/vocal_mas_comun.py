frase = 'Esto es una prueba de ejercicio...'
frase = frase.lower()
letra = input('Introduce la letra a contar: ')
if letra in frase:
    print ('La frase tiene {} letras'.format(frase.count(letra)))