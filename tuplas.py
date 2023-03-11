### TUPLAS ###

# Pueden contener distintos tipos de datos
# No pueden mutar
# Van entre paréntesis aunque se pueden declarar sin ellos
# Para convertir algo a tupla usamos la función tuple()

tupla = (1,2,3,4,'Marcos')
print (tupla)

# Elementos de una tupla

# Accedemos a los elementos usando slicing

coches  = ('Renault', 'Toyota', 'Opel')
print (coches[0])
print (coches[0:3]) # El índice a la derecha de los dos puntos nunca será incluido

if 'Toyota' in coches:
    print (True)
    
# Unpacking

