def funcion_condicional(valor):
    if valor > 0:
        return "Positivo"
    elif valor < 0:
        return "Negativo"
    else:
        return "Cero"

resultado_condicional = funcion_condicional(-7)
print(resultado_condicional)