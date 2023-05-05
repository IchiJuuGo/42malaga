'''import qrcode_terminal
import argparse
import hashlib
import struct
import hmac
import time
import re
import os

from cripta import Cripta as AES

def leer_argumentos():
    analizador = inicializar_analizador()
    return analizador.g, analizador.k, analizador.qr

def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str)
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str)
    analizador.add_argument(
        "-qr",
        metavar="fichero",
        help="muestra un QR con la clave secreta.",
        type=str)

    return analizador.parse_args()

def validar_fichero(fichero):
    global clave
    if not (os.path.isfile(fichero) or os.access(fichero, os.R_OK)):
        print("Error: El fichero no existe o no es legible.")
        return False
    with open(fichero, "r") as f:
        clave = f.read()
    if not re.match(r'^[0-9a-fA-F]{64,}$', clave):
        print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
        return False
    return True

def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack('>I', hash_b[offset:offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado, qr = leer_argumentos()
    if fichero_clave_compartida:
        if validar_fichero(fichero_clave_compartida): 
            with open("ft_otp.key", "w") as f:
                f.write(clave)
            print("Clave almacenada en 'ft_otp.key'.")
            AES().cifrar_fichero("ft_otp.key")
            print("Fichero 'ft_otp.key' cifrado con contraseña.")
        else:
            exit(1)

    elif fichero_cifrado or qr:
        fichero = fichero_cifrado if fichero_cifrado else qr
        if not (os.path.isfile(fichero) or os.access(fichero, os.R_OK)):
            print("Error: El fichero no existe o no es legible.")
            exit(1)
        else:
            clave = AES().leer_fichero(fichero)
            if fichero_cifrado:
                print("Código generado:", generar_OTP(clave))
            else:
                print("QR con la clave secreta:")
                qrcode_terminal.draw(clave)
    else:
        print("No se ha especificado ninguna opción.")
        exit(1)
'''

