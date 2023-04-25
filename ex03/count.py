
import sys

def text_analyzer(texto):
    """
    Esta funcion analiza tu texto permitiendote saber 
    el numero de mayusculas, minusculas, espacios y 
    simbolos que contiene. Introduce un texto.
    """

    if texto is None:
        print("No has introducido nada")
    else:
        print(texto)
        if isinstance(texto, str):
            
            num_mayus = 0
            num_minus = 0
            num_espacios = 0
            simbolos = 0

            try:
                for letra in texto:
                    if letra.isupper():
                        num_mayus += 1
                    elif letra.islower():
                        num_minus += 1
                    elif letra.isspace():
                        num_espacios += 1
                    else:
                        simbolos += 1
                        
            except ValueError:
                print("Error fatal")

            print("El texto contiene:")
            print(f"Numero de mayusculas: {num_mayus}")
            print(f"Numero de minusculas: {num_minus}")
            print(f"Numero de espacios: {num_espacios}")
            print(f"Numero de simbolos: {simbolos}")

        else: 
            print(text_analyzer.__doc__)

if __name__ == '__main__':
    text_analyzer()

