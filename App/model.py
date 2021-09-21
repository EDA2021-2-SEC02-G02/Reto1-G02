﻿"""
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

    catalog['Artista']= lt.newList("ARRAY_LIST", cmpfunction=compareartworks)
    catalog["Obra"]=lt.newList("ARRAY_LIST")


    return catalog

# Funciones para agregar informacion al catalogo
def addartista(catalog, artistas):
        artista={"ConstituentID": artistas["ConstituentID"],
             "DisplayName": artistas["DisplayName"],
             "Nacionality": artistas["Gender"],
             "BeginDate":artistas["BeginDate"],
             "EndDate": artistas["EndDate"],
             "Gender": artistas["Gender"],
             "Artworks":lt.newList("ARRAY_LIST")}
        lt.addLast(catalog["Artista"],artista)
    

def addobra(catalog, obras):
        obra={"ObjectID":obras["ObjectID"],
          "Title": obras ["Title"],
          "ConstituentID": obras ["ConstituentID"][1:-1],
          "Date": obras["Date"],
          "Medium": obras["Medium"],
          "Dimensions": obras["Dimensions"],
          "CreditLine": obras["CreditLine"],
          "Classification": obras["Classification"],
          "Department": obras["Department"],
          "DateAcquired": obras["DateAcquired"],
          "Weight":obras["Weight"]}
        lt.addLast(catalog["Obra"],obra)  
        IDartista= obra["ConstituentID"].split(",")
        for artista in IDartista:
            addArtworkartist(catalog, artista, obra)
      
def addArtworkartist(catalog, IDartista, obra):
    artistas=catalog["Artista"]
    posicion=lt.isPresent(artistas, IDartista)
    if posicion>0:
      artista= lt.getElement(artistas, posicion)
      lt.addLast(artista["Artworks"], obra)

def compareartworks(ID,artistas):
    if (ID in artistas["ConstituentID"]):
      return 0
    return -1


# Funciones para creacion de datos  
# REQ. 1: listar cronológicamente los artistas  
 
def addartistyear(catalog, año1, año2):
    artistsinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Artista"]):
        artista=lt.getElement(catalog["Artista"],i)
        if int(artista["BeginDate"])>= año1 and int(artista["BeginDate"])<=año2:
            lt.addLast(artistsinrange, artista)
    sortedlist=sortyear(artistsinrange)
    return sortedlist

  # Funciones de ordenamiento
def sortyear (artistsinrange):
        sub_list = lt.subList(artistsinrange, 1, lt.size(artistsinrange))
        sub_list = sub_list.copy()
        sorted_list=mg.sort(sub_list, cmpArtworkByBeginDate)
        return sorted_list

  # Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByBeginDate (date1, date2):
    if date1["BeginDate"]!= "" and date2["BeginDate"]!= "":
        year1= int((date1["BeginDate"]))
        year2= int((date2["BeginDate"]))
        return year1<year2 


#REQ. 2: listar cronológicamente las adquisiciones 
def addartworkyear(catalog, fecha1,fecha2):
    artworksinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Obra"]):
        obra=lt.getElement(catalog["Obra"],i)
        enfecha=dt.date.fromisoformat(obra["DateAcquired"])
        if enfecha>= fecha1 and enfecha<= fecha2:
            lt.addLast(artworksinrange, obra)
    sortlist=sortdate(artworksinrange)
    return sortlist

  #encontrar número de obras compradas
def purchaseart (listaordenada2):
    i=1
    n=0
    while i<=lt.size(listaordenada2):
        obra=lt.getElement(listaordenada2,i)
        i+=1
        if obra["CreditLine"]=="Purchase":
            n+=1
    return n
    
  # Funciones de ordenamiento
def sortdate (artworksinrange):
    sub_list = lt.subList(artworksinrange, 1,lt.size(artworksinrange))
    sub_list = sub_list.copy()
    sorted_list=mg.sort(sub_list, cmpArtworkByDateAcquired)
    return sorted_list

  # Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired (obra1, obra2):
    if obra1["DateAcquired"]!= "" and obra2["DateAcquired"]!= "":
        fecha1= dt.date.fromisoformat(obra1["DateAcquired"])
        fecha2= dt.date.fromisoformat(obra2["DateAcquired"])
        return fecha1<fecha2

#REQ. 3: clasificar las obras de un artista por técnica (Individual)
# Total de obras
def totalobrasartista (catalog, name):
    artistas=catalog["Artista"]
    for artista in artistas:
        if artista["DisplayName"] ==name:
           tamaño=lt.size(artista["Artworks"])
        return tamaño

# Total técnicas (medios) utilizados.
def totalmedium (catalog, name):
    listamedium= lt.newList("ARRAY_LIST")
    artistas=catalog["Artista"]
    for artista in artistas:
      if name == artista["DisplayName"]:
        artw=artista["Artworks"]
        for artone in artw:
           medio=artone["Medium"]
           if medio not in listamedium:
             lt.addLast(listamedium,medio)
      
#La técnica mas utilizada
def tecnicarepetida(catalog, name):
    listatecn= lt.newList("ARRAY_LIST")
    artistas=catalog["Artista"]
    for artista in artistas:
      if name == artista["DisplayName"]:
        artw=artista["Artworks"]
        for artone in artw:
           medio=artone["Medium"]
           lt.addLast(listatecn, medio)

#cómo hago para saber cual medio es que más se repite en la lista
def encontrarrepetido(listamedium):
  mayor=""
  valor=0
  for medio in listamedium:
    if medio 

#El listado de las obras de dicha técnica
#Ya llegué a saber si esa obra tiene el medio repetido, pero cómo hago para saber su nombre, fecha, etc
def listado(name, catalog, repetido):
   lista=lt.newList("ARRAY_LIST")
   artistas=catalog["Artista"]
   for artista in artistas:
      if name == artista["DisplayName"]:
        artw=artista["Artworks"]
        for artone in artw:
          if artone ==repetido


#REQ. 5: transportar obras de un departamento
#Total de obras para transportar (size de esto)
def totalobras(catalog, depto):
   listaobras= lt.newList("ARRAY_LIST")
   obras=catalog["Obra"]
   for obra in obras:
     if obra["Department"]==depto:
       lt.addLast(listaobras,obra)
   return listaobras

#Estimado en USD del precio del servicio
#Cómo hago para obtener las dimendiones
def price (listaobras):
  costototal=0
  for obra in listaobras:
     medida=int(obra["Dimensions"])
     if medida ==0:
        costo=48
     else:
        costo=(medida/100)*72
     costototal+=costo
    
def weight (listaobras):
  pesototal=0
  for obra in listaobras:
    peso=int(obra["Weight"])
    pesototal+=peso
  return pesototal

def oldest(listaobras):
  sub_list = lt.subList(listaobras, 1,lt.size(listaobras))
  sub_list = sub_list.copy()
  sorted_list=mg.sort(sub_list, cmpArtworkByDate)
  return sorted_list

def cmpArtworkByDate(obra1, obra2):
   if obra1["Date"]!= "" and obra2["Date"]!= "":
        fecha1= dt.date.fromisoformat(obra1["Date"])
        fecha2= dt.date.fromisoformat(obra2["Date"])
        return fecha1>fecha2 





   






