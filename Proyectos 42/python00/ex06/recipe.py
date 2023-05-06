
# EX06 - RECIPE.PY #

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

def mostrar_cookbook():
    for a in cookbook:
        print(a)

def detalles_receta():
    receta = input("Introduzca el nombre de la receta para mostrar sus detalles: ")
    print(f"Receta de {receta}:")
    print(f"\tLista de ingredientes: {cookbook[receta]['ingredients']}")
    print(f"\tTipo de comida {cookbook[receta]['meal']}.")
    print(f"\tTiempo de preparacion: {cookbook[receta]['prep_time']}.")

def eliminar_receta():
    try:
        r = input("Introduzca el nombre de la receta para borrarla: ")
        cookbook.pop(r)
    except KeyError:
        print("Tienes que introducir una receta ya guardada.")
    print("Receta eliminada con exito! Que vas a hacer ahora?")

def agregar_receta():
    r1 = input("Nombre de la receta: ")
    ingredientes = []
    r2 = input("Introduce los ingredientes: ")
    print("Una vez hayas terminado de introducir los ingredientes, deja el espacio en blanco.")
    while(len(r2) != 0):
        r2 =input("Introduce los ingredientes: ")
    r3 = input("Tipo de comida: ")
    r4 = input("Tiempo de preparacion: ")

    print("Receta guardada con exito! Que vas a hacer ahora?")

    r = {
    'r1': {
    "ingredients": ["ham","bread","cheese","tomatoes"],
    "meal": "lunch",
    "prep_time": 10
    }
    }
    cookbook.update(r)

def salir():
    print("Gracias por utilizar el libro de recetas de python!")
    exit()

def menu():
    print("Bienvenido al libro de cocina de Python!")
    while True:
        print("Lista de opciones:")
        print("\t1: Agregar una receta")
        print("\t2: Eliminar una receta")
        print("\t3: Mostrar receta")
        print("\t4: Mostrar \"Cookbook\"")
        print("\t5: Salir")

        respuesta1 = int(input("Por favor elija una opción: "))
        botones = {
             1: agregar_receta,
             2: eliminar_receta,
             3: detalles_receta,
             4: mostrar_cookbook,
             5: salir
            }
        func = botones.get(respuesta1)
        
        if func:
            func()
        else:
            print("Respuesta incorrecta")

        if respuesta1 == 5:
            break

menu()