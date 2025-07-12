y = 20


def funcion():
    global y
    y = 30
    print(y, " impresión dentro de la función")


funcion()
print(y, " impresión fuera de la función")