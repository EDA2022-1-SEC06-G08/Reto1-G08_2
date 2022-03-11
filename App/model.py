
#  * Copyright 2020, Departamento de sistemas y Computación,
#  * Universidad de Los Andes
#  *
#  *
#  * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
#  *
#  *
#  * This program is free software: you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License as published by
#  * the Free Software Foundation, either version 3 of the License, or
#  * (at your option) any later version.
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
#  *
#  * Contribuciones:
#  *
#  * Dario Correal - Version inicial


import csv
import config as cf
import sys
import datetime as dt
from datetime import datetime as DT
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import (
    shellsort as sh,
    insertionsort as ins,
    selectionsort as se,
    mergesort as me,
    quicksort as qu
)
from DISClib.Algorithms.Search import binarysearch as bi
assert cf

maxInt = sys.maxsize

while True:

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


# Se define la estructura de un catálogo de videos.
# El catálogo tendrá dos listas, una para los videos,
# otra para las categorias de los mismos.


# Construccion de modelos


def newCatalog():

    # Inicializa el catálogo. Crea una lista vacia
    # para guardar todos los tracks, adicionalmente,
    # crea una lista vacia para los artist y una
    # lista vacia para los álbumes. Retorna el
    # catalogo inicializado.

    catalog = {'tracks': None,
               'artists': None,
               'albums': None}

    catalog['tracks'] = lt.newList("ARRAY_LIST")
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['albums'] = lt.newList('ARRAY_LIST')

    return catalog


def addTrack(catalog, track):
    # Se adiciona el track a la lista de tracks
    lt.addLast(catalog['tracks'], track)
    return catalog


def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)
    return catalog


def addAlbum(catalog, album):
    # Se adiciona el album a la lista de álbumes
    lt.addLast(catalog['albums'], album)
    return catalog


# Funciones para creacion de datos

def trackSize(catalog):
    return lt.size(catalog['tracks'])


def artistSize(catalog):
    return lt.size(catalog['artists'])


def albumSize(catalog):
    return lt.size(catalog['albums'])


def rankingArtistas(artists, N):
    sublista = lt.subList(artists, 1, N)

    return sublista

def dateFormat(date, date_precision):
    if date_precision == 'day':
        date_format = DT.strptime(
            date, "%Y-%m-%d")
    elif date_precision == 'month':
        year = date[4:6]
        if int(year) < 69:
            date = date.replace(
                year, '19' + year)
            date_format = DT.strptime(
                date, "%b-%Y")
        else:
            date_format = DT.strptime(
                date, "%b-%y")
    else:
        date = int(date)
        date_format = dt.datetime(
            date, 1, 1, 0, 0, 0, 0)

    return date_format

# Funciones de consulta


def getFirst(list):
    t_3i = lt.newList('ARRAY_LIST')
    for pos in range(1, 4):
        elem = lt.getElement(list, pos)
        lt.addLast(t_3i, elem)

    return t_3i


def getLast(list):
    t_3f = lt.newList('ARRAY_LIST')
    size = lt.size(list)
    for pos in range(size - 2, size + 1):
        elem = lt.getElement(list, pos)
        lt.addLast(t_3f, elem)

    return t_3f


def albumsInTimeSpan(anio_i, anio_f, albums):
    DTanio_i = dt.datetime(anio_i, 1, 1, 0, 0, 0, 0)
    DTanio_f = dt.datetime(
        anio_f, 12, 31, 0, 0, 0, 0)

    firstPos = bi.busqueda(
        albums, DTanio_i, floorAlbums)
    lastPos = bi.busqueda(
        albums, DTanio_f, ceilingAlbums)

    numTotal = lt.subList(
        albums,
        firstPos,
        lastPos -
        firstPos +
        1)

    return numTotal


def findMainArtist(artID, artists):
    found = False
    i = 1
    while not found and i <= lt.size(artists):
        artist = lt.getElement(artists, i)
        if artist['id'] == artID:
            name = artist['name']
            found = True
        i += 1

    return name


def findMainTrack(trackID, tracks):
    found = False
    i = 1
    name = None
    while not found and i <= lt.size(tracks):
        track = lt.getElement(tracks, i)
        if track['id'] == trackID:
            name = track['name']
            found = True
        i += 1

    return name

def findBestTrack(artist, market, tracks):
    artistID = artist['id']
    found = False
    best_track = None
    i = 1

    while not found and i <= lt.size(tracks):
        track = lt.getElement(tracks, i)
        track_artists = track['artists_id']
        track_markets = track ['available_markets']
        if artistID in track_artists and market in track_markets:
            best_track = track
            found = True
        i += 1
    
    return best_track

def findnumTracks(artist, tracks):
    artistID = artist['id']
    numTracks = 0
    i = 1

    for track in lt.iterator(tracks):
        if artistID in track['artists_id']:
            numTracks += 1
    
    return numTracks

def findnumAlbums(artist, albums):
    artistID = artist['id']
    numAlbums = 0
    i = 1

    for album in lt.iterator(albums):
        if artistID == album['artist_id']:
            numAlbums += 1
    
    return numAlbums

# Funciones utilizadas para comparar elementos en una
# búsqueda

