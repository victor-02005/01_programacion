def evaluar_estudio(h_Estudio, objetivo):
    if h_Estudio >= 4:
        mensaje = "Excelente trabajo"
    elif h_Estudio >= objetivo:
        mensaje = "buen trabajo, cumpliste tu objetivo"
    else:
        mensaje = "debes organizar mejor tu tiempo"
        print("te falto estudiar ", objetivo - h_Estudio, "horas para cumplir tu objetivo")

    print(mensaje)
    return mensaje

nombre = input("¿cuál es tu nombre ?")
edad = int(input("cual es tu edad"))
h_Estudio = int(input("cuantas horas estudio hoy"))

# variable
objetivo = 2

# mostrar informacion
print("\n nombre", nombre)
print("edad", edad)
print("horas de estudio", h_Estudio)

# condicion
mensaje = evaluar_estudio(h_Estudio, objetivo)