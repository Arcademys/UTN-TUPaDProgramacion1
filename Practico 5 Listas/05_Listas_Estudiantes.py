lista_estudiantes = ["Ana", "Juan", "Luis", "Maria", "Pedro", "Carla", "Sofia", "Diego"]
print("lISTA DE ESTUDIANTES: ")
for estudiante in lista_estudiantes:
    print(estudiante)

opcion = input("Desea agregar o eliminar un estudiante? ")

if opcion == "agregar":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante:")
    lista_estudiantes.append (nuevo_estudiante)

if opcion == "eliminar":
    eleminar_estudiante = input("Ingrese nombre del estudiante a eleminar: ")
    if eleminar_estudiante  in lista_estudiantes:
        lista_estudiantes.remove(eleminar_estudiante)
        print("Estudiante borrado")
    else:
        print ("El nombre no se encuentra en la lista")

print("Lista final de estudiantes:")
for estudiante in lista_estudiantes:
    print(estudiante)


