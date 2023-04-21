
#############

# VARIABLES

#############

# MANY VALUES TO MULTIPLE VARIABLES
'''
x, y, z = 'Orange', 'Banana', 'Apple'
print(x)
print(y)
print(z)
'''

# ONE VALUE TO MULTIPLE VARIABLES
'''
x = y = z = 'Orange'
print(x)
print(y)
print(z)
'''

# UNPACK A COLLECTION
'''
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)
'''
# OUTPUT VARIABLES
'''
impresionante = ['Python', 'es', 'impresionante']
x, y, z = impresionante
print(x, y, z)
'''

# GLOBAL AND LOCAL VARIABLES
'''
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc() # Esto printa la funcion definida arriba
print("Python is " + x)
'''

# GLOBAL KEYWORD
'''
def myfunc():
  global x
  x = "fantastic"
  print('Homosexuals are ' + x)

myfunc()
print("Python is " + x)
'''

# Also, use the global keyword if you want to change a global variable inside a function.
'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
'''

# SPECIFY A VARIABLE TYPE
'''
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
'''


