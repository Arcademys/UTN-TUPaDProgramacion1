from funciones import *

ruta = "/home/arcademys/Documents/Repositorios/UTN-TUPaDProgramacion1/TPI/Aplicacion/paises_mundo_2023.csv"

# Cargar países
paises = leer_csv(ruta)
print("llega leer_csv:", len(paises), "países cargados\n")

# Test agregar
nuevo = {
    "nombre": "Uruguay",
    "iso_codigo": "URY",
    "poblacion": 3500000,
    "anio_poblacion": 2023,
    "superficie_km2": 176215,
    "continente": "América del Sur",
    "capital": "Montevideo",
}

print("llega agregar_pais:", agregar_pais(paises, nuevo))
print("llega actualizar_pais:", actualizar_pais(paises, "Argentina", 47000000, 2780400))

# Test búsquedas y filtros
print("llega buscar_pais:", len(buscar_pais(paises, "ar")))
print("llega filtrar_por_continente:", len(filtrar_por_continente(paises, "Europa")))
print(
    "llega filtrar_por_rango_poblacion:",
    len(filtrar_por_rango_poblacion(paises, 1000000, 50000000)),
)

# Test ordenamientos
ordenados = ordenar_por_nombre(paises)
print("llega ordenar_por_nombre:", [p["nombre"] for p in ordenados[:5]])

# Test funciones aún sin implementar (comunicación)
print(pais_mayor_poblacion(paises))
print(promedio_poblacion(paises))
