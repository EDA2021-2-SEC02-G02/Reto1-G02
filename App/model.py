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

    catalog['Artista']= lt.newList("ARRAY_LIST", cmpfunction=compareartworks)
    catalog["Obra"]=lt.newList("ARRAY_LIST")


    return catalog

# Funciones para agregar informacion al catalogo
def addartista(catalog, artistas):
        artista={"ConstituentID": artistas["ConstituentID"],
             "DisplayName": artistas["DisplayName"],
             "Nationality": artistas["Nationality"],
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
          "Weight":obras["Weight (kg)"],
          "Artists":lt.newList("ARRAY_LIST")}
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
      lt.addLast(obra["Artists"], artista)

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
        i+=1
    sortedlist=sortyear(artistsinrange)
    return sortedlist

  # Funciones de ordenamiento
def sortyear (artistsinrange):
        sorted_list=mg.sort(artistsinrange, cmpArtworkByBeginDate)
        return sorted_list

  # Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByBeginDate (date1, date2):
    if date1["BeginDate"]!= "" and date2["BeginDate"]!= "":
        year1= int((date1["BeginDate"]))
        year2= int((date2["BeginDate"]))
        return year1<year2 


#REQ. 2: listar cronológicamente las adquisiciones 
def addartworkyear(catalog, fecha1,fecha2):
    fecha1=dt.date.fromisoformat(fecha1)
    fecha2=dt.date.fromisoformat(fecha2)
    artworksinrange=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Obra"]):
        obra=lt.getElement(catalog["Obra"],i)
        if obra["DateAcquired"]!="":
           enfecha=dt.date.fromisoformat(obra["DateAcquired"])
           if enfecha>= fecha1 and enfecha<= fecha2:
               lt.addLast(artworksinrange, obra)
        i+=1
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
    sorted_list=mg.sort(artworksinrange, cmpArtworkByDateAcquired)
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
    obras=lt.newList("ARRAY_LIST")
    i=1
    while i<= lt.size(catalog["Artista"]):
        artista=lt.getElement(catalog["Artista"],i)
        if artista["DisplayName"]== name:
            obras=artista["Artworks"]
        i+=1
    return obras

#Total técnicas (medios) utilizados
def totalmedios(obras):
    tecnicas=lt.newList("ARRAY_LIST", cmpfunction=cmpmediums)
    j=1
    while j <=lt.size(obras):
      obra=lt.getElement(obras,j)
      tecnica=obra["Medium"]
      posicion=lt.isPresent(tecnicas,tecnica)
      if posicion>0:
          tec=lt.getElement(tecnicas, posicion)
          tec["valor"]+=1
      else:
          tec={"Nombre":tecnica,"valor":1}
          lt.addLast(tecnicas, tec)
      j+=1
    sortedlist=sorttecnicas(tecnicas)
    return sortedlist

def sorttecnicas(tecnicas):
   sortedlist=mg.sort(tecnicas, cmptecnicas)
   return sortedlist

def cmptecnicas( tecnica1, tecnica2):
    if tecnica1["valor"]>=tecnica2["valor"]:
       return True
    else:
       return False
  
def cmpmediums (tecnica1,tecnica2):
  if tecnica1== tecnica2["Nombre"]:
    return 0
  else:
    return 1

#La técnica mas utilizada  
def primeratecnica (sortedlist):
   nombre=lt.firstElement(sortedlist)
   nombre=nombre["Nombre"]
   return nombre

#El listado de las obras de dicha técnica
def obrastecnica(nombre,obras):
  listaobras=lt.newList("ARRAY_LIST")
  for obra in lt.iterator(obras):
    if obra["Medium"]==nombre:
      lt.addLast(listaobras,obra)
  return listaobras
    

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
#def price (listaobras):
   # kgprice=0
   # m2price=0
    #m3price=0
    #totalprice=0
    #totalweight=0
    #costo=72
    #for obra in listaobras:
     #  weight=obra["Weight (kg)"]
      # diameter=obra["Diameter (cm)"]
       #circumference=obra["Circumference (cm)"]
    #   length=obra["Length (cm)"]
     #  height=obra["Height (cm)"]
     #  width=obra["Width (cm)"]
      # depth=obra["Depth (cm)"]
      # if weight !="":
      
