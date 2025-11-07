
flowchart TD

A[Inicio] --> B[Leer archivo CSV]
B --> C{Archivo existe?}
C -- No --> D[Crear lista vacía]
C -- Sí --> E[Cargar lista de países]
E --> F[Mostrar menú principal]

F --> G[Opción: Agregar país]
F --> H[Opción: Actualizar país]
F --> I[Opción: Buscar / Filtrar]
F --> J[Opción: Ordenar]
F --> K[Opción: Estadísticas]
F --> L[Opción: Salir]

G --> M[Agregar país a lista]
H --> N[Modificar país existente]
I --> O[Mostrar resultados en consola]
J --> P[Mostrar lista ordenada]
K --> Q[Calcular y mostrar resultados]
L --> R[Guardar CSV y finalizar]

M --> R
N --> R
O --> F
P --> F
Q --> F
R --> S[Fin]
