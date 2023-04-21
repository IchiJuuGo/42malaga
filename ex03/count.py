
import sys

def text_analyzer(texto):
    input("Introduce un texto para analizar: ")
    
    # num_mayus = 0
    # num_minus = 0
    # num_espacios = 0
    # num_simbolos = 0

    # print('Numero de mayusculas: ' + num_mayus)
    # print('Numero de minusculas: ' + num_minus)
    # print('Numero de espacios: ' + num_espacios)
    # print('Numero de simbolos: ' + num_simbolos )


analizar = text_analyzer (sys.argv[1])




                                                                                                                                                                                                                                                                  


#  converted_arg = str(sys.argv[1])
# import sys

# def text_analyzer(texto=None):
#     '''Introduce una cadena de texto y te devuelve el numero
#     de mayusculas, minusculas, simbolos y espacios en blancos
#     que contiene el texto'''

#     while True:
#         texto = input('Escriba un texto para ser analizado: ')
#         if isinstance(texto, str):    
#             # num_mayus = 0
#             # num_minus = 0
#             # num_espacios = 0
#             # num_simbolos = 0
 
#             # for letra in texto:
#             #     if letra.isupper():
#             #         num_mayus += 1
#             #     elif letra.islower():
#             #         num_minus += 1
#             #     elif letra.isspace():
#             #         num_espacios += 1
#             #     else:
#             #         num_simbolos += 1
#             return


    # if texto is None or texto == "": # while
    #     print('Inserta un texto') # input
    # elif not isinstance(texto, str):
    #     print('Error: tiene que ser un texto!')
    # elif isinstance(texto, str):
    #     print('Es una cadena de texto')
    #     return

    # num_mayus = 0
    # num_minus = 0
    # num_espacios = 0
    # num_simbolos = 0

    # for letra in texto:
    #     if letra.isupper():
    #         num_mayus += 1
    #     elif letra.islower():
    #         num_minus += 1
    #     elif letra.isspace():
    #         num_espacios += 1
    #     else:
    #         num_simbolos += 1
    
    # print('Numero de mayusculas: ' + num_mayus)
    # print('Numero de minusculas: ' + num_minus)
    # print('Numero de espacios: ' + num_espacios)
    # print('Numero de simbolos: ' + num_simbolos )

# print(text_analyzer.__doc__)




























# TEXT ANALYZER
# import sys
# import string

# def text_analyzer(pepe):
#     upper_count = 0
#     lower_count = 0
#     punctuation_count = 0
#     blanks_count = 0

#     for char in pepe: 
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count = 0
#         elif char in string.punctuation:
#             punctuation_count += 1
#         elif char.isspace():
#             blanks_count += 1

#     print(sys.argv[1::])

#     print('Mayusculas: ', upper_count)
#     print('Minusculas: ', lower_count)
#     print('Signos: ', punctuation_count)
#     print('Espacios: ', blanks_count)
    

# if not len(sys.argv) == 2:
#     print("Only 1 argument")
# else:
#     frase = sys.argv[1]
#text_analyzer('hola que tal ', '')


# ////////////////////////////



