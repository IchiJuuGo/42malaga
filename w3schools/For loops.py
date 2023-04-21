
#############

# PYTHON FOR LOOPS

#############

# FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# LOOPING THROUGH A STRING
for x in 'banana':
  print(x)

# THE BREAK STATEMENT
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # Exit the loop when x is "banana"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) # Exit the loop when x is "banana", but this time the break comes before the print

for x in 'banana':
  print(x)
  if x == "n":
    break

# THE continue STATEMENT
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # With the continue statement we can stop the current iteration of the loop, and continue with the next

# THE range() FUNCTION
for x in range(6):
  print(x) 
  
  # The range() function returns a sequence of numbers,
  # starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
  # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for x in range(2, 6):
  print(x) # El ultimo numero no aparece

for x in range(2, 30, 3):
  print(x) # El tercer parametro marca el incremento

# ELSE IN FOR LOOP
 # The else keyword in a for loop specifies a block of code to be executed when the loop is finished

for x in range(6):
  print(x)
else:
  print('Listo!') 

for x in range(6):
  if x == 3: 
    break
  print(x)
else:
  print('Hemos acabado') # Note: The else block will NOT be executed if the loop is stopped by a break statement

# NESTED LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #  The "inner loop" will be executed one time for each iteration of the "outer loop"

# THE PASS STATEMENT
for x in [0, 1, 2]:
  pass # Para quitar errores





