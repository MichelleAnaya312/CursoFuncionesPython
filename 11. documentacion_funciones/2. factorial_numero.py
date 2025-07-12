# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    # (") * 3 + Enter
    """
    Calcula el factorial de un número entero no negativo.

    :param n: (int) Número entero no negativo.
    :return: (int) El factorial de n.
    :raises RecursionError: Si n es un número negativo.
    :raise: (genera excepciones)
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


resultado_factorial = factorial(5)
print(resultado_factorial)

#Consulta la documentacion de la funcion
# Opcion 1
# help(factorial)

# Opcion 2
# print(factorial.__doc__)