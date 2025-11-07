```mermaid
flowchart TD
    A([Inicio del programa]) --> B[Leer archivo CSV con leer_csv]
    B --> C{Archivo existe?}
    C -->|No| D[Crear lista vacia de paises]
    C -->|Si| E[Cargar lista de paises desde el CSV]
    E --> F[Mostrar menu principal]

    F --> G[1 Buscar pais por nombre]
    F --> H[2 Filtrar paises]
    F --> I[3 Ordenar paises]
    F --> J[4 Mostrar estadisticas]
    F --> K[5 Salir]

    G --> L[Usa buscar_pais]
    L --> M[Mostrar resultados en consola]
    M --> F

    H --> H1{Criterio de filtro}
    H1 -->|Continente| H2[Usa filtrar_por_continente]
    H1 -->|Poblacion| H3[Usa filtrar_por_rango_poblacion]
    H1 -->|Superficie| H4[Usa filtrar_por_rango_superficie]
    H2 --> M
    H3 --> M
    H4 --> M

    I --> I1{Criterio de ordenamiento}
    I1 -->|Nombre| I2[Usa ordenar_por_nombre]
    I1 -->|Poblacion| I3[Usa ordenar_por_poblacion]
    I1 -->|Superficie| I4[Usa ordenar_por_superficie]
    I2 --> M
    I3 --> M
    I4 --> M

    J --> J1[Usa funciones estadisticas]
    J1 --> J2[pais_mayor_poblacion y pais_menor_poblacion]
    J2 --> J3[promedio_poblacion y promedio_superficie]
    J3 --> J4[cantidad_por_continente]
    J4 --> M

    K --> N[Guardar cambios con guardar_csv]
    N --> O([Fin del programa])


```
