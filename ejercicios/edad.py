# Vamos a pedirle al usuario su año de nacimiento  y el año actual y le vamos a imprimir su edad

nacimiento = int(input('Introduce tu año de nacimiento: '))
actual = int(input('Introduce el año actual: '))
edad = actual - nacimiento
print ('Tu edad es de {} años'.format(edad))