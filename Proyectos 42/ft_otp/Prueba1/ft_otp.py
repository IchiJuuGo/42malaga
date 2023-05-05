
##### OBJETIVO
"""
En este proyecto, el objetivo es implementar un sistema de TOTP 
que sea capaz de generar contraseñas efímeras a partir de una clave maestra.
Estará basado en el RFC TOTP 6238 / HOTP 4226.
En el lenguaje de tu elección, debes implementar un programa que permita:
- Registrar una clave inicial
- Que sea capaz de generar una nueva contraseña cada vez que se solicite. 
"""

##### FUNCIONALIDADES
"""
- El programa deberá llamarse ft_otp.
- Con la opción -g, el programa recibirá como argumento 
una clave hexadecimal de al menos 64 caracteres. 
El programa guardará a buen recaudo esta clave en un archivo
llamado ft_otp.key, que estará cifrado en todo momento.
- Con la opción -k, el programa generará una nueva contraseña temporal
y la mostrará en la salida estándar
"""

##### LIBRERIAS
"""
Puedes utilizar cualquier librería que facilite la implementación del algoritmo, 
siempre que no hagan el trabajo sucio, es decir, 
queda terminantemente prohibido hacer uso de cualquier librería TOTP. 
Por supuesto, puedes y debes hacer uso de alguna librería o función que te permita 
acceder al tiempo del sistema.
"""

import hmac
import base64
import struct
import hashlib
import time
import argparse
import secrets
from cryptography.fernet import Fernet
import os

##### FUNCIONES DE PARSEO

def lector_argumentos():
    # Inicializar el analizador de argumentos.
    opcion = iniciar_lector()
    return opcion.g, opcion.k,

def iniciar_lector():
    # Analizador de argumentos de la línea de comandos.
    parser = argparse.ArgumentParser(
        description = "Generardor de contraseñas TOTP")
    parser.add_argument(
        "-g",
        help = "Introduce una clave hexadecimal de al menos 64 caracteres",
        type = str)
    parser.add_argument(
        "-k",
        help = "Genera una contraseña temporal",
        type = str)
    return parser.parse_args()

##### FUNCIONES TOTP
"""
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)-
    #decoding our key
    msg = struct.pack(">Q", intervals_no)
    #conversions between Python values and C structs represente
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    #Generate a hash using both of these. Hashing algorithm is HMAC
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    #unpacking
    return h

def get_totp_token(secret):
    #ensuring to give the same otp for 30 seconds
    x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
    #adding 0 in the beginning till OTP has 6 digits
    while len(x)!=6:
        x+='0'
    return x
#base64 encoded key
secret = 'MNUGC2DBGBZQ===='
print(get_totp_token(secret))
"""

def generar_clave_secreta():
    # Generamos una clave secreta aleatoria de 64 bytes y la pasamos a formato hex.
    clave_bytes = secrets.token_bytes(64)
    clave_hex = clave_bytes.hex()
    print(clave_hex)
    return clave_hex
generar_clave_secreta()

def guardar_clave_en_archivo(clave, nombre_archivo = "ft_otp.key"):
    # Guardamos la clave secreta hex generada, en un archivo cifrado para protegerla.
    # 1) Generamos una clave de cifrado aleatoria para cifrar el archivo y creamos 
    # un objeto fernet para cifrar y descifrar la clave secreta.
    clave_cifrado = Fernet.generate_key()
    fernet = Fernet(clave_cifrado)
    
    # 2) Ciframos la clave y la guardamos en un archivo
    clave_cifrada = fernet.encrypt(clave.encode())
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(clave_cifrada)
    
    # Devolvemos la clave de cifrado para poder descifrar el archivo más adelante
    return clave_cifrado
guardar_clave_en_archivo("mi_clave_secreta", "ft_otp.key")

def generar_totp(clave_secreta):
    # 1) Obtenemos el tiempo actual en segundos desde la epoca Unix,
    # lo pasamos a entero y agregamos el intervalo de 30 segundos.
    tiempo_actual = int(time.time() // 30)

    # 2) Convertimos el tiempo en intervalos en un número entero de 8 bytes (64 bits)
    # en formato big-endian (">Q") utilizando la función struct.pack().
    tiempo_en_bytes = struct.pack(">Q", tiempo_actual)

    # 3) Calculamos el HMAC-SHA1 de la clave secreta y el tiempo en intervalos. 
    # La clave secreta se decodifica de base32 a bytes utilizando la función base64.b32decode(). 
    # El resultado es el valor del digest (resumen criptográfico) de la función HMAC-SHA1.
    hmac_sha1 = hmac.new(base64.b32decode(clave_secreta), tiempo_en_bytes, hashlib.sha1).digest()

    # 4) Esta línea calcula el índice (offset) en el digest de HMAC-SHA1 
    # a partir del último byte y coje los 4 ultimos bits.
    indice = hmac_sha1[-1] & 0x0F

    # 5) En esta línea se extraen 4 bytes del digest de HMAC-SHA1 a partir del índice 
    # calculado anteriormente y se convierten a un número entero. Se enmascara 
    # el resultado para obtener los 31 bits más significativos del número.
    # Luego hacemos modulo de 1000000 para que el resultado tenga 6 dígitos.
    codigo_otp = struct.unpack(">I", hmac_sha1[indice:indice+4])[0]
    codigo_otp = (codigo_otp & 0x7FFFFFFF) % 1000000



##### FUNCION MAIN

##### EJECUTAMOS COMO PROGRAMA PRINCIPAL

# if __name__ == "__main__":
#     lector_argumentos()
