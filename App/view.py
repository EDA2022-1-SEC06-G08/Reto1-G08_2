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

#Crear controlador

def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control
# Se crea el controlador asociado a la vista
control = newController()


#Cargar

def loadData():
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f   = controller.loadData(control)
    return num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f


#Funciones de impresión

def printTracks(num, t_3i, t_f):
    
    print('Tracks cargadas: ' + str(num))
    print('Primeras 3 tracks' + t_3i)
    print("." + "\n." + "\n.")
    print('Últimas 3 tracks' + t_3f)

def printArtists(num, Ar_3i, Ar_f):
    
    print('Tracks cargadas: ' + str(num))
    print('Primeras 3 tracks' + Ar_3i)
    print("." + "\n." + "\n.")
    print('Últimas 3 tracks' + Ar_3f)

def printAlbums(num, Al_3i, Al_f):
    
    print('Tracks cargadas: ' + str(num))
    print('Primeras 3 tracks' + Al_3i)
    print("." + "\n." + "\n.")
    print('Últimas 3 tracks' + Al_3f)


#Interfaz

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f = loadData()
        printTracks(num_tracks, tracks_3i, tracks_3f)
        printArtists(num_artists, artists_3i, artists_3f)
        printAlbums(num_albums, albums_3i, albums_3f)


    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
