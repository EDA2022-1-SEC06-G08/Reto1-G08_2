﻿"""
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

from controller import getFirst, getLast
import config as cf
import sys
import csv
import controller
import time
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

# Cargar


def loadData(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    datos = controller.loadData(control)
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


def printRanking(lista, N, control):
    i = 1
    print(
        "\n\nPrimeros " +
        str(N) +
        " artistas por popularidad:\n")
    if N < 7:
        for artist in lt.iterator(lista):
            cancion_referente = controller.findMainTrack(
                artist['track_id'], control)
            if cancion_referente is None:
                cancion_referente = "Canción no encontrada"
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
                artist['followers'] +
                '\nCanción referente: ' +
                cancion_referente)
            i += 1
    else:
        size = lt.size(lista)
        ai = getFirst(lista)
        for artist in lt.iterator(ai):
            cancion_referente = controller.findMainTrack(
                artist['track_id'], control)
            if cancion_referente is None:
                cancion_referente = "Canción no encontrada"
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
                artist['followers'] +
                '\nCanción referente: ' +
                cancion_referente)
            i += 1
        print(".")
        for pos in range(4, size - 2):
            print(
                str(i) + "." +
                lt.getElement(lista, pos)['name'])
            i += 1
        print(".")
        af = getLast(lista)
        for artist in lt.iterator(af):
            cancion_referente = controller.findMainTrack(
                artist['track_id'], control)
            if cancion_referente is None:
                cancion_referente = "Canción no encontrada"
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
                artist['followers'] +
                '\nCanción referente: ' +
                cancion_referente)
            i += 1


def printAlbumsTimeSpan(total, control):
    size = lt.size(total)
    print(
        "\n\nNúmero total de álbumes en el periodo: " +
        str(size))
    if size > 6:
        print("\nPrimeros 3 albumes: ")
        ai = getFirst(total)
        i = 0
        for album in lt.iterator(ai):
            i += 1
            artista_principal = controller.findMainArtist(
                album['artist_id'], control)
            if artista_principal is None:
                artista_principal = 'Artista no encontrado'
            print(
                str(i) + "." + '\nNombre: ' +
                album['name'] +
                '\nFecha de publicación: ' +
                album['release_date'] +
                '\nTipo de album: ' +
                album['album_type'] +
                '\nArtista principal asociado: ' +
                artista_principal +
                '\nNúmero de canciones: ' +
                album['total_tracks'])

        print("\nÚltimos 3 albumes: ")
        af = getLast(total)
        i = size - 3
        for album in lt.iterator(af):
            i += 1
            artista_principal = controller.findMainArtist(
                album['artist_id'], control)
            if artista_principal is None:
                artista_principal = 'Artista no encontrado'
            print(
                str(i) + "." + '\nNombre: ' +
                album['name'] +
                '\nFecha de publicación: ' +
                album['release_date'] +
                '\nTipo de album: ' +
                album['album_type'] +
                '\nArtista principal asociado: ' +
                artista_principal +
                '\nNúmero de canciones: ' +
                album['total_tracks'])

    else:
        i = 0
        for album in lt.iterator(total):
            i += 1
            artista_principal = controller.findMainArtist(
                album['artist_id'], control)
            if artista_principal is None:
                artista_principal = 'Artista no encontrado'
            print(
                str(i) + "." + '\nNombre: ' +
                album['name'] +
                '\nFecha de publicación: ' +
                album['release_date'] +
                '\nTipo de album: ' +
                album['album_type'] +
                '\nArtista principal asociado: ' +
                artista_principal +
                '\nNúmero de canciones: ' +
                album['total_tracks'])


def printBestTrack(
        best_track,
        numTracks,
        numAlbums,
        album,
        involved_artists,
        artist,
        market):
    #artist_name = artist['name']
    release_date = controller.dateFormat(
        album['release_date'],
        album['release_date_precision'])
    if best_track['lyrics'] == '-99':
        lyrics = "Letra de la canción NO disponible"
    else:
        lyrics = best_track['lyrics']
    # TODO: album, involved artists
    print(
        'El número total de canciones asociadas a',
        artist,
        'es:',
        numTracks)
    print('El número total de álbumes de',
          artist, 'es:', numAlbums)
    print(
        '\nLa mejor canción de',
        artist,
        'diponible en el mercado de',
        market,
        'es la siguiente:')
    print('Nombre', best_track['name'])
    print(
        'Nombre del álbum de la canción:',
        album['name'])
    print('Fecha de publicación:', release_date)
    print('Artistas Involucrados:')
    for i in lt.iterator(involved_artists):
        print(i['name'])
    print(
        'Tiempo de duración (ms):',
        best_track['duration_ms'])
    print('Popularidad:', best_track['popularity'])
    print(
        'Enlace al audio de muestra:',
        best_track['preview_url'])
    print('Letra de la canción', lyrics)


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

# Funciones de tiempo


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter() * 1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Interfaz

def printMenu():
    print("\nBienvenido")
    print("0- Cargar el archivo")
    print(
        "1- Encontrar los álbumes en un periodo de tiempo")
    print("2- Encontrar los artistas más populares")
    print("3- Encontrar las canciones mas populares")
    print(
        "4- Encontrar la canción más popular de un artista")
    print("5- Encontrar la discografía de un artista")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input(
        'Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        # Se crea el controlador asociado a la vista
        control = controller.newController()
        print(
            "Cargando información de los archivos ....")
        datos = loadData(control)
        report = input(
            "Desea imprimir del reporte de datos? (y/n) ")
        if report.lower() == "y":
            dataReport(datos)

    elif int(inputs[0]) == 1:
        anio_i = int(
            input(
                "¿Desde qué año desea realizar su busqueda? (Por favor escriba los 4 dígitos del año) "))
        anio_f = int(
            input(
                "¿Hasta qué año desea realizar su búsqueda? (Por favor escriba los 4 dígitos del año) "))
        if anio_f < anio_i or anio_i < 1886 or anio_f > 2019:
            print(
                "Por favor introduzca un intervalo de tiempo válido")
        else:
            time1 = getTime()
            numTotal = controller.albumsInTimeSpan(
                anio_i,
                anio_f,
                control)
            printAlbumsTimeSpan(numTotal, control)
            time2 = getTime()
            print(deltaTime(time1, time2))

    elif int(inputs[0]) == 2:
        N = int(
            input("¿Cuántos artistas desea visualizar? "))
        if N < 1 or N > 56129:
            print(
                "Por favor ingrese un número válido de artistas")
        else:
            time1 = getTime()
            lista = controller.rankingArtistas(
                control, N)
            printRanking(lista, N, control)
            time2 = getTime()
            print(deltaTime(time1, time2))

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

        top = controller.topTracks(control, n)

        for track in range(lt.size(top)):
            trackInfo = lt.getElement(top, track)

            if n <= 6:
                print("Canción #", track + 1)
            else:
                if track + 1 <= 3:
                    print("Canción #", track + 1)
                else:
                    print(
                        "Canción #",
                        track + 1 + n - 6)
            for info in trackInfo:
                print(info, ":", trackInfo[info])

    elif int(inputs[0]) == 4:
        artist = input(
            "Introduzca el artista que desea analizar: ")
        market = input(
            "Introduzca las dos siglas del mercado que desea analizar (Alpha 2): ")

        time1 = getTime()
        best_track, numTracks, numAlbums, album, involved_artists = controller.findBestTrack(
            artist, market, control)
        if best_track is None:
            print("Artista no encontrado")
        else:
            printBestTrack(
                best_track,
                numTracks,
                numAlbums,
                album,
                involved_artists,
                artist,
                market)
            time2 = getTime()
            print(deltaTime(time1, time2))

    elif int(inputs[0]) == 5:
        artist = input(
            "Introduzca el artista que desea analizar: ")

        controller.sortTracks(control)
        discography, albumes = controller.findDiscography(
            control, artist)

        print("Este artista tiene:")

        for type in discography:
            print(discography[type], type)

        for album in range(lt.size(albumes)):
            albumInfo = lt.getElement(albumes, album)

            if lt.size(albumes) <= 6:
                print("Album #", album + 1)
            else:
                if album + 1 <= 3:
                    print("Album #", album + 1)
                else:
                    print(
                        "Album #",
                        album +
                        1 +
                        lt.size(albumes) -
                        6)

            for info in albumInfo:
                print(info, ":", albumInfo[info])
                print()

    else:
        sys.exit(0)
