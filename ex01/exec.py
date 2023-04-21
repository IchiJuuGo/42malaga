
''' Crear un programa que tome la cadena como argumento, le de la vuelta,
le cambie las letras de mayus a minus y viceversa y printe el resultado. '''
''''''

import sys

def programa01(string):
    vuelta = string[::-1]
    return vuelta.swapcase()

''' Si introducimos mas de un argumento, unelos en una sola linea
con cada argumento separado por un espacio. Si no se introduce ningun argumento, 
que no haga nada o que imprima su forma de uso'''

if len(sys.argv) > 1:
    string = " ".join(sys.argv[1:])
    result = programa01(string)
    print(result)

else:
    print("Introduce al menos una palabra")

# if__name__ =='__main__'

