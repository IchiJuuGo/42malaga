
# EX05 - KATA01 #

'''
The kata variable is always a dictionary 
and can only be filled with strings.
'''

# Escribir un programa que imprima los elementos del 
# diccionario con el formato indicado en el ejercicio.

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for value, name in kata.items():
    print(f"{value}, was created by {name}")

# Creamos un bucle con dos variables correspondientes
# a la primera y segunda posicion del diccionario y con f-string 
# le damos formato dentro de la cadena