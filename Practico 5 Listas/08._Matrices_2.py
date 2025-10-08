
notas = []


for estudiante in range(1, 6):
    print(f"\nEstudiante {estudiante}:")
    fila = []
    for materia in range(1, 4):
        nota = float(input(f"Ingrese la nota {materia}: "))
        fila.append(nota)
    notas.append(fila)

print("\nMatriz de notas (5 estudiantes x 3 materias):")
print("Est | Nota1 | Nota2 | Nota3")
print("-----------------------------")

for i in range(5):
    print(f"{i+1:3} | {notas[i][0]:6.2f} | {notas[i][1]:6.2f} | {notas[i][2]:6.2f}")


print("\nPromedio de cada estudiante:")
for i in range(5):
    suma = 0
    for j in range(3):
        suma = suma + notas[i][j]
    promedio = suma / 3
    print(f"Estudiante {i+1}: {promedio:.2f}")


print("\nPromedio de cada materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma = suma + notas[i][j]
    promedio = suma / 5
    print(f"Materia {j+1}: {promedio:.2f}")
