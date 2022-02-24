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
from DISClib.Algorithms.Sorting import shellsort as sh, insertionsort as ins, selectionsort as se
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


def newCatalog(artists_liststr):
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los tracks, adicionalmente, crea una lista vacia para los artistas
    y una lista vacia para los álbumes.
    Retorna el catalogo inicializado.
    """
    catalog = {'tracks': None,
               'artists': None,
               'albums': None}

    catalog['tracks'] = lt.newList()
    # cmpfunction = compareTracks)
    catalog['artists'] = lt.newList(
        artists_liststr, cmpfunction=compareArtists)
    # cmpfunction=compareArtists)
    catalog['albums'] = lt.newList()
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


# Funciones de consulta

def getFirstTracks(catalog):
    t_3i = lt.newList('ARRAY_LIST')
    for pos in range(1, 4):
        track = lt.getElement(catalog['tracks'], pos)
        lt.addLast(t_3i, track)

    return t_3i


def getLastTracks(catalog):
    t_3f = lt.newList('ARRAY_LIST')
    size = lt.size(catalog['tracks'])
    for pos in range(size - 2, size + 1):
        track = lt.getElement(catalog['tracks'], pos)
        lt.addLast(t_3f, track)

    return t_3f


def getFirstArtists(catalog):
    Ar_3i = lt.newList('ARRAY_LIST')
    for pos in range(1, 4):
        artist = lt.getElement(
            catalog['artists'], pos)
        lt.addLast(Ar_3i, artist)

    return Ar_3i


def getLastArtists(catalog):
    Ar_3f = lt.newList('ARRAY_LIST')
    size = lt.size(catalog['artists'])
    for pos in range(size - 2, size + 1):
        artist = lt.getElement(
            catalog['artists'], pos)
        lt.addLast(Ar_3f, artist)

    return Ar_3f


def getFirstAlbums(catalog):
    Al_3i = lt.newList('ARRAY_LIST')
    for pos in range(1, 4):
        album = lt.getElement(catalog['albums'], pos)
        lt.addLast(Al_3i, album)

    return Al_3i


def getLastAlbums(catalog):
    Al_3f = lt.newList('ARRAY_LIST')
    size = lt.size(catalog['albums'])
    for pos in range(size - 2, size + 1):
        album = lt.getElement(catalog['albums'], pos)
        lt.addLast(Al_3f, album)

    return Al_3f


# Funciones utilizadas para comparar elementos dentro
# de una lista

# def compareTracks():


def compareArtists(artist1, artist2):
    """
    Devuelve verdadero (True) si los 'followers' de artist1 son menores que los del artist2
    Args:
    artist1: informacion del primer artista que incluye su valor 'followers'
    artist2: informacion del segundo artista que incluye su valor 'followers'
    """
    followers1 = int(float(artist1['followers']))
    followers2 = int(float(artist2['followers']))

    return followers1 < followers2


# def compareAlbums():


# Funciones de ordenamiento

# def sortTracks():


# def sortArtists():


# def sortAlbums():

def selection_sort(catalog):
    sub_list = catalog['artists']
    start_time = getTime()
    se.sort(sub_list, compareArtists)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)

    return delta_time


def insertion_sort(catalog):
    sub_list = catalog['artists']
    start_time = getTime()
    ins.sort(sub_list, compareArtists)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)

    return delta_time


def shell_sort(catalog):
    sub_list = catalog['artists']
    start_time = getTime()
    sh.sort(sub_list, compareArtists)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)

    return delta_time


# Funciones para medir tiempos de ejecucion

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
