def exterior():
    a = 50 # a es de ámbito local de función exterior

    def interior():
        nonlocal a
        a = 20

    interior() # esta instrucción corresponde a la función exterior
    print(a)

exterior() # llamado de la función principal
