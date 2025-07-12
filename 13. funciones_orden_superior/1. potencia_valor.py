def cuadrado(x):
    return x * x


def cubo(x):
    return x ** 3

# Funcion de orden superior
def aplicar(funcion, valor):
    return funcion(valor)

# Envia la función por parámetro
resultado = aplicar(cubo, 3)
print(resultado)

