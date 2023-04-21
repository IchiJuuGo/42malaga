
#############

# PYTHON BOOLEANS

#############

# BOOLEAN VALUES
'''
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print('\'b\' es mayor que \'a\'')
else:
    print('\'b\' no es mayor que \'a\'')
'''

# EVALUATE VALUES AND VARIABLES
'''
print(bool('Hello')) # Evaluar una cadena
print(bool(15)) # Evaluar un numero entero

x = 'Hello'
y = 15
print(bool(x)) # Evaluar dos variables
print(bool(y))

Cosas que son true: casi todos los valores, todas las cadenas excepto las vacias, cualquier numero excepto 0
listas, tuplas, set y diccionarios ecepto los que estan vacios

Valores que son False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

# FUNCTIONS CAN RETURN A BOOLEAN

'''
def myFunction():
    return True
print(myFunction())
'''

'''
def myFunction():
    return False # Hacemos que la funcion nos devuelva False

if myFunction():
    print('Yes') # Nos imprime Yes si la funcion es True
else:
    print('Nope') # Nos imprime Nope si la funcion es False
'''

x = 200
print(isinstance(x, int))

