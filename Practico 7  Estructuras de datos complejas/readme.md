## 🧠 Guía Visual: Estructuras de Datos en Python

# 📋 **Listas (`list`)**

Crear una lista vacía

mi_lista = []

Agregar elementos
mi_lista.append(10)           # ➕ Agrega un elemento
mi_lista.extend([20, 30])     # ➕ Agrega varios

Acceder a elementos
mi_lista[0]                   # 👁️ Primer elemento → 10

Eliminar elementos
mi_lista.remove(20)           # ❌ Elimina el valor 20
mi_lista.pop()                # ❌ Elimina el último → 30
del mi_lista[0]               # ❌ Elimina por índice

 Vaciar la lista
mi_lista.clear()              # 🧹 Vacía la lista

# 🔗 **Tuplas (`tuple`)**
Crear una tupla vacía
mi_tupla = ()

#Crear una tupla con elementos
mi_tupla = (1, 2, 3)

 Acceder a elementos
mi_tupla[1]                   # 👁️ Segundo elemento → 2

 **⚠️Las tuplas son inmutables: no se pueden modificar ni borrar elementos⚠️**
 **📘Usos comunes:** agrupar datos fijos (por ejemplo, coordenadas o constantes).

# 🧪 **Conjuntos (`set`)**
Crear un set vacío
mi_set = set()

Agregar elementos
mi_set.add(5)                 # ➕ Agrega un elemento
mi_set.update([6, 7])         # ➕ Agrega varios

Eliminar elementos
mi_set.remove(6)              # ❌ Elimina 6 (error si no existe)
mi_set.discard(8)             # ❌ Elimina 8 (sin error si no existe)
mi_set.pop()                  # ❌ Elimina aleatorio

Vaciar el set
mi_set.clear()                # 🧹 Vacía el set

📘 **Usos comunes:** eliminar duplicados, operaciones de unión/intersección, comparar conjuntos.

# 📚 **Diccionarios (`dict`)**
Crear un diccionario vacío
mi_dict = { }

Agregar elementos
mi_dict["nombre"] = "Juan"    # ➕ Clave-valor
mi_dict.update({"edad": 25})  # ➕ Múltiples pares

Acceder a valores
mi_dict["nombre"]             # 👁️ → "Juan"

Eliminar elementos
del mi_dict["edad"]           # ❌ Elimina clave 'edad'
mi_dict.pop("nombre")         # ❌ Elimina y devuelve valor

Vaciar el diccionario
mi_dict.clear()               # 🧹 Vacía el diccionario

🔍 **Métodos útiles de diccionario**
mi_dict = {"nombre": "Juan", "edad": 25, "curso": "Python"}

 .keys() → 🔑 Claves
mi_dict.keys()
→ dict_keys(['nombre', 'edad', 'curso'])

.values() → 📦 Valores
mi_dict.values()
→ dict_values(['Juan', 25, 'Python'])

.items() → 🧩 Pares clave-valor
mi_dict.items()
→ dict_items([('nombre', 'edad', 'curso')])

📘 **¿Para qué sirven?**
-   `.keys()` → recorrer claves, validar existencia (`if "nombre" in mi_dict`)
    
-   `.values()` → buscar valores, estadísticas, filtrado
    
-   `.items()` → ideal para bucles `for clave, valor in mi_dict.items()`

# 🔁 **Recorrer estructuras**
for elemento in mi_lista:
    print(elemento)

for clave in mi_dict:
    print(clave, mi_dict[clave])

for clave, valor in mi_dict.items():
    print(f"{clave}: {valor}")

# 🧩 **Extras útiles**
# Copiar estructuras
nueva_lista = mi_lista.copy()
nuevo_dict = mi_dict.copy()

# Verificar existencia
if "nombre" in mi_dict:
    print("Existe la clave 'nombre'")

if 10 in mi_lista:
    print("El valor 10 está en la lista")
