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
import csv
import controller
from DISClib.ADT import list as lt
assert cf

maxInt = sys.maxsize

while True:

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# Crear controlador


def newController(artists_liststr):
    """
    Se crea una instancia del controlador
    """
    control = controller.newController(
        artists_liststr)
    return control


# Cargar

def loadData(filesize):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f = controller.loadData(
        filesize, control)
    return num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f


# Funciones de impresión

def printTracks(num, t_3i, t_3f):

    print('Tracks cargadas: ' + str(num) + '\n')
    print('Primeras 3 canciones: ')
    for track in lt.iterator(t_3i):
        print(
            'Nombre: ' +
            track['name'] +
            '\nPaíses donde está disponible: ' +
            track['available_markets'] +
            '\nDuración: ' +
            track['duration_ms'] +
            '\nID en el álbum: ' +
            track['album_id'])
    print("\n." * 5 + "\n")
    print('Últimas 3 canciones: ')
    for track in lt.iterator(t_3f):
        print(
            'Nombre: ' +
            track['name'] +
            '\nPaíses donde está disponible: ' +
            track['available_markets'] +
            '\nDuración: ' +
            track['duration_ms'] +
            '\nID en el álbum: ' +
            track['album_id'])


def printArtists(num, Ar_3i, Ar_3f):

    print('Artistas cargados: ' + str(num) + '\n')
    print('Primeros 3 artistas')
    for artist in lt.iterator(Ar_3i):
        print(
            'Nombre: ' +
            artist['name'] +
            '\nGéneros: ' +
            artist['genres'] +
            '\nPopularidad: ' +
            artist['artist_popularity'] +
            '\nNúmero de seguidores: ' +
            artist['followers'])
    print("\n." * 5 + "\n")
    print('Últimos 3 artistas')
    for artist in lt.iterator(Ar_3f):
        print(
            'Nombre: ' +
            artist['name'] +
            '\nGéneros: ' +
            artist['genres'] +
            '\nPopularidad: ' +
            artist['artist_popularity'] +
            '\nNúmero de seguidores: ' +
            artist['followers'])


def printAlbums(num, Al_3i, Al_3f):

    print('Álbumes cargados: ' + str(num) + '\n')
    print('Primeros 3 álbumes')
    for album in lt.iterator(Al_3i):
        print(
            'Nombre: ' +
            album['name'] +
            '\nTipo de álbum: ' +
            album['album_type'] +
            '\nMercados donde está disponible: ' +
            album['available_markets'] +
            '\nFecha de lanzamiento: ' +
            album['release_date'])
    print("\n." * 5 + "\n")
    print('Últimos 3 álbumes')
    for album in lt.iterator(Al_3f):
        print(
            'Nombre: ' +
            album['name'] +
            '\nTipo de álbum: ' +
            album['album_type'] +
            '\nMercados donde está disponible: ' +
            album['available_markets'] +
            '\nFecha de lanzamiento: ' +
            album['release_date'])


# Interfaz

def printMenu():
    print("\nBienvenido")
    print(
        "0- Seleccionar el tipo de representación de la lista")
    print("1- Cargar información en el catálogo")
    # print("2- Encontrar los artistas más populares")
    # print("3- Clasificar las canciones por popularidad")
    # print(
    #     "4- Encontrar la canción más popular de un artista")
    # print("5- Encontrar la discografía de un artista")
    print("6- Ordenar la lista de artistas\n")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input(
        'Seleccione una opción para continuar\n')

    if int(inputs[0]) == 0:
        artists_listsrt = input(
            "Estructura de datos para artists: ")
        filesize = input(
            "Archivo que se leerá (sufijo de tamaño): ")

    elif int(inputs[0]) == 1:
        # Se crea el controlador asociado a la vista
        control = newController(artists_listsrt)
        print(
            "Cargando información de los archivos ....\n")
        num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f = loadData(
            filesize)
        printTracks(num_tracks, tracks_3i, tracks_3f)
        print("\n." * 10 + "\n")
        printArtists(
            num_artists,
            artists_3i,
            artists_3f)
        print("\n." * 10 + "\n")
        printAlbums(num_albums, albums_3i, albums_3f)

    elif int(inputs[0]) == 6:
        sort_type = input(
            "¿Qué tipo de ordenamiento desea usar (selection, insertion o shell)? ")
        if sort_type == 'selection':
            print('Por favor espere . . .')
            time = controller.selection_sort(control)
            print(str(round(time, 2)) + ' ms')
        elif sort_type == 'insertion':
            print('Por favor espere . . .')
            time = controller.insertion_sort(control)
            print(str(round(time, 2)) + ' ms')
        elif sort_type == 'shell':
            print('Por favor espere . . .')
            time = controller.shell_sort(control)
            print(str(round(time, 2)) + ' ms')
        else:
            print(
                'Por favor seleccione una opción válida')

    else:
        sys.exit(0)
