
Ltitulos = []
Lejemplares = []
opcion = 0

while opcion != 8:
    opcion = int(input("1. Ingresar titulos 2. Ingresar ejemplares  3. Mostrar catalago 4. Consultar disponibilidad 5. Listar agotados 6. Agragar titulos   7. Actualizar ejemplares    8. Salir"))

    if opcion == 1:
        cantidad = int(input("Cuantos titulos quiere ingresar? "))
        for i in range (cantidad):
            titulo = str(input("AGREGAR TITULO:"))
            Ltitulos.append(titulo)
            Lejemplares.append(0)
       
        
        
    elif opcion == 2:
    for i in range(len(Ltitulos)):
    cantidad_ejemplares = int(input(f"Ingrese ejemplares para '{Ltitulos[i]}': ")
    Lejemplares[i] = cantidad_ejemplares


    elif opcion == 3:
    for i in range(len(Ltitulos)):
    print(f"{Ltitulos[i]}, {Lejemplares[i]}")

    elif opcion == 4:
    