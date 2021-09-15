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
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        catalog=inicializar_catalogo()
        cargarinfo(catalog)
        print("Artistas cargados "+str(lt.size(catalog["Artista"])))
        print("Obras cargadas "+str(lt.size(catalog["Obra"])))


    elif int(inputs[0]) == 2:
        tipolista=input("Ingrese el tipo de lista: ")
        algoritmo=input("Ingrese el tipo de algoritmo: ")
        size=input("Ingrese el tamaño de la muestra: ")
        if size > size(catalog["Obra"]):
            print("El tamaño de la muestra excede el tamaño de los datos cargados"+ str(size(catalog["Obra"])))
        elif:
            

        


        pass

    else:
        sys.exit(0)
sys.exit(0)
