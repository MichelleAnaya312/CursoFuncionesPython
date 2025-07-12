def operaciones_basicas(a, b):
    # (") * 3 + Enter
    """
    Realiza operaciones básicas entre dos números.

    :param a: (int o float) Primer número
    :param b: (int o float) Segundo número
    :return: Una tupla con los resultados de las operaciones.
            - suma (int o float): Suma de a y b
            - resta (int o float): Resta de a y b
            - multiplicacion (int o float): Producto de a y b
            - division (float): Cociente de a dividido por b (si b no es cero)
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

#Los muestra en Formato de tupla
resultados = operaciones_basicas(8, 4)
print(resultados)

#Consulta la documentacion de la funcion
# Opcion 1
# help(operaciones_basicas)

# Opcion 2
print(operaciones_basicas.__doc__)