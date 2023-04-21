
#############

# STRINGS

#############

# STRINGS ARE ARRAYS
'''
a = "Hello, World!"
print(a[1]) # Printa la letra e
'''

# LOOPING THROUGH A STRING
'''
for x in 'banana':
    print(x) # Printa la palabra banana, una letra por fila
'''

# STRING LENGHT
'''
a = 'Hello world'
print(len(a)) # Printa la longitud de la cadena
'''

# CHECK STRING
'''
 # Con in
txt = "The best things in life are free!"
print("free" in txt)

 # Con if
txt = "The best things in life are free!"
if "free" in txt:
    print('Yes, free is present')
'''

# CHECK IF NOT
'''
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = 'The best things in life are free!'
if 'expensive' not in txt:
    print('No, expensive is NOT present')
'''

# SLICING
'''
b = 'Hello World!'
print(b[2:5]) # Printa el trozo seleccionado
print(b[:5]) # Printa desde el principio a la posicion 5
print(b[2:]) # Printa desde la posicion 2 al final
print(b[-5:-2]) # Al ponerlo en negativo, empieza contando por el final
'''

# MODIFY STRINGS
'''
a = 'Hello World!'
b = '  Hello World!   '
c = 'Hello, World'
print(a.upper()) # Printa todo en mayus
print(a.lower()) # Printa todo en minus
print(b.strip()) # Quita espacios del principio y del fin
print(a.replace('H', 'J')) # Sustituye una cadena por otra
print(a.replace('Hello', 'Gay'))
print(c.split(',')) # El separador que elija, separa los trozos de cadena en una lista
'''

# CONCATENATE
'''
a = 'Hello'
b = 'World'
c = a + ' ' + b
print(c)
'''

# STRING FORMAT
'''
age = 36
txt = 'My name is John and I am {}'
print(txt.format(age)) # Coje argumentos pasados, les da formato y los mete como cadena dentro de {}

quantity = 3
itemno = 567
price = 49.95

myorder = 'I want {} pieces of the product number {} which cost is {} euros'
print(myorder.format(quantity, itemno, price)) # Puedes poner los que quieras y se ponen en orden

myorder = 'I want {2} pieces of the product number {0} which cost is {1} euros'
print(myorder.format(quantity, itemno, price)) # Puedes utilizar numeros para cambiar el orden
'''

# ESCAPE CHARACTER
'''
txt = 'We are the so-called \'Vikings\' from the north'
print(txt) # Para printar caracteres no permitidos en una cadena se usa \

\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value
'''

# STRING METHODS
'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''