# Crear la matriz vacía
ventas = []

# Cargar datos
for producto in range(1, 5):
    print(f"\nProducto {producto}:")
    fila = []
    for dia in range(1, 8):
        cantidad = float(input(f"Ingrese las ventas del día {dia}: "))
        fila.append(cantidad)
    ventas.append(fila)

# Mostrar la matriz
print("\nMatriz de ventas (4 productos x 7 días):")
print("Prod | Día1 Día2 Día3 Día4 Día5 Día6 Día7")
print("-----------------------------------------")

for i in range(4):
    print(f"{i+1:4} |", end=" ")
    for j in range(7):
        print(f"{ventas[i][j]:4.0f}", end=" ")
    print()

# Calcular total por producto (por fila)
print("\nTotal vendido por cada producto:")
totales_productos = []
for i in range(4):
    suma = 0
    for j in range(7):
        suma = suma + ventas[i][j]
    totales_productos.append(suma)
    print(f"Producto {i+1}: {suma:.2f}")

# Calcular total por día (por columna)
print("\nVentas totales por día:")
ventas_por_dia = []
for j in range(7):
    suma = 0
    for i in range(4):
        suma = suma + ventas[i][j]
    ventas_por_dia.append(suma)
    print(f"Día {j+1}: {suma:.2f}")

# Día con mayores ventas
max_ventas_dia = max(ventas_por_dia)
dia_mayor = ventas_por_dia.index(max_ventas_dia) + 1
print(f"\nEl día con mayores ventas fue el día {dia_mayor} con {max_ventas_dia:.2f} unidades.")

# Producto más vendido
max_producto = max(totales_productos)
producto_mayor = totales_productos.index(max_producto) + 1
print(f"El producto más vendido fue el producto {producto_mayor} con {max_producto:.2f} unidades.")
