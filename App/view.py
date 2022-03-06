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

# Se crea el controlador asociado a la vista

def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

control = newController()

# Cargar

def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f = controller.loadData(control)
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

def printRanking(ai, af, lista, N):
    i = 1
    size = lt.size(lista)
    print("Primeros " + str(N) + " artistas por popularidad:\n")
    for artist in lt.iterator(ai):
        print(
            str(i) + "." +
            '\nNombre: ' + artist['name'] +
            '\nGéneros: ' + artist['genres'] +
            '\nPopularidad: ' + artist['artist_popularity'] +
            '\nNúmero de seguidores: ' + artist['followers'])
        i += 1
    print(".")
    for pos in range(4, size - 2):
        print(
            str(i) + "." +
            lt.getElement(lista, pos)['name'])
        i += 1
    print(".")
    for artist in lt.iterator(af):
        print(
            str(i) + "." +
            '\nNombre: ' + artist['name'] +
            '\nGéneros: ' + artist['genres'] +
            '\nPopularidad: ' + artist['artist_popularity'] +
            '\nNúmero de seguidores: ' + artist['followers'])
        i += 1


# Interfaz

def printMenu():
    print("\nBienvenido")
    print("0- Cargar información en el catálogo")
    print("2- Encontrar los artistas más populares")
    # print("3- Clasificar las canciones por popularidad")
    # print(
    #     "4- Encontrar la canción más popular de un artista")
    # print("5- Encontrar la discografía de un artista")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input(
        'Seleccione una opción para continuar\n')

    if int(inputs[0]) == 0:
        print(
            "Cargando información de los archivos ....\n")
        num_tracks, num_artists, num_albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f = loadData(control)
        printTracks(num_tracks, tracks_3i, tracks_3f)
        print("\n." * 10 + "\n")
        printArtists(
            num_artists,
            artists_3i,
            artists_3f)
        print("\n." * 10 + "\n")
        printAlbums(num_albums, albums_3i, albums_3f)

    elif int(inputs[0]) == 1:
        pass

    elif int(inputs[0]) == 2:
        N = int(input("¿Cuántos artistas desea visualizar? "))
        ai, af, lista = controller.rankingArtistas(control, N)
        printRanking(ai, af, lista, N)
    
    else:
        sys.exit(0)
