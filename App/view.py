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

# Cargar


def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    datos = controller.loadData(filesize, control)
    return datos


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
    print(
        "Primeros " +
        str(N) +
        " artistas por popularidad:\n")
    for artist in lt.iterator(ai):
        print(
            str(i) +
            "." +
            '\nNombre: ' +
            artist['name'] +
            '\nGéneros: ' +
            artist['genres'] +
            '\nPopularidad: ' +
            artist['artist_popularity'] +
            '\nNúmero de seguidores: ' +
            artist['followers'])
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
            str(i) +
            "." +
            '\nNombre: ' +
            artist['name'] +
            '\nGéneros: ' +
            artist['genres'] +
            '\nPopularidad: ' +
            artist['artist_popularity'] +
            '\nNúmero de seguidores: ' +
            artist['followers'])
        i += 1


def dataReport(datos):
    printTracks(
        datos["num_tracks"],
        datos["tracks_3i"],
        datos["tracks_3f"])
    print("\n." * 5 + "\n")
    printArtists(
        datos["num_artists"],
        datos["artists_3i"],
        datos["artists_3f"])
    print("\n." * 5 + "\n")
    printAlbums(
        datos["num_albums"],
        datos["albums_3i"],
        datos["albums_3f"])

# Interfaz


def printMenu():
    print("\nBienvenido")
    print(
        "0- Seleccionar el tipo de representación de la lista")
    print("1- Cargar información en el catálogo")
    # print("2- Encontrar los artistas más populares")
    print("3- Encontrar las canciones mas populares")
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
        artists_liststr = input(
            "Estructura de datos para artists: ")
        tracks_liststr = input(
            "Estructura de datos para tracks: ")
        album_liststr = input(
            "Estructura de datos para albumes: ")
        filesize = input(
            "Archivo que se leerá (sufijo de tamaño): ")

    elif int(inputs[0]) == 1:
        # Se crea el controlador asociado a la vista
        control = controller.newController(
            artists_liststr, tracks_liststr, album_liststr)
        print(
            "Cargando información de los archivos ....")
        datos = loadData(filesize)
        report = input(
            "Desea imprimir del reporte de datos? (y/n) ")
        if report.lower() == "y":
            dataReport(datos)

    elif int(inputs[0]) == 3:
        while True:
            n = int(
                input("Cuantas canciones del top desea consultar? "))
            if 0 < n < datos["num_tracks"]:
                break
            else:
                print(
                    "por favor escoga un valor valido")
        controller.sortTracks(control)
        print("TOP 1",
              lt.getElement(
                  control["model"]["tracks"],
                  1)["name"])
        # TODO: IMPRIMIR CORERECTAMENTE LA
        # INFORMACIÓN
    elif int(inputs[0]) == 6:
        sort_type = input(
            "¿Qué tipo de ordenamiento desea usar (selection, insertion, shell, merge o quick)? ")
        print('Por favor espere . . .')
        time = controller.sortBy(sort_type, control)
        if bool(time):
            print(str(round(time, 2)) + ' ms')
        else:
            print("por favor escoga una opción valida")

    elif int(inputs[0]) == 2:
        N = int(
            input("¿Cuántos artistas desea visualizar? "))
        ai, af, lista = controller.rankingArtistas(
            control,
            N)
        printRanking(ai, af, lista, N)

    else:
        sys.exit(0)