'''
# &&&&&&&&&&&&&&&&&&

import argparse
import hashlib
import struct
import hmac
import time
import re
import os

from cripta import Cripta as AES

def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k, argumentos.qr

def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str)
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str)
    analizador.add_argument(
        "-qr",
        metavar="fichero",
        help="muestra un QR con la clave secreta.",
        type=str)

    return analizador

def validar_argumentos(argumentos):
    if not any([argumentos.g, argumentos.k, argumentos.qr]):
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    if argumentos.k and not validar_fichero(argumentos.k):
        return False
    if argumentos.qr and not (os.path.isfile(argumentos.qr) and os.access(argumentos.qr, os.R_OK)):
        print("Error: El fichero no existe o no es legible.")
        return False
    return True

def validar_fichero(fichero):
    global clave
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r'^[0-9a-fA-F]{64,}$', clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except IOError:
        print("Error: El fichero no existe o no es legible.")
        return False

def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack('>I', hash_b[offset:offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado, qr = leer_argumentos()
    if fichero_clave_compartida:
        if validar_fichero(fichero_clave_compartida): 
            with open("ft_otp.key", "w") as f:
                f.write(clave)
            print("Clave almacenada en 'ft_otp.key'.")
            AES().cifrar_fichero("ft_otp.key")
            print("Fichero 'ft_otp.key' cifrado con contraseña.")
        else:
            exit(1)

    elif fichero_cifrado or qr:
        fichero = fichero_cifrado if fichero_cifrado else qr
        if not (os.path.isfile(fichero) or os.access(fichero, os.R_OK)):
            print("Error: El fichero no existe o no es legible.")
            exit(1)
        else:
            clave = AES().leer_fichero(fichero)
            if fichero_cifrado:
                print("Código generado:", generar_OTP(clave))
            else:
                print("QR con la clave secreta:")
                qrcode_terminal.draw(clave)
    else:
        print("No se ha especificado ninguna opción.")
        exit(1)
'''
'''
# 7777777777777777



import argparse
import hashlib
import struct
import hmac
import time
import re
import os

from cripta import Cripta as AES

def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k

def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str)
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str)

    return analizador

def validar_argumentos(argumentos):
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else
    if not any([argumentos.g, argumentos.k]):
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    if argumentos.k and not validar_fichero(argumentos.k):
        return False
    return True

def validar_fichero(fichero):
    global clave
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r'^[0-9a-fA-F]{64,}$', clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except IOError:
        print("Error: El fichero no existe o no es legible.")
        return False

def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack('>I', hash_b[offset:offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado = leer_argumentos()
    if fichero_clave_compartida:
        if validar_fichero(fichero_clave_compartida): 
            with open("ft_otp.key", "w") as f:
                f.write(clave)
            print("Clave almacenada en 'ft_otp.key'.")
            AES().cifrar_fichero("ft_otp.key")
            print("Fichero 'ft_otp.key' cifrado con contraseña.")
        else:
            exit(1)

    elif fichero_cifrado:
        if not (os.path.isfile(fichero_cifrado) or os.access(fichero_cifrado, os.R_OK)):
            print("Error: El fichero no existe o no es legible.")
            exit(1)
        else:
            clave = AES().leer_fichero(fichero_cifrado)
            print("Código generado:", generar_OTP(clave))
    else:
        print("No se ha especificado ninguna opción.")
'''
'''
import argparse
import hashlib
import hmac
import os
import re
import struct
import time

from cripta import Cripta as AES


def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k


def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str,
    )
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str,
    )

    return analizador


def validar_argumentos(argumentos):
    if not argumentos.g and not argumentos.k:
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    return bool(not argumentos.k or validar_fichero(argumentos.k))


def validar_fichero(fichero):
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r"^[0-9a-fA-F]{64,}$", clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except FileNotFoundError:
        print("Error: El fichero no existe o no es legible.")
        return False


def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack(">I", hash_b[offset : offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)


if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado = leer_argumentos()
    if fichero_clave_compartida:
        if validar_fichero(fichero_clave_compartida):
            with open("ft_otp.key", "w") as f:
                f.write(clave)
            print("Clave almacenada en 'ft_otp.key'.")
            AES().cifrar_fichero("ft_otp.key")
            print("Fichero 'ft_otp.key' cifrado con contraseña.")
        else:
            exit(1)

    elif fichero_cifrado:
        if not (os.path.isfile(fichero_cifrado) and os.access(fichero_cifrado, os.R_OK)):
            print("Error: El fichero no existe o no es legible.")
            exit(1)
        else:
            clave = AES().leer_fichero(fichero_cifrado)
            print("Código generado:", generar_OTP(clave))
    else:
        print("No se ha especificado ninguna opción.")




'''

