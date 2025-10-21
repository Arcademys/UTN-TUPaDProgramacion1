with open("productos.txt", "w") as archivo:
          archivo.write("Lapicera, 120.5,30\n")
          archivo.write("Cuaderno,350.0,15\n")
          archivo.write("Regla,80.0,20\n")
          
print("Archivo 'productos.txt' creado correctamente.")

# actividad 2 


with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

