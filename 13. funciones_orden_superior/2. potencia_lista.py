def cuadrado(x):
    return x * x

def cubo(x):
    return x ** 3

# Funcion de orden superior
def aplicar_funcion_a_lista(funcion, lista):
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado

lista_numeros = [1, 2, 3, 4, 5]
# Envia la función por parámetro
resultados = aplicar_funcion_a_lista(cubo, lista_numeros)
print(resultados)