'''

import argparse
import base64
import hashlib
import hmac
import os
import re
import struct
import time

from cryptography.fernet import Fernet


def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k


def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str,
    )
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str,
    )

    return analizador


def validar_argumentos(argumentos):
    if not argumentos.g and not argumentos.k:
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    return bool(not argumentos.k or validar_fichero(argumentos.k))


def validar_fichero(fichero):
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r"^[0-9a-fA-F]{64,}$", clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except FileNotFoundError:
        print("Error: El fichero no existe o no es legible.")
        return False


def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack(">I", hash_b[offset : offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado = leer_argumentos()
    if fichero_clave_compartida:
        if validar_fichero(fichero_clave_compartida):
            with open("ft_otp.key", "w") as f:
                f.write(clave)
            print("Clave almacenada en 'ft_otp.key'.")
            # Generar la clave Fernet a partir de la clave compartida
            clave_compartida = bytes.fromhex(clave)
            clave_fernet = base64.urlsafe_b64encode(clave_compartida)
            # Crear una instancia de Fernet con la clave generada
            f = Fernet(clave_fernet)
            # Cifrar el archivo ft_otp.key con la clave Fernet y escribir el resultado en ft_otp.key.encrypted
            with open("ft_otp.key", "rb") as f_original:
                contenido = f_original.read()
            contenido_cifrado = f.encrypt(contenido)
            with open("ft_otp.key.encrypted", "wb")
 with open("ft_otp.key.encrypted", "wb") as f_cifrado:
            f_cifrado.write(contenido_cifrado)
        print("Fichero 'ft_otp.key' cifrado con contraseña.")
    else:
        exit(1)

elif fichero_cifrado:
    if not (os.path.isfile(fichero_cifrado) and os.access(fichero_cifrado, os.R_OK)):
        print("Error: El fichero no existe o no es legible.")
        exit(1)
    else:
        with open(fichero_cifrado, "rb") as f_cifrado:
            contenido_cifrado = f_cifrado.read()
        # Leer la clave Fernet del usuario y decodificarla
        clave_fernet_usuario = input("Introduzca la clave de cifrado: ")
        clave_fernet_usuario_bytes = clave_fernet_usuario.encode()
        # Crear una instancia de Fernet con la clave introducida
        f = Fernet(clave_fernet_usuario_bytes)
        # Descifrar el archivo y mostrar el resultado
        contenido_descifrado = f.decrypt(contenido_cifrado)
        clave = contenido_descifrado.decode()
        print("Código generado:", generar_OTP(clave))
else:
    print("No se ha especificado ninguna opción.")'''

