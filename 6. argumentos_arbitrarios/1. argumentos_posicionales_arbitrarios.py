# Argumentos posicionales arbitrarios: *args
#Formato de tupla
def sum_numeros(*numeros):
    print(numeros)
    resultado = sum(numeros)
    print(resultado)


sum_numeros(1, 2, 3, 4, 5, 6)


