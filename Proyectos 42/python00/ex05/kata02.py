
'''
The kata variable is always a tuple that contains 
5 non-negative integers. The first integer contains 
up to 4 digits, the rest up to 2 digits.
'''

# Igual que en el ejercicio kata00, llamamos a los
# elementos de la tupla y colocamos dentro el formato
# con el que queremos que sea devuelto

kata = (2019, 9, 25, 3, 30)
print(f" {kata[1]}/{kata[2]}/{kata[0]} 0{kata[3]}:{kata[4]}" )
