

# cosas = ('hola', 'gay', 'suricata', 'globo', 'pantufla')
# for pepe in cosas:

# # INPUT
'''
respuesta = input('Introduce un texto para analizar: ')
while not isinstance(respuesta, str):
    respuesta = input('Error. Introduce un texto: ')
print('Tu texto es una caca')

'''

# FUNCION PARA SACAR LA NOTA MEDIA DE 3 ALUMNOS
'''
def calc_media(alumno1, alumno2, alumno3):
    suma = alumno1 + alumno2 + alumno3
    return suma / 3

media = calc_media(5, 6, 7.5) 
print("La puntuacion de la clase media es:", media)
'''

# FUNCION PARA SACAR LA NOTA MEDIA DE LOS ALUMNOS QUE SEA
'''
def notas(clase):
    return sum(clase) / len(clase)

clase = [7, 8, 9, 6.5, 8]
media = notas(clase)
print("La nota media de esta clase es: ", media)

clase = [7, 8, 9]
media = notas(clase)
print("La nota media de esta clase es: ", media)
'''

# FUNCION TABLA DE MULTIPLICAR
'''
numero = 2565

def mostrar_linea(num, linea):
    print(num, 'x', linea, '=', num * linea )

mostrar_linea(numero, 1)
mostrar_linea(numero, 2)
mostrar_linea(numero, 3)
mostrar_linea(numero, 4)
mostrar_linea(numero, 5)
mostrar_linea(numero, 6)
mostrar_linea(numero, 7)
mostrar_linea(numero, 8)
mostrar_linea(numero, 9)
mostrar_linea(numero, 10)
'''

# TUPLAS
'''
tupla1 = ('gay', 'lesbiana', 'no-binarie')
longitud = len(tupla1)

print ("En esta tupla hay", longitud, "elementos:")
print(tupla1)
'''
# F-STRINGS
'''
lenguaje = "Python"
escuela = "freeCodeCamp"
print("Estoy aprendiendo", lenguaje, "en", escuela,".")

lenguaje1 = "Python"
escuela1 = "freeCodeCamp"
print(f"Estoy aprendiendo {lenguaje1} en {escuela1}.")'''

# DICTIONARY
# diccionario = {
#     "Edad": "Cienes y cienes",
#     "Sexo": "Escaso",
#     "Rol": "Dungeons and Dragons",
#     "Sinceridad": True
# }

import argparse

def sumar_numeros(a, b):
    return a + b

if __name__ == '__main__':
    # Crear un objeto analizador de argumentos
    parser = argparse.ArgumentParser(description='Suma dos números.')

    # Agregar los argumentos de la línea de comandos
    parser.add_argument('numero1', type=int, help='El primer número a sumar.')
    parser.add_argument('numero2', type=int, help='El segundo número a sumar.')

    # Analizar los argumentos de la línea de comandos
    args = parser.parse_args()

    # Realizar la suma
    resultado = sumar_numeros(args.numero1, args.numero2)

    # Mostrar el resultado
    print(f'La suma de {args.numero1} y {args.numero2} es {resultado}.')