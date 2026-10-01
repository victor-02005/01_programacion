def verificar_edad(edad):
    if int(edad) >= 18:
        return "mayor de edad"
    else:
        return "menor de edad"


print("------INFORMACION-----")
nombre = input("¿cual es tu nombre ?")
edad = int(input("¿cual es tu edad ?"))

resultado = verificar_edad(edad)
print(resultado)









