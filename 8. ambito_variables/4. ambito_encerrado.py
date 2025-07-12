def exterior():
    a = 50 # a es de ámbito local de función exterior

    def interior():
        print(a) # función interior puede acceder a la variable a de exterior


    interior() # esta instrucción corresponde a la función exterior


exterior() # llamado de la función principal
