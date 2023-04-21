
#############

# PYTHON OPERATORS

#############


# LIST
'''
thislist1 = ["apple", "banana", "cherry"]
print(thislist1)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # Las listas permiten duplicados
print(len(thislist)) # Te dice la longitud de la lista

# DATA TYPES
 # Una lista puede tener cualquier tipo de dato, iguales o combinados
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# Tambien se puede usar el constructo list()
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# PYTHON COLLECTIONS
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

# ACCESS LIST ITEMS
'''
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# NEGATIVE INDEXING
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1]) # -1 refers to the last item, -2 refers to the second last item etc.

# RANGE OF INDEXES
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Index 2 (included) and index 5 (not included). First item has index 0.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # This example returns the items from the beginning to, but NOT including, "kiwi"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # This example returns the items from "cherry" to the end

# RANGE OF NEGATIVE INDEXES
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)

# CHECK IF ITEM EXISTS
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''

# CHANGE LIST ITEMS
'''
# CHANGE ITEM VALUE
thislist = ['apple', 'orange', 'strawberry']
thislist[1] = 'gay'
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # El ultimo numero no se incluye

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # If you insert more items than you replace,
# the new items will be inserted where you specified, and the remaining items will move accordingly

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # If you insert less items than you replace, 
# the new items will be inserted where you specified, and the remaining items will move accordingly

'''
# ADD LIST ITEMS

'''
# APPEND ITEMS
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # Suma un item al final de la lista

# INSERT ITEMS
thislist = ['apple', 'banana', 'watermelon']
thislist.insert(2, 'CheRRyyy')
print(thislist) # To insert a list item at a specified index, use the insert() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # The extend() method does not have to append lists, 
# you can add any iterable object (tuples, sets, dictionaries etc.).

'''
# REMOVE ITEMS
'''
# REMOVE SPECIFIED ITEM
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # The del keyword also removes the specified index

thislist = ["apple", "banana", "cherry"]
del thislist # The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # The clear() method empties the list. The list still remains, but it has no content.

'''
# LOOP LISTS

# LOOP THROUGH A LIST
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# LOOP THROUGH THE INDEX NUMBERS
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])