'''
import argparse
import base64
import hashlib
import hmac
import os
import re
import struct
import time

from cryptography.fernet import Fernet


def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k


def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Herramienta casera para generar contraseñas TOTP.",
        epilog="Ejercicio",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str,
    )
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str,
    )

    return analizador


def validar_argumentos(argumentos):
    if not argumentos.g and not argumentos.k:
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    return bool(not argumentos.k or validar_fichero(argumentos.k))


def validar_fichero(fichero):
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r"^[0-9a-fA-F]{64,}$", clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except FileNotFoundError:
        print("Error: El fichero no existe o no es legible.")
        return False


def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack(">I", hash_b[offset : offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado = leer_argumentos()
    if fichero_clave_compartida:
        if validar_fichero(fichero_clave_compartida):
            with open(fichero_clave_compartida, "r") as f:
                clave = f.read()
            with open("ft_otp.key", "w") as f:
                f.write(clave)
            print("Clave almacenada en 'ft_otp.key'.")
            # Generar la clave Fernet a partir de la clave compartida
            clave_compartida = bytes.fromhex(clave)
            clave_fernet = base64.urlsafe_b64encode(clave_compartida)
            # Crear una instancia de Fernet con la clave generada
            f = Fernet(clave_fernet)
            # Cifrar el archivo ft_otp.key con la clave Fernet y escribir el resultado en ft_otp.key.encrypted
            with open("ft_otp.key", "rb") as f_original:
                contenido = f_original.read()
            contenido_cifrado = f.encrypt(contenido)
            with open("ft_otp.key.encrypted", "wb") as f_cifrado:
                f_cifrado.write(contenido_cifrado)
            print("Clave cifrada y almacenada en 'ft_otp.key.encrypted'.")
    if fichero_cifrado:
        if validar_fichero(fichero_cifrado):
            with open(fichero_cifrado, "rb") as f:
                contenido_cifrado = f.read()
            # Leer la clave Fernet desde el archivo ft_otp.key
            with open("ft_otp.key", "r") as f:
                clave = f.read()
            clave_compartida = base64.urlsafe_b64encode(bytes.fromhex(clave))
            # Crear una instancia de Fernet con la clave generada
            f = Fernet(clave_compartida)
            # Descifrar el archivo ft_otp.key.encrypted y escribir el resultado en ft_otp.key.decrypted
            contenido_descifrado = f.decrypt(contenido_cifrado)
            with open("ft_otp.key.decrypted", "wb") as f_descifrado:
                f_descifrado.write(contenido_descifrado)
            print("Clave descifrada y almacenada en 'ft_otp.key.decrypted'.")


'''
'''import argparse
import base64
import hashlib
import hmac
import os
import re
import struct
import time

from cryptography.fernet import Fernet


def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k

def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Generador de contraseñas TOTP.",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str,
    )
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str,
    )
    return analizador

def validar_argumentos(argumentos):
    if not argumentos.g and not argumentos.k:
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    return bool(not argumentos.k or validar_fichero(argumentos.k))

def validar_fichero(fichero):
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r"^[0-9a-fA-F]{64,}$", clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except FileNotFoundError:
        print("Error: El fichero no existe o no es legible.")
        return False

def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack(">I", hash_b[offset : offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado = leer_argumentos()
    if fichero_clave_compartida and validar_fichero(fichero_clave_compartida):
        with open(fichero_clave_compartida, "r") as f:
            clave = f.read()
        with open("ft_otp.key", "w") as f:
            f.write(clave)
        print("Clave almacenada en 'ft_otp.key'.")
        # Generar la clave Fernet a partir de la clave compartida
        clave_compartida = bytes.fromhex(clave)
        clave_fernet = base64.urlsafe_b64encode(clave_compartida)
        # Crear una instancia de Fernet con la clave generada
        f = Fernet(clave_fernet)
        # Cifrar el archivo ft_otp.key con la clave Fernet y escribir el resultado en ft_otp.key.encrypted
        with open("ft_otp.key", "rb") as f_original:
            contenido = f_original.read()
        contenido_cifrado = f.encrypt(contenido)
        with open("ft_otp.key.encrypted", "wb") as f_cifrado:
            f_cifrado.write(contenido_cifrado)
        print("Clave cifrada y almacenada en 'ft_otp.key.encrypted'.")
    if fichero_cifrado and validar_fichero(fichero_cifrado):
        with open(fichero_cifrado, "rb") as f:
            contenido_cifrado = f.read()
        # Leer la clave Fernet desde el archivo ft_otp.key
        with open("ft_otp.key", "r") as f:
            clave = f.read()
        clave_compartida = base64.urlsafe_b64encode(bytes.fromhex(clave))
        # Crear una instancia de Fernet con la clave generada
        f = Fernet(clave_compartida)
        # Descifrar el archivo ft_otp.key.encrypted y escribir el resultado en ft_otp.key.decrypted
        contenido_descifrado = f.decrypt(contenido_cifrado)
        with open("ft_otp.key.decrypted", "wb") as f_descifrado:
            f_descifrado.write(contenido_descifrado)
        print("Clave descifrada y almacenada en 'ft_otp.key.decrypted'.")

    # Generar OTP si se especificó un archivo de clave
    if fichero_clave_compartida is not None:
        clave = leer_clave(fichero_clave_compartida)
        if clave is not None:
            while True:
                print(generar_OTP(clave))
                time.sleep(5)
    # Generar OTP si se especificó un archivo de clave cifrado
    elif fichero_cifrado is not None:
        clave_descifrada = descifrar_clave(fichero_cifrado)
        if clave_descifrada is not None:
            while True:
                print(generar_OTP(clave_descifrada))
                time.sleep(5)

'''

import argparse
import base64
import hashlib
import hmac
import re
import struct
import time
from cryptography.fernet import Fernet


def leer_argumentos():
    analizador = inicializar_analizador()
    argumentos = analizador.parse_args()
    if not validar_argumentos(argumentos):
        exit(1)
    return argumentos.g, argumentos.k

def inicializar_analizador():
    analizador = argparse.ArgumentParser(
        description="Generador de contraseñas TOTP.",
    )
    analizador.add_argument(
        "-g",
        metavar="fichero",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        type=str,
    )
    analizador.add_argument(
        "-k",
        metavar="fichero",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        type=str,
    )
    return analizador

def validar_argumentos(argumentos):
    if not argumentos.g and not argumentos.k:
        print("No se ha especificado ninguna opción.")
        return False
    if argumentos.g and not validar_fichero(argumentos.g):
        return False
    return not bool(argumentos.k) or validar_fichero(argumentos.k)