def searchAlbumTime(alb_list, current_pos):
    bottom = False
    top = False
    if current_pos == lt.size(alb_list):
        top = True
    if current_pos == 1:
        bottom = True

    current_album = lt.getElement(
        alb_list, current_pos)
    current_date = current_album['release_date']
    current_date_precision = current_album['release_date_precision']

    current_date_format = dateFormat(current_date, current_date_precision)

    if not bottom:
        previous_album = lt.getElement(
            alb_list, current_pos - 1)
        previous_date = previous_album['release_date']
        previous_date_precision = previous_album['release_date_precision']
        previous_date_format = dateFormat(previous_date, previous_date_precision)
    else:
        previous_date_format = -1

    if not top:
        next_album = lt.getElement(
            alb_list, current_pos + 1)
        next_date = next_album['release_date']
        next_date_precision = next_album['release_date_precision']
        next_date_format = dateFormat(next_date, next_date_precision)
    else:
        next_date_format = -1

    return previous_date_format, current_date_format, next_date_format


def floorAlbums(alb_list, current_pos, value):
    prev, current, nxt = searchAlbumTime(
        alb_list, current_pos)

    current_true = current >= value
    if prev == -1:
        if current_true:
            return 0
        else:
            return 1

    previous_true = prev >= value

    if current_true:
        if not previous_true:
            return 0
        else:
            return -1
    else:
        return 1


def ceilingAlbums(alb_list, current_pos, value):
    prev, current, nxt = searchAlbumTime(
        alb_list, current_pos)

    current_true = current <= value
    if nxt == -1:
        if current_true:
            return 0
        else:
            return -1

    nxt_true = nxt <= value

    if current_true:
        if not nxt_true:
            return 0
        else:
            return 1
    else:
        return -1

# Funciones utilizadas para comparar elementos en un
# ordenamiento


def compareTracks(track1, track2,):

    # Devuelve verdadero (True) si la 'popularity'
    # del track1 es mayor que la del track2
    # Args:

    # track1: informacion del primer track que
    # incluye su valor 'popularity'
    # track2: informacion del segundo track que
    # incluye su valor 'popularity'

    toRank = ["popularity", "duration_ms", ]

    for x in toRank:
        if track1[x] != track2[x]:
            return int(
                float(track1[x])) > int(
                float(track2[x]))
    # no podemos pasar el nombre a float, por lo
    # que hacemos esto en vez al final
    return track1["name"] > track2["name"]


def compareArtists(artist1, artist2,):

    # Devuelve verdadero (True) si artist1 es más popular
    # (o en su defecto, tiene más followers o su nombre
    # es primero alfabéticamente) que artist2
    # Args:
    # artist1: informacion del primer artista que
    # incluye su valor 'followers'
    # artist2: informacion del segundo artista que
    # incluye su valor 'followers'

    value_p = comparePopularity(artist1, artist2)
    if value_p != 0:
        if value_p == 1:
            return True
        else:
            return False
    value_f = compareFollowers(artist1, artist2)
    if value_f != 0:
        if value_f == 1:
            return True
        else:
            return False
    value_n = compareName(artist1, artist2)
    if value_n != 0:
        if value_n == 1:
            return True
        else:
            return False
    else:
        return False


def comparePopularity(art1, art2):

    # Devuelve 1 si el artista 1 tiene más
    # popularidad, 0 si son iguales y -1 de lo
    # contrario

    comp = int(
        float(art1['artist_popularity'])) > int(
        float(art2['artist_popularity']))
    if comp:
        return 1
    elif int(float(art1['artist_popularity'])) == int(float(art2['artist_popularity'])):
        return 0
    else:
        return -1


def compareFollowers(art1, art2):

    # Devuelve 1 si el artista 1 tiene más
    # seguidores, 0 si son iguales y -1 de lo
    # contrario

    comp = int(
        float(art1['followers'])) > int(
        float(art2['followers']))
    if comp:
        return 1
    elif int(float(art1['followers'])) == int(float(art2['followers'])):
        return 0
    else:
        return -1


def compareName(art1, art2):

    # Devuelve 1 si el artista 1 tiene un nombre
    # primero en el alfabeto, 0 si son iguales y -1
    # de lo contrario

    comp = (
        str(art1['name']).lower()) < (
        str(art2['name']).lower())
    if comp:
        return 1
    elif (art1['name']) == (art2['name']):
        return 0
    else:
        return -1


def compareAlbums(alb1, alb2):
    date1 = alb1['release_date']
    date2 = alb2['release_date']
    date_precision1 = alb1['release_date_precision']
    date_precision2 = alb2['release_date_precision']

    date1Format = dateFormat(date1, date_precision1)
    date2Format = dateFormat(date2, date_precision2)

    return date1Format < date2Format


# Funciones de ordenamiento

def sortTracks(catalog):
    sub_list = catalog["tracks"]
    me.sort(sub_list, compareTracks)


def sortArtists(artists):
    me.sort(artists, compareArtists)


def sortAlbums(albums):
    me.sort(albums, compareAlbums)


def sortArtists(catalog):
    me.sort(catalog, compareArtists)


# def topTracks(control, n):
#     tracks = control["model"]["tracks"]
#     albums = control["model"]["albums"]
#     artists = control["model"]["artists"]
#     topTracks = lt.newList("ARRAY_LIST")

#     for trackPos in range(1, n):
#         addTrack(
#             topTracks,
#             lt.getElement(
#                 tracks,
#                 trackPos))

#     # topTracks ya tiene los top n tracks
#     top = lt.newList("ARRAY_LIST")
#     while lt.size(topTracks) > 6:
#         lt.deleteElement(topTracks, 4)

#     for trackPos in range(lt.size(topTracks)):
#         for albumPos in range(lt.size(albums)):
#             if lt.getElement(
#                     topTracks,
#                     trackPos)["album_id"] == lt.getElement(
#                     albums,
#                     albumPos)["id"]:
#                 album = lt.getElement(
#                     albums, albumPos)["name"]
#         for
#         lt.addLast(
#             top, {
#                 "name": lt.getElement(
#                     topTracks, trackPos)["name"],
#                 "album": album,
#             })
