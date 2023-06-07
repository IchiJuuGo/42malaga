
# Librerias
import subprocess
import time

# Ruta de los archivos correspondientes a cada nodo
node1_file = "Nodo_5001.py"
node2_file = "Nodo_5002.py"
node3_file = "Nodo_5003.py"
connection_file = "conexion_nodos.py"

# Ejecutar los archivos correspondientes a cada nodo
subprocess.Popen(["python", node1_file])
subprocess.Popen(["python", node2_file])
subprocess.Popen(["python", node3_file])

# Esperar un breve tiempo para asegurarse de que los nodos se inicien
time.sleep(1)

# Ejecutar el archivo para la conexión entre nodos
subprocess.Popen(["python", connection_file])
