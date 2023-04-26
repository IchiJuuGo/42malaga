'''
Part 3: A command line executable !
Create a program that use your cookbook and your functions.
The program will prompt the user to make a choice between printing the cookbook
content, printing one recipe, adding a recipe, deleting a recipe or quitting the cookbook.
Your program will continue to ask for prompt until the user decide to quit it. The program 
cannot crash if a wrong value is entered: you must handle the error and ask for another prompt.
'''

#  ///////////////////////////////////////////////////////////

# PARTE 1 - NESTED DICTIONARY
# Guardamos un diccionario con la receta y sus items, dentro de otro diccionario
# superior que corresponde al libro de recetas.

cookbook = {
    "Sandwich" : {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch", 
        "prep_time": 10
    },

    "Cake" : {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert", 
        "prep_time": 60
    },
    
    "Salad" : {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch", 
        "prep_time": 15
    },

    "Caracoles" : {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch", 
        "prep_time": 15
    },

}

# PARTE 2 - HELPFUL FUNCTIONS
# Funcion que printe los nombres de todas las recetas.
'''
def nombres_recetas(cookbook):
    for nombre_receta in cookbook:
        print(nombre_receta)

nombres_recetas(cookbook)

'''
# Funcion que coja el nombre de una receta y printe sus detalles
'''
def detalles_receta(cookbook, nombre_receta):
    for nombre, detalles in cookbook.items():
        if nombre == nombre_receta:
            
            print(f"Receta de {nombre}")
            print(f"Ingredientes: {(cookbook)[nombre]['ingredients']}")
            print(f"Comida: {(cookbook)[nombre]['meal']}")
            print(f"Tiempo de preparacion: {(cookbook)[nombre]['prep_time']} minutos")

        else:
            print("No encuentro la receta maricon")

        exit()

detalles_receta(cookbook, "Sandwich")
'''
# Funcion que tome el nombre de una receta y lo elimine
'''
def eliminar_receta(cookbook, nombre_receta):
        if nombre_receta in cookbook:
            del cookbook[nombre_receta]
            print("Receta eliminada")
        else:
            print("No se encuentra la receta")
        
# eliminar_receta(cookbook, "Caracoles")
'''

# HASTA AQUI FUNCIONA <3

# Funcion que sume una receta desde el input de usuario.
    # Para ello necesitas un nombre, ingredientes, meal y prep_time

def sumar_receta(cookbook):
    input("Introduce el nombre de la receta: ")
    input("Introduce los ingredientes: ")
    input("El mejor momento para esta comida es: ")
    input("Tiempo de preparacion: ")

    nuevo_diccionario = {}
    
sumar_receta(cookbook)

# BILBIOGRAFIA
# https://j2logo.com/bucle-for-en-python/#for-en-python
# https://www.w3schools.com/python/python_dictionaries.asp







# ///////////////////
# BACKUP DICCIONARIO
# ///////////////////
# cookbook = {
#     "Sandwich" : {
#         "ingredients": ["ham", "bread", "cheese", "tomatoes"],
#         "meal": "lunch", 
#         "prep_time": 10
#     },

#     "Cake" : {
#         "ingredients": ["flour", "sugar", "eggs"],
#         "meal": "dessert", 
#         "prep_time": 60
#     },
    
#     "Salad" : {
#         "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
#         "meal": "lunch", 
#         "prep_time": 15
#     },

#     "Caracoles" : {
#         "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
#         "meal": "lunch", 
#         "prep_time": 15
#     },

# }