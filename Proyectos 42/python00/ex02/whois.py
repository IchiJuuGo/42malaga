
# EX02 / WHOIS.PY #

'''Hacer un programa que utilice un numero como argumento, compruebe si es par
impar o 0 e imprima el resultado'''

'''Si se introducen mas de un argumento, o el argumento no es un entero,
que imprima un mensaje de error. Si no se introduce ning'un argumento,
que no haga nada o que printe la forma de uso'''

import sys

try:
    converted_arg = int(sys.argv[1]) # Convertimos el arg en un numero entero
    if len(sys.argv) > 2:
        print('Has introducido mas de un argumento')
    else:
        suuji = int(sys.argv[1])
        try:
            if suuji == 0:
                print('Soy cero')
            elif suuji % 2 == 0:
                print('Soy par')
            else:
                print('Soy impar')
        except Exception:
            print("Ha ocurrido un error")
except Exception:
    print("El argumento no es un numero entero")
