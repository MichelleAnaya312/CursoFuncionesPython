def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

#Los muestra en Formato de tupla
resultados = operaciones_basicas(8, 4)
print(resultados)