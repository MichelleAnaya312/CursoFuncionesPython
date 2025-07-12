def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función: ", lista)


mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función: ", mi_lista)

# Paso por referencia a objeto si modifica el objeto original
# Los tipos de datos que se envian por referencia:
# Listas, diccionarios y objetos personalizados