

cookbook = {
    'Sandwich': {
    "ingredients": ["ham","bread","cheese","tomatoes"],
    "meal": "lunch",
    "prep_time": 10,
    },

    'Cake': {
    "ingredients": ["flour","sugar","eggs"],
    "meal": "dessert",
    "prep_time": 60,
    },

    'Salad': {
    "ingredients": ["avocado","arugula","tomatoes","spinach"],
    "meal": "lunch",
    "prep_time": 15,
    },

    }

def show_cookbook():
    for a in cookbook:
        print(a)

def details_recipe():
    r = input("Introduzca el nombre de la receta para mostrar sus detalles: ")
    print(f"Recipe for {r}:")
    print(f"\tIngedients list:  {cookbook[r]['ingredients']}")
    print(f"\tTo be eaten for {cookbook[r]['meal']}.")
    print(f"\tTakes {cookbook[r]['prep_time']} minutes of cooking.")

def delete_recipe():
    try:
        r = input("Introduzca el nombre de la receta para borrarla: ")
        cookbook.pop(r)
    except KeyError:
        print("KeyError: You must enter a saved recipe.")

def add_recipe():
    
    r1 = input("Enter a recipe name: ")
    ingredientes=[]
    r2 = input("Enter a ingredient: ")
    while(len(r2) != 0):
        r2 =input("Enter a ingredient: ")
    r3 = input("Enter a meal type: ")
    r4 = input("Enter a preparation time: ")

    r = {
    'r1': {
    "ingredients": ["ham","bread","cheese","tomatoes"],
    "meal": "lunch",
    "prep_time": 10
    }
    }
    cookbook.update(r)

def menu():

    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")

    respuesta1 = str(input("Please select an option:"))
    switcher = {
         1:
            add_recipe(),
         2:
            delete_recipe(),
         3:
            details_cookbook(),
         4:
            show_cookbook()
        }
    func = switcher.get(respuesta1, "respuesta incorrecta")
    print(func)

menu()
