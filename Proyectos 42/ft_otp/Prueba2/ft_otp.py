
import argparse
import base64
import hashlib
import hmac
import re
import struct
import time
from cryptography.fernet import Fernet, InvalidToken

def validar_fichero(clave):
        if not re.match(r'^[0-9a-fA-F]{64,}$', clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            exit()

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
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        return clave.strip()
    except Exception as e:
        print(e)
        exit()

def encrypt(clave):
    clave = clave.encode()
    master = Fernet.generate_key()
    try:
        with open ("jefa.key", 'wb') as a:
            a.write(master)
    except Exception as e:
        print(e)
    claveb =  base64.urlsafe_b64encode(clave)
    f = Fernet(master)
    clave_cifrada = f.encrypt(claveb)

    try:
        with open("ft_otp.key", "wb") as f:
            f.write(clave_cifrada)
            print("Clave almacenada en 'ft_otp.key'.")
    except Exception as e:
        print(e)
        exit()

def descifrar_clave(fichero):
    try:
        with open("jefa.key", "rb") as k:
            key = k.read()
    except Exception as e:
        print(e)

    try:
        with open(fichero, "rb") as f:
            contenido_cifrado = f.read()
    except Exception as e:
        print(e)
     
    f = Fernet(key)
    contenido_descifrado = f.decrypt(contenido_cifrado)
    contenido_descifrado = base64.urlsafe_b64decode(contenido_descifrado)
    contenido_descifrado = contenido_descifrado.decode('utf-8')
    return contenido_descifrado

def main():
    analizador = argparse.ArgumentParser(
        description="Generador de contraseñas TOTP.",
    )
    analizador.add_argument(
        "-g",
        help="almacena una clave hexadecimal de 64 caracteres mínimo en un fichero 'ft_otp.key'.",
        action='store_true',
    )
    analizador.add_argument(
        "-k",
        help="genera una contraseña temporal usando un fichero y la muestra por pantalla.",
        action='store_true',
    )
    analizador.add_argument(
        "fichero",
        type=str,
    )
    argumentos = analizador.parse_args()
    if not argumentos.g and not argumentos.k:
        print("No se ha especificado ninguna opción.")
    if argumentos.g == True:
        clave = leer_clave(argumentos.fichero)
        validar_fichero(clave)
        encrypt(clave)
    elif argumentos.k == True:
        decrypted = descifrar_clave(argumentos.fichero)
        print(generar_OTP(decrypted))

if __name__ == "__main__":
    main()
               