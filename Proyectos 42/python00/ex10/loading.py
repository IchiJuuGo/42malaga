import time

def ft_progress(lst):
    # la longitud total de la lista lst se almacena en una variable llamada total utilizando la función len() 
    total = len(lst)
    # se guarda la hora actual utilizando la función time.time() en una variable llamada start_time.
    start_time = time.time()
    # El bucle for comienza a iterar a través de la lista lst utilizando la función enumerate() para obtener tanto el índice de cada elemento como el propio elemento.
    for i, item in enumerate(lst):
        # En cada iteración del bucle, se calcula el tiempo transcurrido desde el comienzo del bucle en segundos y se almacena en una variable llamada elapsed_time.
        elapsed_time = time.time() - start_time
        # A continuación, se calcula el tiempo estimado restante para completar el bucle en segundos utilizando la fórmula elapsed_time * (total / (i+1) - 1) 
        # y se almacena en una variable llamada eta. La fórmula utiliza la proporción de elementos procesados hasta el momento con respecto al total de elementos 
        # para estimar el tiempo restante.
        eta = elapsed_time * (total / (i+1) - 1)
        # Luego, se calcula el porcentaje del progreso completado hasta el momento utilizando la fórmula (i+1) * 100 // total y se almacena en una variable llamada progress.
        # La fórmula divide el número actual de elementos procesados más uno (para evitar una división por cero) por el total de elementos y lo multiplica por 100.
        progress = (i+1) * 100 // total
        #Se construye una barra de progreso utilizando el porcentaje completado. La barra se compone de 20 caracteres y se divide en secciones de 4 caracteres cada una. 
        #Las secciones completadas se muestran como el carácter "=" y la sección actual se muestra como el carácter ">". Las secciones restantes se muestran como espacios en blanco.
        bar = "=" * (progress//5) + ">" + " " * (20 - progress//5)
        # Finalmente, se muestra una línea de progreso en la consola utilizando la función print(). La línea incluye el tiempo estimado restante, 
        # el porcentaje completado y la barra de progreso, la cantidad actual de elementos procesados y el tiempo transcurrido hasta el momento. 
        # El argumento end="" se utiliza para evitar que la línea se imprima con un salto de línea al final.
        print("\rETA: {:.2f}s [{}%][{}] {}/{} | elapsed time {:.2f}s".format(eta, progress, bar, i+1, total, elapsed_time), end="")
        # El elemento actual de la lista lst se devuelve utilizando la palabra clave yield.
        yield item
    print()

# Ejemplos de uso
# se crea una lista de números enteros del 0 al 999 utilizando la función range()
listy = range(0, -100, -1)
# crea una variable ret y se establece en 0. Esta variable se utilizará para almacenar el resultado del cálculo en cada iteración del bucle.
ret = 0
# Se inicia un bucle for utilizando la función ft_progress() para iterar sobre cada elemento de la lista listy. 
# En cada iteración del bucle, se realiza un cálculo utilizando el elemento actual y se agrega a la variable ret.
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
    # Se utiliza la función time.sleep() de Python para hacer una pausa de 0.01 segundos entre cada iteración del bucle. 
    # Esto es para simular un proceso que tarda un poco en procesar cada elemento.
print()
#  se imprime el resultado del cálculo en la variable ret utilizando la función print().
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)