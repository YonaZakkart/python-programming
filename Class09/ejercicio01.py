# Ejercicio 1: Sistema de configuración de servidor.
# Una aplicación necesita almacenar configuraciones que no deben modificarse 
# accidentalmente durante la ejecución.
# Crea una tupla llamada configuración con la siguiente información:
# Nombre de aplicación
# Versión
# Servidor
# Puerto
# Modo de ejecución

configuracion = ("SnapStore", "1.7.2", "localhost", "8082", "Produccion")
print("" \
"\nApp: ", configuracion[0],
"\nVersion: ", configuracion[1],
"\nServidor: ", configuracion[2],
"\nPuerto: ", configuracion[3],
"\nModo: ", configuracion[4]) #Me gusta ordenar los mensajes de salida

# A. Acceso
# Muestra solamente:
# • La versión. 
print("\n- Version: ", configuracion[1])
# • El servidor. 
print("\n- Servidor: ", configuracion[2])
# • El puerto. 
print("\n- Puerto: ", configuracion[3])

# B. Longitud
# Utiliza len() para determinar cuántos elementos contiene la tupla.
print("\nConfiguracion tiene: ", len(configuracion), "Elementos")