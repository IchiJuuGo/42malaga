
# EX08 - SOS.PY #

import sys

codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".--.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}

text_codificado = ""

if len(sys.argv) == 1:
    word = input("Por favor, introduce el texto a codificar en código Morse: ")
else:
    word = " ".join(sys.argv[1:])

for c in word:
    if c != "" and c.lower() in codigo_morse:
        text_codificado += f"{codigo_morse[c.lower()]} "
    else:
        print("ERROR: No es un carácter alfanumérico.")
        sys.exit()

print(text_codificado)
