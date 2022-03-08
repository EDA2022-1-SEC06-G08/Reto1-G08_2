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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los tracks, adicionalmente, crea una lista vacia para los artistas
    y una lista vacia para los álbumes.
    Retorna el catalogo inicializado.
    """
    catalog = {'tracks': None,
               'artists': None,
               'albums': None,
               'time_album': None}

    catalog['tracks'] = lt.newList("ARRAY_LIST")
    # cmpfunction = compareTracks)
    catalog['artists'] = lt.newList('ARRAY_LIST')
    # cmpfunction=compareArtists)
    catalog['albums'] = lt.newList('ARRAY_LIST')
    # cmpfunction=compareAlbums)
    catalog['time_album'] = lt.newList('ARRAY_LIST')

    return catalog


# Funciones para agregar informacion al catalogo

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
    DTanio_f = dt.datetime(anio_f, 1, 1, 0, 0, 0, 0)

    firstPos = bi.busqueda(albums, DTanio_i, searchAlbumTime)
    lastPos = bi.busqueda(albums, DTanio_f, searchAlbumTime)

    numTotal = lt.subList(albums, firstPos, lastPos)

    return numTotal


#Funciones utilizadas para comparar elementos en una búsqueda

def searchAlbumTime(alb_list, current_pos, value):
    current_album = lt.getElement(alb_list, current_pos)
    previous_album = lt.getElement(alb_list, current_pos-1)
    
    current_date = current_album['release date']
    previous_date = previous_album(alb_list, current_pos-1)['release date']

    current_date_precision = current_album['release_date_precision']
    previous_date_precision = previous_album['release_date_precision']

    if current_date_precision == 'day':
        current_date_format = DT.strptime(current_date, "%Y-%m-%d")
    elif current_date_precision == 'month':
        current_date_format = DT.strptime(current_date, "%b-%y")
    else:
        current_date = int(current_date)
        current_date_format = dt.datetime(int(current_date), 1, 1, 0, 0, 0, 0)

    if previous_date_precision == 'day':
        previous_date_format = DT.strptime(previous_date, "%Y-%m-%d")
    elif previous_date_precision == 'month':
        previous_date_format = DT.strptime(previous_date, "%b-%y")
    else:
        previous_date = int(previous_date)
        previous_date_format = dt.datetime(int(previous_date), 1, 1, 0, 0, 0, 0)

    current_true = DT.strftime(current_date_format, "%Y") >= value
    previous_true = DT.strftime(previous_date_format, "%Y") >= value

    if current_true:
        if not previous_true:
            return 0
        else:
            return 1
    else:
        return -1


# Funciones utilizadas para comparar elementos en un
# ordenamiento


def compareTracks(track1, track2,):
    """
        Devuelve verdadero (True) si la 'popularity' del track1 es mayor que la del track2
        Args:
        track1: informacion del primer track que incluye su valor 'popularity'
        track2: informacion del segundo track que incluye su valor 'popularity'
    """

    toRank = ["popularity", "duration_ms", ]

    for x in toRank:
        if track1[x] != track2[x]:
            return int(
                float(track1[x])) > int(
                float(track2[x]))
    # no podemos pasar el nombre a float, por lo
    # que hacemos esto en vez al final
    return track1["name"] > track2["name"]


def compareArtists(artist1, artist2):
    """
    Devuelve verdadero (True) si artist1 es más popular (o en su defecto, tiene más followers o su nombre
    es primero alfabéticamente) que artist2
    Args:
    artist1: informacion del primer artista que incluye su valor 'followers'
    artist2: informacion del segundo artista que incluye su valor 'followers'
    """
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
        if value_f == 1:
            return True
        else:
            return False
    else:
        return False

def comparePopularity(art1, art2):
    """
    Devuelve 1 si el artista 1 tiene más popularidad, 0 si son iguales y -1 de lo contrario
    """
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
    """
    Devuelve 1 si el artista 1 tiene más seguidores, 0 si son iguales y -1 de lo contrario
    """
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
    """
    Devuelve 1 si el artista 1 tiene un nombre primero en el alfabeto, 0 si son iguales y -1 de lo contrario
    """
    comp = (
        str(art1['name']).lower()) < (
        str(art2['name']).lower())
    if comp:
        return 1
    elif (art1['name']) == (art2['name']):
        return 0
    else:
        return -1


def compareAlbumsTime(alb1, alb2):
    date1 = alb1['release_date']
    date2 = alb2['release_date']
    date_precision1 = alb1['release_date_precision']
    date_precision2 = alb2['release_date_precision']

    if date_precision1 == 'day':
        date1Format = DT.strptime(date1, "%Y-%m-%d")
    elif date_precision1 == 'month':
        date1Format = DT.strptime(date1, "%b-%y")
    else:
        date1 = int(date1)
        date1Format = dt.datetime(int(date1), 1, 1, 0, 0, 0, 0)

    if date_precision2 == 'day':
        date2Format = DT.strptime(date2, "%Y-%m-%d")
    elif date_precision2 == 'month':
        date2Format = DT.strptime(date2, "%b-%y")
    else:
        date2 = int(date2)
        date2Format = dt.datetime(int(date2), 1, 1, 0, 0, 0, 0)


    return date1Format < date2Format

# def compareAlbums():


# Funciones de ordenamiento

def sortTracks(catalog):
    sub_list = catalog["tracks"]
    me.sort(sub_list, compareTracks)

# def sortAlbums():

def sortArtists(artists):
    me.sort(artists, compareArtists)

def sortAlbumsTime(albums):
    sublist = lt.subList(albums, 1, lt.size(albums))
    -me.sort(sublist, compareAlbumsTime)
    
    return sublist
