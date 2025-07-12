def modificar_valor(x):
    x = x + 10
    print("Dentro de la función: ", x)


numero = 5
modificar_valor(numero)
print("Fuera de la función: ", numero)

# Paso por valor no modifica los valores
# Los tipos de datos que se envian por valor:
# Enteros, flotantes y cadenas