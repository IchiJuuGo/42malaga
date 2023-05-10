
# FT_OTP / GENERADOR DE PASSWORD TOTP #

import argparse
import base64
import hashlib
import hmac
import re
import struct
import time
import qrcode
from cryptography.fernet import Fernet

# FUNCIONES DEL PROGRAMA #
# Debajo de cada funcion encontraras la descripcion con la tarea que realiza

def validar_fichero(clave):
        if not re.match(r'^[0-9a-fA-F]{64,}$', clave):
            print("La clave no es hexadecimal o tiene menos de 64 caracteres.")
            exit()

# Validamos si la clave es hexadecimal y tiene 64 o mas caracteres.

def generar_OTP(clave):
    clave_b = bytes.fromhex(clave)
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.digest(clave_b, tiempo_b, hashlib.sha1)
    offset = hash_b[19] & 15
    codigo = struct.unpack(">I", hash_b[offset : offset + 4])[0]
    codigo = (codigo & 0x7FFFFFFF) % 1000000
    return "{:06d}".format(codigo)

# Generamos una pass OTP usando la clave hexadecimal.
# La función calcula el hash de la clave + el tiempo actual. 
# Luego, obtenemos un código de 6 dígitos.

def leer_clave(fichero):
    try:
        with open(fichero, "r") as f:
            clave = f.read()
        return clave.strip()
    except Exception as e:
        print(e)
        exit()

# Esta función lee el contenido del archivo y devuelve la clave como una cadena, 
# eliminando cualquier espacio en blanco adicional.

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

# Cifra una clave utilizando la biblioteca Fernet en combinación con una clave maestra 
# generada aleatoriamente. En lugar de dejar la clave maestra aqui pegada en el codigo,
# la guardamos en un archivo llamado "jefa.key" y la clave cifrada 
# la metemos guarda en un archivo llamado "ft_otp.key". 

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

# Aqui hacemos lo contrario, desciframos la clave almacenada en el 
# archivo "ft_otp.key" utilizando la clave maestra almacenada en "jefa.key". 

def codigo_qr(texto):
    qr = qrcode.QRCode(version=1, box_size=20, border=20)
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill_color="purple", back_color="white")
    img.show()

# Con esta funcion, hacemos que se genere un codigo QR 
# con el numero que hemos generado con la clave maestra

def main():
    analizador = argparse.ArgumentParser(
        description="Generador de contraseñas TOTP.",
    )
    analizador.add_argument(
        "-g",
        help="Almacena una clave hexadecimal encriptada en el fichero \"ft_otp.key\".",
        action='store_true',
    )
    analizador.add_argument(
        "-k",
        help="Genera una contraseña temporal usando el fichero \"ft_otp.key\".",
        action='store_true',
    )
    analizador.add_argument(
        "fichero",
        type=str,
    )
    analizador.add_argument(
        "-q",
        help="Genera un código QR de la contraseña temporal.",
        action='store_true',
    )
    argumentos = analizador.parse_args()
    if not argumentos.g and not argumentos.k and not argumentos.q:
        print("No se ha especificado ninguna opción.")
    if argumentos.g == True:
        clave = leer_clave(argumentos.fichero)
        validar_fichero(clave)
        encrypt(clave)
    elif argumentos.k == True:
        decrypted = descifrar_clave(argumentos.fichero)
        print(generar_OTP(decrypted))
    elif argumentos.q == True:
        decrypted = descifrar_clave(argumentos.fichero)
        otp = generar_OTP(decrypted)
        print(f"Contraseña temporal: {otp}")
        codigo_qr(otp)

# Aqui simplemente llamamos a todas las funciones paraejecutar el programa. 
# Si usamos -g, se lee una clave del archivo especificado, se valida, 
# se cifra y se guarda la clave maestra en otro archivo encriptado. 
# Si usamos -k, se descifra la clave del archivo especificado 
# y se genera un OTP utilizando esa clave.

if __name__ == "__main__":
    main()

# Y lanzamos el programa