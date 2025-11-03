import csv
import os.path # chequear la existencia

"""
1. Gestion de archivos
"""
def leer_csv(paises_mundo_2023):
    paises = []
    if not os.path.exists(paises_mundo_2023):
        return paises   #Devuelve una lista vacia
    
    with open(paises_mundo_2023,'r',newline='',encoding='utf-8-sig') as f:     #lee los datos de los paises desde un archivo csv.
            lector = csv.DictReader(f)
            for fila in lector:
                if fila.get['nombre'] and fila.get['poblacion'] and fila.get['superficie_km2']:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie_km2'])
                    paises.append(fila)
            return paises

"""
Notas:
    - Si se devuelve una lista vacía, el archivo no fue encontrado.
    - No se utilizan excepciones
    - Se asume que los datos 'poblacion' y 'superficie' son números válidos en el CSV. 
      Si no lo son, el programa se detendrá (error ValueError) ya que no se manejan fallos.
"""
            
                        
                                #Cada pais debe tener las claves: nombre, poblacion, superfcie, continente.

def guardar_csv(archivo, lista_paises): #Guarda la lista actualizada de paises en el archivo leer_csv
    pass
                                        

"""
2. Gestion de paises ( altas y modificaciones)
"""
#agrega un nuevo pais a la lista
#nuevo_pais es un diccionario con las claves: nombre, poblacion, superficie, continente.
#valida que los campos no esten vacios y que el pais no exista previamente

def actualizar_pais(lista_paises, nombre, nueva_poblacion, nueva_superficie):
    pass
#Busca un pais por nombre y actualiza sus datos.
#Devuelve True si se actualizo correctamente,
#False si no se encontro  

"""
3. Busquedas y filtro
"""

def buscar_pais(lista_paises, nombre):
    pass
#Devuelve una lista de países cuyo nombre contenga
#el texto buscado (coincidencia parcial, sin distinción de mayúsculas).

def filtrar_por_continente(lista_paises, continente):
    pass
#   

def filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob):
    pass
    #Devuelve una lista de países cuya población esté dentro del rango.

def filtrar_por_rango_superficie(lista_paises, min_sup, max_sup):
    pass
    #Devuelve una lista de países cuya superficie esté dentro del rango.

#4. ORDENAMIENTOS


def ordenar_por_nombre(lista_paises, ascendente=True):
    pass
"""
Devuelve una nueva lista ordenada por nombre de país.
"""


def ordenar_por_poblacion(lista_paises, ascendente=True):
    pass
"""
Devuelve una nueva lista ordenada por población.
"""


def ordenar_por_superficie(lista_paises, ascendente=True):
    pass
"""
Devuelve una nueva lista ordenada por superficie.
"""



#5. ESTADÍSTICAS

def pais_mayor_poblacion(lista_paises):
    pass
"""
Devuelve el país con mayor población.
"""


def pais_menor_poblacion(lista_paises):
    pass
"""
Devuelve el país con menor población.
"""


def promedio_poblacion(lista_paises):
    pass
"""
Devuelve el promedio de población.
"""


def promedio_superficie(lista_paises):
    pass
"""
Devuelve el promedio de superficie.
"""


def cantidad_por_continente(lista_paises):
    pass
"""
Devuelve un diccionario con la cantidad de países por continente.
Ejemplo: {"América": 5, "Europa": 3, ...}
"""


#6. VALIDACIONES (opcional)


def validar_entero(valor):
    pass
"""
Verifica si el valor puede convertirse a entero.
Devuelve True o False.
"""
    

def validar_no_vacio(texto):
    pass
"""
Verifica que el texto no esté vacío ni solo contenga espacios.
"""

