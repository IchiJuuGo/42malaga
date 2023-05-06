
# EX04 / OPERATIONS.PY #

'''Esta funcion recoge los argumentos A y B, realiza 
las operaciones e imprime los resultados:'''

import sys

def calculadora(A, B):

    Sum = A + B
    Difference = A - B
    Product = A * B

    # Si las operaciones no se pueden realizar,
    # imprimen el error de calculo:

    Quotient = "ERROR: division por cero" if B == 0 else A / B
    Remainder = "ERROR: modulo por cero" if B == 0 else A % B 

    print('Suma: ', Sum)
    print('Resta: ', Difference)
    print('Producto: ', Product)
    print('Division: ', Quotient)
    print('Modulo: ', Remainder)
    
'''Si no se introduce ningun argumento, 
nos imprime la forma de uso y cierra el programa:'''

if len(sys.argv) == 1:
    print("Debes introducir dos numeros enteros")
    exit()

'''Si la longitud de los argumentos es diferente
a 3 o si los argumentos no son enteros,
nos muestre un mensaje de error:'''

if len(sys.argv) != 3:
    print("Introduce \"dos\" numeros enteros")
else:
    try:
        numero1 = int(sys.argv[1])
        numero2 = int(sys.argv[2])

        numeros = calculadora (numero1, numero2)
    except ValueError:
        print("Solo acepto numeros enteros")
    