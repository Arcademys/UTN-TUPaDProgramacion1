"""
1. Gestion de archivos
"""
def leer_csv(archivo):  #lee los datos de los paises desde un archivo csv.
                        #Devuelve una lista de diccionarios
                        #Cada pais debe tener las claves: nombre, poblacion, superfcie, continente.

def guardar_csv(archivo, lista_paises): #Guarda la lista actualizada de paises en el archivo leer_csv
                                        #no devuelve

"""
2. Gestion de paises ( altas y modificaciones)
"""
#agrega un nuevo pais a la lista
#nuevo_pais es un diccionario con las claves: nombre, poblacion, superficie, continente.
#valida que los campos no esten vacios y que el pais no exista previamente

def actualizar_pais(lista_paises, nombre, nueva_poblacion, nueva_superficie):
#Busca un pais por nombre y actualiza sus datos.
#Devuelve True si se actualizo correctamente,
#False si no se encontro  

"""
3. Busquedas y filtro
"""

def buscar_pais(lista_paises, nombre):
#Devuelve una lista de países cuyo nombre contenga
#el texto buscado (coincidencia parcial, sin distinción de mayúsculas).

def filtrar_por_continente(lista_paises, continente):
#   

def filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob):
    #Devuelve una lista de países cuya población esté dentro del rango.

def filtrar_por_rango_superficie(lista_paises, min_sup, max_sup):
    #Devuelve una lista de países cuya superficie esté dentro del rango.

4. ORDENAMIENTOS
------------------------------------------------------------

def ordenar_por_nombre(lista_paises, ascendente=True):
"""
Devuelve una nueva lista ordenada por nombre de país.
"""
pass

def ordenar_por_poblacion(lista_paises, ascendente=True):
"""
Devuelve una nueva lista ordenada por población.
"""
pass

def ordenar_por_superficie(lista_paises, ascendente=True):
"""
Devuelve una nueva lista ordenada por superficie.
"""
pass

------------------------------------------------------------
5. ESTADÍSTICAS
------------------------------------------------------------

def pais_mayor_poblacion(lista_paises):
"""
Devuelve el país con mayor población.
"""
pass

def pais_menor_poblacion(lista_paises):
"""
Devuelve el país con menor población.
"""
pass

def promedio_poblacion(lista_paises):
"""
Devuelve el promedio de población.
"""
pass

def promedio_superficie(lista_paises):
"""
Devuelve el promedio de superficie.
"""
pass

def cantidad_por_continente(lista_paises):
"""
Devuelve un diccionario con la cantidad de países por continente.
Ejemplo: {"América": 5, "Europa": 3, ...}
"""
pass

------------------------------------------------------------
6. VALIDACIONES (opcional)
------------------------------------------------------------

def validar_entero(valor):
"""
Verifica si el valor puede convertirse a entero.
Devuelve True o False.
"""
pass

def validar_no_vacio(texto):
"""
Verifica que el texto no esté vacío ni solo contenga espacios.
"""
pass
