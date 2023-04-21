
#############

# PYTHON WHILE LOOPS

#############

# THE WHILE LOOP
'''
i = 1
while i < 900000: # Se traduce como 'mientras que'. Mientras que 1 sea menor de 90000...
  print(i)
  i += 1 # Ponemos un incremento porque si no el loop continuaria hasta el infinito
'''

# THE BREAK STATEMENT
'''
i = 1
while i < 30000:
  print(i)
  if i == 25000:
    break # Para cuando llegue a 25k
  i += 1 # Suma uno
'''

# THE CONTINUE STATEMENT
'''
i = 1
while i < 30000:
    i += 1
    if i == 29998:
        continue # Se salta el 29998
    print(i)

'''
# THE ELSE STATEMENT
'''
i = 1
while i < 30000:
    print(i)
    i += 1
else:
    print('Gaaaay, te has pasadoooooo') # Si no se cumple lo de arriba, pasa esto
'''

# EJEMPLO 
respuesta = int(input('Cuantas lunas tiene Jupiter: '))
print(type(respuesta))

while respuesta != 79:
    respuesta = int(input('Respuesta Equivocada. Prueba otra vez: '))
print('Enhorabuena maricons.')