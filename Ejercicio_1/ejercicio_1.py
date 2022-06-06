print()
print("-----------------------------------------------------")
print("-----------Centinela---------------------------------")
print("-----------------NOTAS ESTUDIANTES-------------------")
print()

# input

cod = int(input("Ingrese el código del estudiante: "))
nombre = input("Ingrese el nombre del estudiante: ")

if cod != 0:
    nota1= float(input("Ingrese la nota del parcial no. 1: "))
    nota2 = float(input("Ingrese la nota del parcial no. 2: "))
    nota3 = float(input("Ingrese la nota del parcial no. 3: "))
else:
    print("Fin de los datos de entrada")

#Procesing

reprobados = 0

while cod != 0:
    nota_final = (nota1+nota2+nota3)/3
    print("El estudiante de código " + str(cod) + " cuyo nombre es " + nombre + " obtuvo una nota definitiva de " + str(nota_final))
    if nota_final < 3:
        reprobados = reprobados + 1  
    # input
    cod = int(input("Ingrese el código del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    if cod != 0:
        nota1= float(input("Ingrese la nota del parcial no. 1: "))
        nota2 = float(input("Ingrese la nota del parcial no. 2: "))
        nota3 = float(input("Ingrese la nota del parcial no. 3: "))
    else:
        print("Fin de los datos de entrada")

# Output
print("Cantidad de estudiantes que reprobaron la materia: " + str(reprobados))