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

}

# PARTE 2 - HELPFUL FUNCTIONS

def nombres_recetas(cookbook):
    # Funcion que printe los nombres de todas las recetas.
    for nombre_receta in cookbook:
        print(nombre_receta)

# nombres_recetas("Sandwich")

def detalles_receta(cookbook, nombre_receta):
    # Funcion que coja el nombre de una receta y printe sus detalles
    for nombre, detalles in cookbook.items():
        if nombre == nombre_receta:
            
            print(f"Receta de {nombre}")
            print(f"Ingredientes: {(cookbook)[nombre]['ingredients']}")
            print(f"Comida: {(cookbook)[nombre]['meal']}")
            print(f"Tiempo de preparacion: {(cookbook)[nombre]['prep_time']} minutos")

        else:
            print("No encuentro la receta")

        exit()

# detalles_receta(cookbook, "Sandwich")

def eliminar_receta(cookbook, nombre_receta):
    # Funcion que tome el nombre de una receta y lo elimine
    if nombre_receta in cookbook:
        del cookbook[nombre_receta]
        print("Receta eliminada")
    else:
        print("No se encuentra la receta")
        
# eliminar_receta(cookbook, "Caracoles")

def agregar_receta(cookbook):
    # Funcion que sume una receta desde el input de usuario.
    # Para ello necesitas un nombre, ingredientes, meal y prep_time
    nombre_receta = input("Introduce el nombre de la receta: ")
    ingredients = input("Introduce los ingredientes separados por comas: ").split(",")
    meal = input("El mejor momento para esta comida es: ")
    prep_time = int(input("Tiempo de preparacion en min: "))

    if isinstance(prep_time, int):
        print("Por favor introduce un numero valido")

    nueva_receta = {"nombre": nombre_receta, "ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    cookbook[nombre_receta] = nueva_receta

# agregar_receta(cookbook)

def cerrar_libro(cookbook):
    print("Gracias por cocinar con nosotros <3")
    return True

# cerrar_libro(cookbook)

############### HASTA AQUI FUNCIONA <3 ###############

# PARTE 3 - A COMMAND LINE EXECUTABLE!
# El programa te hara tomar una decision entre imprimir el contenido del cookbook,
# mostrar, agregar, eliminar una receta o salir del programa.

'''
# Lista de las funciones
nombres_recetas("Sandwich")
detalles_receta(cookbook, "Sandwich")
eliminar_receta(cookbook, "Sandwich")
agregar_receta(cookbook)
cerrar_libro(cookbook)
'''

def programa():
    while True:
        print("Bienvenido al libro de recetas de Python")
        print("Por favor elige una opcion: ")
        print("1: Agregar una receta")
        print("2: Eliminar receta")
        print("3: Imprimir una receta")
        print("4: Imprimir el libro de cocina")
        print("5: Salir de la app")

        try:
            elegir = int(input("Introduce un numero del 1 al 5: "))
            if elegir == 1:
                agregar_receta(cookbook)
            elif elegir == 2:
                eliminar_receta(cookbook)
            elif elegir == 3:
                detalles_receta(cookbook)
            elif elegir == 4:
                nombres_recetas(cookbook)
            elif elegir == 5:
                cerrar_libro(cookbook)
            else:
                print("Por favor introduce un numero valido")
        except ValueError:
            print("Invalid choice. Please enter a numbre from 1 - 5")    
        break

    
programa()

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

# }