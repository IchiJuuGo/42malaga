
# EX05 - KATA04 #

'''
The kata variable is always a tuple that contains, 
in the following order: 
• 2 non-negative integer containing up to 2 digits
• 1 decimal
• 1 integer
• 1 decimal
'''

kata = (0, 4, 132.42222, 10000, 12345.67)

print(f"module_0{kata[0]}, ex_0{kata[1]} : {kata[2]:.2f}, {kata[3]/10000:.2f}e+04, {kata[4]/10000:.2f}e+04")
# :.2f se usa para mostrar solo 2 decimales con f-strings

