'''import argparse
import os
import re
import struct
import time
import hmac
import hashlib
from cryptography.fernet import Fernet

def leer_argumentos():
    parser = argparse.ArgumentParser(
        prog="./ft_otp",
        description="Herramienta para generar contraseñas TOTP.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-g", metavar="fichero", help="almacena una clave cifrada en un fichero cifrado 'ft_otp.key'.", type=str)
    group.add_argument("-k", metavar="fichero", help="genera una contraseña temporal usando una clave cifrada en un fichero.", type=str)
    return parser.parse_args()
def clave_fernet():
    clave = "qOBSrgOzLbDZPW5NExTo4nbw60uvlKVN76PBzYe6YEQ="
    return clave
def generar_clave():
    clave = Fernet.generate_key()
    return clave
def guardar_clave_en_fichero(fichero, clave):
    f = Fernet(clave)
    with open(fichero, "wb") as archivo:
        archivo.write(f.encrypt(b"dummy"))
    print(f"Key was successfully saved in {fichero}.")

def cargar_clave_desde_archivo(fichero):
    if not os.path.isfile(fichero) or not os.access(fichero, os.R_OK):
        print("Error: El archivo no existe o no es legible.")
        return None
    with open(fichero, "rb") as f:
        encrypted_data = f.read()
    try:
        f = Fernet(decrypted_data)
    except Exception:
        print("Error: El archivo no es un fichero cifrado válido.")
        return None
    decrypted_data = f.decrypt(encrypted_data)
    regex = re.compile(r"^[0-9a-fA-F]{64,}$")
    if not regex.match(decrypted_data.hex()):
        print("Error: La clave no es hexadecimal de 64 caracteres.")
        return None
    return decrypted_data

def generar_OTP(clave):
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.new(clave, tiempo_b, hashlib.sha1).digest()
    offset = hash_b[19] & 15
    codigo_b = hash_b[offset:offset + 4]
    codigo = struct.unpack(">I", codigo_b)[0]
    return codigo
if __name__ == '__main__':
    args = leer_argumentos()
    if args.g:
        clave = generar_clave()
        guardar_clave_en_fichero("ft_otp.key", clave)
        print("./ft_otp -g key.txt")
        print("./ft_otp: error: key must be 64 hexadecimal characters.")
        print("./ft_otp -g key.hex")
        print("Key was successfully saved in ft_otp.key.")
    elif args.k:
        clave = cargar_clave_desde_archivo(args.k)
        if not clave:
            exit(1)
        otp = generar_OTP(clave)
        print(f"La contraseña temporal es: {otp}")
    else:
        exit(1)
'''

# 77777777777777777777

import argparse
import os
import re
import struct
import time
import hmac
import hashlib
from cryptography.fernet import Fernet

def leer_argumentos():
    parser = argparse.ArgumentParser(
        prog="./ft_otp",
        description="Herramienta para generar contraseñas TOTP.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-g", metavar="fichero", help="almacena una clave cifrada en un fichero cifrado 'ft_otp.key'.", type=str)
    group.add_argument("-k", metavar="fichero", help="genera una contraseña temporal usando una clave cifrada en un fichero.", type=str)
    return parser.parse_args()

def clave_fernet():
    clave = "qOBSrgOzLbDZPW5NExTo4nbw60uvlKVN76PBzYe6YEQ="
    return clave

def generar_clave():
    clave = Fernet.generate_key()
    return clave

def guardar_clave_en_fichero(fichero, clave):
    f = Fernet(clave)
    with open(fichero, "wb") as archivo:
        archivo.write(f.encrypt(b"dummy"))
    print(f"Key was successfully saved in {fichero}.")

def cargar_clave_desde_archivo(fichero):
    if not os.path.isfile(fichero) or not os.access(fichero, os.R_OK):
        print("Error: El archivo no existe o no es legible.")
        return None
    with open(fichero, "rb") as f:
        encrypted_data = f.read()
        print(f"Datos del archivo cifrado: {encrypted_data}")
    try:
        cargar_clave_desde_archivo.clave_fernet = Fernet.generate_key()
        f = Fernet(cargar_clave_desde_archivo.clave_fernet)
        decrypted_data = f.decrypt(encrypted_data)
        regex = re.compile(r"^[0-9a-fA-F]{64,}$")
        if not regex.match(decrypted_data.hex()):
            print("Error: La clave no es hexadecimal de 64 caracteres.")
            return None
        return decrypted_data
    except Exception:
        print("Error: El archivo no es un fichero cifrado válido.")
        return None


def generar_OTP(clave):
    tiempo = int(time.time() // 30)
    tiempo_b = struct.pack(">Q", tiempo)
    hash_b = hmac.new(clave, tiempo_b, hashlib.sha1).digest()
    offset = hash_b[19] & 15
    codigo_b = hash_b[offset:offset + 4]
    codigo = struct.unpack(">I", codigo_b)[0]
    return codigo

if __name__ == '__main__':
    args = leer_argumentos()
    if args.g:
        clave = generar_clave()
        guardar_clave_en_fichero("ft_otp.key", clave)
        print("./ft_otp -g key.txt")
        print("./ft_otp: error: key must be 64 hexadecimal characters.")
        print("./ft_otp -g key.hex")
        print("Key was successfully saved in ft_otp.key.")
    elif args.k:
        clave = cargar_clave_desde_archivo

if __name__ == '__main__':
    args = leer_argumentos()
    if args.g:
        clave = generar_clave()
        guardar_clave_en_fichero(args.g, clave)
    elif args.k:
        clave = cargar_clave_desde_archivo(args.k)
        if clave:
            codigo = generar_OTP(clave)
            print(f"Contraseña temporal: {codigo}")
