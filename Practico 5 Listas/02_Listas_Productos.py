
listas_productos = []
print ("Ingrese 5 productos:")
for i in range(5):
    producto = input("Producto: ")
    listas_productos.append(producto)

print("Lista de pruductos:")
for producto in listas_productos:
    print(producto)

lista_ordenada = sorted(listas_productos)
print("Lista ordenada:")
for producto in lista_ordenada:
    print(producto)

eleminar = input("Ingrese el producto a eleminar: ")

if eleminar in lista_ordenada:
    lista_ordenada.remove(eleminar)
    print(f"Producto {eleminar} ha sido eleminado.")
else:
    print(f"El producto {eleminar} no existe")

print("Lista actualizada:")

for producto in lista_ordenada:
    print(producto)
      