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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import (
    shellsort as sh,
    insertionsort as ins,
    selectionsort as se,
    mergesort as me,
    quicksort as qu
)
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
               'albums': None}

    catalog['tracks'] = lt.newList("ARRAY_LIST")
    # cmpfunction = compareTracks)
    catalog['artists'] = lt.newList('ARRAY_LIST')
    # cmpfunction=compareArtists)
    catalog['albums'] = lt.newList('ARRAY_LIST')
    # cmpfunction=compareAlbums)

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
    ai = getFirst(sublista)
    af = getLast(sublista)

    return ai, af, sublista

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
    # no podemos pasar el nombre a sun float, por lo
    # que hacemos esto en vez al final
    return track1["name"] > track2["name"]


def compareArtists2(art1, art2):
    return int(
        float(art1['artist_popularity'])) > int(
        float(art2['artist_popularity']))


def compareArtists(artist1, artist2,):
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
        return True


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

# def compareAlbums():


# Funciones de ordenamiento

def sortTracks(catalog):
    sub_list = catalog["tracks"]
    me.sort(sub_list, compareTracks)

# def sortAlbums():


def sortArtists(catalog):
    me.sort(catalog['artists'], compareArtists)
