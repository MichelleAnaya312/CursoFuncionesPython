def suma_cuadrados(a, b):
    """
    Calcula la suma de los cuadrados de dos números.
    """
    cuadrado_a = a ** 2
    cuadrado_b = b ** 2
    suma = cuadrado_a + cuadrado_b
    return suma

def imprimir_resultado(a, b):
    """
    Imprime la suma de los cuadrados de dos números.
    """
    resultado = suma_cuadrados(a, b)
    print(f"La suma de los cuadrados de {a} y {b} es: {resultado}")

numero1 = 3
numero2 = 4
imprimir_resultado(numero1, numero2)

#Según pep8, no debería superar las 79 líneas de código