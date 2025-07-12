def saludar(nombre):
    return f"Hola, {nombre}"


mi_funcion = saludar

# Llamado a través de la variable
mensaje = mi_funcion("Mariana")
print(mensaje)