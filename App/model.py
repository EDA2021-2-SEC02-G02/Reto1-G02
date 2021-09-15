"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import datetime as dt
import time as time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as it
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qu

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    
    catalog = {"Artista":None,
                 "Obra":None }

    catalog['Artista']= lt.newList()
    catalog["Obra"]=lt.newList()


    return catalog

# Funciones para agregar informacion al catalogo
def addartista(catalog, artista, tipolista):
    if tipolista==1:
        artista={"ConstituentID": artista["ConstituentID"],
             "DisplayName": artista["DisplayName"],
             "Nacionality": artista["Gender"],
             "BeginDate":artista["BeginDate"],
             "EndDate": artista["EndDate"],
             "Artworks":lt.newList("ARRAY_LIST")}
        lt.addLast(catalog["Artista"],artista)

    if tipolista==2:
        artista={"ConstituentID": artista["ConstituentID"],
             "DisplayName": artista["DisplayName"],
             "Nacionality": artista["Gender"],
             "BeginDate":artista["BeginDate"],
             "EndDate": artista["EndDate"],
             "Artworks":lt.newList("LINKED_LIST")}
        lt.addLast(catalog["Artista"],artista)
    
# Funciones para creacion de datos
def addobra(catalog, obra):
    lt.addLast(catalog["Obra"],obra)

def sortdate (algoritmo,catalog,size):
    if algoritmo == "shellsort":
        sub_list = lt.subList(catalog["Obra"], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list=sa.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list

    if algoritmo == "insertionsort":
        sub_list = lt.subList(catalog["Obra"], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list=it.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list

    if algoritmo == "mergesort":
        sub_list = lt.subList(catalog["Obra"], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list=mg.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list

    if algoritmo == "quicksort":
        sub_list = lt.subList(catalog["Obra"], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list=qu.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list

def cmpArtworkByDateAcquired (obra1, obra2):
    if obra1["DateAcquired"]!= " " and obra2["DateAcquired"]!= " ":
        fecha1= dt.date.fromisoformat(obra1["DateAcquired"])
        fecha2= dt.date.fromisoformat(obra2["DateAcquired"])
        return fecha1<fecha2






# Funciones de consulta
# REQ. 1: listar cronológicamente los artistas 



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento