'''Hacer un programa que cuente mayusculas, minusculas, espacios y signos de puntuacion'''

import sys
def text_analyzer(texto=None):
  
    if texto is None or texto == "":
        texto = input("Introduce una cadena de texto: ")
    if not isinstance(texto, str):
        print("Error: el argumento debe ser una cadena de texto.")
        return
    num_mayus = num_minus = num_puntuacion = num_espacios = 0

    for caracter in texto:
        if caracter.isupper():
            num_mayus += 1
        elif caracter.islower():
            num_minus += 1
        elif caracter.isspace():
            num_espacios += 1
        else:
            num_puntuacion += 1
    resultado = len(texto)
    print(f"Tu texto contiene {resultado} caractere(s)")
    print("Número de mayúsculas: ", num_mayus)
    print("Número de minúsculas: ", num_minus)
    print("Número de signos de puntuación: ", num_puntuacion)
    print("Número de espacios: ", num_espacios)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        texto = " ".join(sys.argv[1:])
        text_analyzer(texto)
        print(texto)
        sys.exit
    elif len(sys.argv) < 2:
        texto = ""
        text_analyzer(texto)
        print(texto)
        sys.exit