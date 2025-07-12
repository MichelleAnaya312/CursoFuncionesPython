# Argumentos de palabra clave arbitrarios: **kwargs
# Formato de diccionario
def imprimir_info(**info):
    # Genera un diccionario
    print(info)
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

imprimir_info(nombre="Juan", edad=25, ciudad="Ejemplo")
