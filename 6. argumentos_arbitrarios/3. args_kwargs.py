def funcion_combinada(*args, **kwargs):
    # Formato de tupla
    print("Argumentos posicionales:", args)
    # Formato de diccionario
    print("Argumentos de palabra clave:", kwargs)

funcion_combinada(1, 2, 3, nombre="Juan", edad=25)
