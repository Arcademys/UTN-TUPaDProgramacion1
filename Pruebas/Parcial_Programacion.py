Ltitulos = []
Lejemplares = []

while True:
    print("************************************************************************")
    print("**********************Bienvenido a la biblioteca************************")
    print("************************************************************************")
    print("Elija una opción: ")
    print(" 1. Ingresar títulos")
    print(" 2. Ingresar ejemplares")
    print(" 3. Mostrar catálogo")
    print(" 4. Consultar disponibilidad")
    print(" 5. Listar agotados")
    print(" 6. Agregar título")
    print(" 7. Actualizar ejemplares (préstamo/devolución)")
    print(" 8. Salir")

    opcion = int(input("-----> "))

    match opcion:
        case 1:
            cantidad = int(input("Ingresa la cantidad de títulos a agregar: "))
            for i in range(cantidad):
                titulo = input("Agregar título: ")
                Ltitulos.append(titulo)
                

        case 2:
            for i in range(len(Ltitulos)):
                ejemplar = int(input(f"Ingrese cantidad de ejemplares para '{Ltitulos[i]}': "))
                Lejemplares.append(ejemplar)

        case 3:
            for i in range(len(Ltitulos)):
                print(f"{Ltitulos[i]} -> {Lejemplares[i]} ejemplares") 
                
                

        case 4:
            buscar = input("Ingrese el título a consultar: ")
            if buscar in Ltitulos:
                i = Ltitulos.index(buscar)
                print(f"{buscar} tiene {Lejemplares[i]} ejemplares")
            else:
                print("Título no encontrado.")

        case 5:
            print("Libros agotados:")
            for i in range(len(Ltitulos)):
                if Lejemplares[i] == 0:
                    print(Ltitulos[i])

        case 6:
            nuevo = input("Ingrese nuevo título: ")
            stock = int(input("Ingrese cantidad de ejemplares: "))
            Ltitulos.append(nuevo)
            Lejemplares.append(stock)

        case 7:
            libro = input("Ingrese el título a actualizar: ")
            if libro in Ltitulos:
                i = Ltitulos.index(libro)
                accion = input("¿Prestamo o devolucion?: ").lower()
                if accion == "prestamo" and Lejemplares[i] > 0:
                    Lejemplares[i] -= 1
                    print("Prestamo registrado.")
                elif accion == "devolucion":
                    Lejemplares[i] += 1
                    print("Devolucion registrada.")
                else:
                    print("No se puede realizar la acción.")
            else:
                print("Título no encontrado.")

        case 8:
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción no válida, intente nuevamente.")
