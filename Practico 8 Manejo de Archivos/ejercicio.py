# actividad 1

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

# actividad 3

with open("producto.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n ***Agregar un nuevo producto***")
nombre = input("Nombre del producto: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

with open("producto.txt", "a") as archivo:
    archivo.write(f"{nombre}, {precio},{cantidad}\n")

print("Producto agregado exitosamente.")

#Actividad 4

# actividad4_lista_diccionarios.py

productos = []

# Leer archivo y cargar en lista de diccionarios
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

# Mostrar productos cargados
print("=== Productos cargados ===")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Opción: agregar un nuevo producto
print("\n--- Agregar nuevo producto ---")
nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

# Agregarlo a la lista y al archivo
productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("Producto agregado y guardado correctamente.")


#actividad 5

productos = [{"nombre": "Lapicera", "precio": 120.5, "cantidad": 30}, {"nombre": "Cuaderno", "precio": 350.0, "cantidad": 15}, 
             {"nombre": "Regla", "precio": 80.0, "cantidad": 20}]
nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")


encontrado = False


for producto in productos:
    if producto["nombre"].lower() == nombre_buscado.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break  


if not encontrado:
    print(f"\nEl producto '{nombre_buscado}' no existe en la lista.")

# actividad 6



with open("productos.txt", "w") as archivo:  # 
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        archivo.write(f"{nombre},{precio},{cantidad}\n")

print("Archivo 'productos.txt' actualizado correctamente.")
