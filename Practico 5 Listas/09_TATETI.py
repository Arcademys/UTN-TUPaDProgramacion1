# Crear el tablero vacío 3x3 con guiones
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Mostrar tablero inicial
print("Tablero inicial:")
for fila in tablero:
    print(" ".join(fila))

# Comienza el juego (solo algunas jugadas de ejemplo)
for turno in range(3):  # por ejemplo, 3 rondas de jugadas
    print(f"\nTurno {turno + 1}")

    # Jugador 1 (X)
    print("Jugador 1 (X):")
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = "X"
    else:
        print("Casilla ocupada, pierde turno.")

    # Mostrar tablero
    for fila_tablero in tablero:
        print(" ".join(fila_tablero))

    # Jugador 2 (O)
    print("Jugador 2 (O):")
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = "O"
    else:
        print("Casilla ocupada, pierde turno.")

    # Mostrar tablero
    for fila_tablero in tablero:
        print(" ".join(fila_tablero))
