"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """



import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Listar cronologicamente los artistas")
    print("2- Listar cronologicamente las adquisiciones")
    print("3- Clasificar obras de un artista por técnica")
    print("4- Clasificar las obras por nacionalidad de sus creadores")
    print("5- Transportar obras de un departamento")
    print("6- Proponer una nueva exposición en el museo")


def inicializar_catalogo():
    return controller.initcatalog()

def cargarinfo(catalog):
    controller.loaddata(catalog)

catalog=None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

#Carga de datos
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        catalog=inicializar_catalogo()
        cargarinfo(catalog)
        print("Artistas cargados "+str(lt.size(catalog["Artista"])))
        print("Obras cargadas "+str(lt.size(catalog["Obra"])))

    elif int(inputs[0]) == 1:
        año1= int(input("Ingrese el año inicial del que desea organizar los artistas: "))
        año2= int(input("Ingrese el año final del que desea organizar los artistas: "))
        print("Buscando....")
        lista1=controller.addartistyear(catalog, año1, año2)
        nartistas=lt.size(lista1)
        print("El número total de artistas en dicho rango es de: "+ str(nartistas)+", los 3 primeros artistas del rango cronológico (nombre, año de nacimiento, año de fallecimiento, nacionalidad y género) son: ")
        #if
        tresfirst1=(lt.getElement(lista1,1),lt.getElement(lista1,2),lt.getElement(lista1,3))
        for artistaF in tresfirst1:
            print(artistaF["DisplayName"], artistaF["BeginDate"], artistaF["EndDate"], artistaF["Nationality"], artistaF["Gender"])
        print("los 3 últimos artistas del rango cronológico (nombre, año de nacimiento, año de fallecimiento, nacionalidad y género) son: ")
        treslast1=(lt.getElement(lista1,nartistas) ,lt.getElement(lista1,nartistas-1),lt.getElement(lista1,nartistas-2))
        for artistaL in treslast1:
            print(artistaL["DisplayName"], artistaL["BeginDate"], artistaL["EndDate"], artistaL["Nationality"], artistaL["Gender"])

#solo nombre
    elif int(inputs[0]) == 2:
        fecha1= input("Ingrese la fecha inicial (AAAA MM DD): ")
        fecha2= input("Ingrese la fecha final (AAAA MM DD): ")
        print("Creando lista ....")
        lista2= controller.addartworkyear(catalog, fecha1, fecha2)
        Nobrascompra=controller.purchaseart(lista2)
        tamaño=lt.size(lista2)
        print("El número total de obras en el rango cronológico es de: "+ str(tamaño)+", El número total de obras adquiridas por compra es de "+str(Nobrascompra)+", La tres primeras obras del rango cronológico (título, artista(s), fecha, medio y dimensiones) son: ") 
        tresfirst2= (lt.getElement(lista2,1),lt.getElement(lista2,2),lt.getElement(lista2,3))
        for obraF in tresfirst2:
            print(obraF["Title"], obraF["Date"], obraF["Medium"], obraF["Dimensions"])
            print("Los artistas de la obra son: ")
            for artist in lt.iterator(obraF["Artists"]):
                print(artist["DisplayName"])
        #print(". La tres últimas obras del rango cronológico (título, artista(s), fecha, medio y dimensiones) son: " )
        treslast2=(lt.getElement(lista2,tamaño),lt.getElement(lista2,tamaño-1),lt.getElement(lista2,tamaño-2))
        for obraL in treslast2:
            print(obraL["Title"],  obraL["Date"], obraL["Medium"], obraL["Dimensions"])
            print("Los artistas de la obra son: ")
            for artist in lt.iterator(obraF["Artists"]):
                print(artist["DisplayName"])

    elif int(inputs[0]== 3):
       name=input("Ingrese el nombre del artista: ")
       totalobras=controller.totalobrasartista(catalog, name)
       totalmedio=lt.size(controller.totalmedium(catalog, name))
       print("El total de obras del artista "+name+"es de: "+str(totalobras)+", el total de técnicas utilizadas por el artista es de: "+str(totalmedium) )



    #elif int(inputs[0]== 4):


    #Cómo incluyo el precio y los artistas?
    elif int(inputs[0]== 5):
       depto=input("Ingrese el departamento del museo que desea transportar: ")
       listaobras=controller.totalobras(catalog, depto)
       obrastransport=lt.size(listaobras)
       price=controller.price(listaobras)
       weight=controller.weight(listaobras)
       print("El total de obras para transportar es de: "+str(obrastransport)+", el Estimado en USD del precio del servicio es de: "+str(price)+" y el peso estimado de las obras es de: "+str(weight))
       oldest=controller.oldest(listaobras)
       fiveoldest=(lt.getElement(oldest,1),lt.getElement(oldest,2), lt.getElement(oldest,3), lt.getElement(oldest,4), lt.getElement(oldest,5))
       print(". Las 5 obras más antiguas a transportar son (Título, artista(s), clasificación, fecha de la obra, medio, dimensiones, costo asociado al transporte): ")
       for obra in fiveoldest:
           print(obra["Title"], obra["Artists"], obra["Classification"], obra["Date"], obra["Medium"], obra["Dimensions"], obra[""])
    
    else:
        sys.exit(0)
sys.exit(0)
