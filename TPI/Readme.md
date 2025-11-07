```mermaid
flowchart TD
    A([Inicio del Programa]) --> B[Leer archivo CSV con leer_csv()]
    B --> C{¿Archivo existe?}
    C -->|No| D[Crear lista vacía de países]
    C -->|Sí| E[Cargar lista de países desde el CSV]
    E --> F[Mostrar Menú Principal]

    F --> G[1️⃣ Buscar país por nombre]
    F --> H[2️⃣ Filtrar países]
    F --> I[3️⃣ Ordenar países]
    F --> J[4️⃣ Mostrar estadísticas]
    F --> K[5️⃣ Salir]

    G --> L[Usa buscar_pais()]
    L --> M[Mostrar resultados en consola]
    M --> F

    H --> H1{Criterio de filtro}
    H1 -->|Continente| H2[Usa filtrar_por_continente()]
    H1 -->|Población| H3[Usa filtrar_por_rango_poblacion()]
    H1 -->|Superficie| H4[Usa filtrar_por_rango_superficie()]
    H2 --> M
    H3 --> M
    H4 --> M

    I --> I1{Criterio de ordenamiento}
    I1 -->|Nombre| I2[Usa ordenar_por_nombre()]
    I1 -->|Población| I3[Usa ordenar_por_poblacion()]
    I1 -->|Superficie| I4[Usa ordenar_por_superficie()]
    I2 --> M
    I3 --> M
    I4 --> M

    J --> J1[Usa funciones estadísticas]
    J1 --> J2[pais_mayor_poblacion(), pais_menor_poblacion()]
    J2 --> J3[promedio_poblacion(), promedio_superficie()]
    J3 --> J4[cantidad_por_continente()]
    J4 --> M

    K --> N[Guardar cambios (guardar_csv)]
    N --> O([Fin del Programa])

```
