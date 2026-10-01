nombre = input ("¿cual es tu nombre ?")
edad = int(input("¿cual es tu edad ?"))
horas_estudio = []
total_horas = 0
dias_cumplidos = 0

for i in range(5):
    horas = int(input(f"¿cuantas horas estudiaste en el día {i+1}? "))
    horas_estudio.append(horas)

    total_horas += horas
    if horas >= 2:
        print("Cumpliste")
        dias_cumplidos += 1
    else:
        print("No cumpliste")

print("Total de horas:", total_horas)
print("Días cumplidos:", dias_cumplidos)

estudiante = {
    "nombre": nombre,
    "edad": edad,
    "horas_estudio": horas_estudio,
    "total_horas": total_horas,
    "dias_cumplidos": dias_cumplidos
}

with open("registro_estudio.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n")
    archivo.write(f"Horas estudiadas: {horas_estudio}\n")
    archivo.write(f"Total de horas: {total_horas}\n")
    archivo.write(f"Días cumplidos: {dias_cumplidos}\n")