def validar_fichero(fichero):
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        if not re.match(r"^[0-9a-fA-F]{64,}$", clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            return False
        return True
    except FileNotFoundError:
        print("Error: El fichero no existe o no es legible.")
        return False

def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack(">I", hash_b[offset : offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

def leer_clave(fichero):
    if validar_fichero(fichero):
        with open(fichero, "r") as f:
            clave = f.read()
        return clave.strip()

def descifrar_clave(fichero):
    with open(fichero, "rb") as f:
        contenido_cifrado = f.read()
    # Leer la clave Fernet desde el archivo ft_otp.key
    clave = leer_clave("ft_otp.key")
    if clave is None:
        return None
    clave_compartida = base64.urlsafe_b64encode(bytes.fromhex(clave))
    # Crear una instancia de Fernet con la clave generada
    f = Fernet(clave_compartida)
    # Descifrar el archivo ft_otp.key.encrypted y escribir el resultado en ft_otp.key.decrypted
    contenido_descifrado = f.decrypt(contenido_cifrado)
    with open("ft_otp.key.decrypted", "wb") as f_descifrado:
        f_descifrado.write(contenido_descifrado)
    print("Clave descifrada y almacenada en 'ft_otp.key.decrypted'.")
    return leer_clave("ft_otp.key.decrypted")

if __name__ == "__main__":
    fichero_clave_compartida, fichero_cifrado = leer_argumentos()
    if fichero_clave_compartida and validar_fichero(fichero_clave_compartida):
        with open(fichero_clave_compartida, "r") as f:
            clave = f.read()
        with open("ft_otp.key", "w") as f:
            f.write(clave)
        print("Clave almacenada en 'ft_otp.key'.")
        # Generar la clave Fernet a partir de la clave compartida
        clave_compartida = bytes.fromhex(clave)
        clave_fernet = base64.urlsafe_b64encode(clave_compartida)
        # Crear una instancia de Fernet con la clave generada
        f = Fernet(clave_fernet)
        # Cifrar el archivo ft_otp.key con la clave Fernet y escribir el resultado en ft_otp.key.encrypted
        with open("ft_otp.key", "rb") as f_original:
            contenido = f_original.read()
        contenido_cifrado = f.encrypt(contenido)
        with open("ft_otp.key.encrypted", "wb") as f_cifrado:
            f_cifrado.write(contenido_cifrado)
        print("Clave cifrada y almacenada en 'ft_otp.key.encrypted'.")
    if fichero_cifrado and validar_fichero(fichero_cifrado):
        with open(fichero_cifrado, "rb") as f:
            contenido_cifrado = f.read()
        # Leer la clave Fernet desde el archivo ft_otp.key
        with open("ft_otp.key", "r") as f:
            clave = f.read()
        clave_compartida = base64.urlsafe_b64encode(bytes.fromhex(clave))
        # Crear una instancia de Fernet con la clave generada
        f = Fernet(clave_compartida)
        # Descifrar el archivo ft_otp.key.encrypted y escribir el resultado en ft_otp.key.decrypted
        contenido_descifrado = f.decrypt(contenido_cifrado)
        with open("ft_otp.key.decrypted", "wb") as f_descifrado:
            f_descifrado.write(contenido_descifrado)
        print("Clave descifrada y almacenada en 'ft_otp.key.decrypted'.")

    # Generar OTP si se especificó un archivo de clave
    if fichero_clave_compartida is not None:
        clave = leer_clave(fichero_clave_compartida)
        if clave is not None:
            while True:
                print(generar_OTP(clave))
                time.sleep(5)
    # Generar OTP si se especificó un archivo de clave cifrado
    elif fichero_cifrado is not None:
        clave_descifrada = descifrar_clave(fichero_cifrado)
        if clave_descifrada is not None:
            while True:
                print(generar_OTP(clave_descifrada))
                time.sleep(5)

