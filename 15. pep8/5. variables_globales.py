def calcular_promedio(notas):
    """
    Calcular el promedio de una lista de notas.
    """
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

def imprimir_resultado(nombre, promedio):
    """
    Imprime el resultado del promedio de notas para un estudiante.
    """
    print("{} tiene un promedio de notas de: {:.2f}".format(nombre, promedio))

# Uso directo sin variables globales
notas_juan = [85, 90, 92, 88]
notas_maria = [78, 85, 89, 92]

promedio_juan = calcular_promedio(notas_juan)
promedio_maria = calcular_promedio(notas_maria)

imprimir_resultado("Juan", promedio_juan)
imprimir_resultado("Maria", promedio_maria)