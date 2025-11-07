
# Sistema de Gestión de Países
**Trabajo Práctico Integrador (TPI) - Programación 1**

Este proyecto es un sistema de consola desarrollado en Python que permite gestionar, filtrar, ordenar y analizar datos de países cargados desde un archivo CSV.

---

## Diagrama de Flujo
A continuación, se presenta el flujo principal de la aplicación:

![Diagrama de Flujo](diagrama.png)

---

## Instalación y Ejecución

Para ejecutar este proyecto, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Arcademys/UTN-TUPaDProgramacion1.git](https://github.com/Arcademys/UTN-TUPaDProgramacion1.git)
    ```
2.  **Navegar a la carpeta de la aplicación:**
    ```bash
    cd UTN-TUPaDProgramacion1/TPI/Aplicacion
    ```
3.  **Ejecutar el programa:**
    ```bash
    python sistema_gestion_países.py
    ```

---

## Funcionalidades
### 🧭 Menú Principal
![Menú Principal](Menu%20Principal.jpg)

### 1. Buscar País
![Ejemplo de Búsqueda](Busqueda.jpg)
Permite buscar un país por su nombre exacto o parcial.
*(Ejemplo: Buscar "arg" encuentra "Argentina").*

### 2. Filtrar Países
![Ejemplo de Filtro](Filtro.jpg)
Sub-menú para filtrar la lista completa por:
* **Continente** (ej. "América del Sur")
* **Rango de Población** (mínimo y máximo)
* **Rango de Superficie** (mínimo y máximo)

### 3. Ordenar Lista
Permite reordenar los países ascendente o descendentemente por:
* Nombre
* Población
* Superficie

### 4. Estadísticas
![Ejemplo de Estadísticas](Estadisticas.jpg)
Muestra cálculos automáticos sobre los datos actuales:
* País con mayor/menor población.
* Promedios de población y superficie.
* Cantidad de países por continente.

---

## 👥 Integrantes y Roles

* **Enrique Alejandro Carrasco:** Desarrollo de la interfaz de terminal (menús, validaciones, interacción con el usuario).
* **Juan José (apellido):** Desarrollo de la lógica de negocio (carga de datos, funciones de filtrado, ordenamiento y cálculos).