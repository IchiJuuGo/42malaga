
'''
The kata variable is always a string whose length 
is not higher than 42.
'''

# En este caso usamos esta funcion de f-string
# para rellenar los espacios vacios con guiones hasta
# un valor maximo de 42

kata = "The right format"
print(f"{kata:->41}")

