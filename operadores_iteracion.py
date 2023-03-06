### OPERADORES ITERACIÓN ###

# while

numero = 101
while numero > 0:
    numero -= 1
    print ('El número es {}'.format(numero))
    
    
numero = 1
while numero <= 10:
    print (numero)
    numero += 1
    
# Comando break: cortamos la ejecución

# Combinación while else

i = 10
while i >= 0:
    i -= 1
    print (i)
else: 
    print ('La cuenta atrás ha finalizado¡¡')
    