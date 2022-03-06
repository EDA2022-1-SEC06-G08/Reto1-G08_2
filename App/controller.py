﻿"""
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
 """

from App.model import trackSize
import config as cf
import model
import sys
import csv

maxInt = sys.maxsize

while True:

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def newController(
        artists_liststr,
        tracks_liststr,
        album_liststr):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos

def loadData(control, filesize='large'):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    datos = {
        "num_tracks": loadTracks(
            catalog,
            filesize),
        "num_artists": loadArtists(
            catalog,
            filesize),
        "num_albums": loadAlbums(
            catalog,
            filesize),
        "tracks_3i": getFirst(catalog),
        "tracks_3f": getLast(catalog),
        "artists_3i": getFirst(catalog),
        "artists_3f": getLast(catalog),
        "albums_3i": getFirst(catalog),
        "albums_3f": getLast(catalog)}
    return datos


def loadTracks(catalog, filesize):
    """
    Carga todos los tracks del archivo y los agrega a la lista de tracks
    """
    tracksfile = cf.data_dir + 'Spotify/spotify-tracks-utf8-' + filesize + '.csv'
    input_file = csv.DictReader(
        open(tracksfile, encoding='utf-8'))
    for track in input_file:
        if track["id"] != "-1":
            model.addTrack(catalog, track)
    return model.trackSize(catalog)


def loadArtists(catalog, filesize='large'):
    """
    Carga todos los artistas del archivo y los agrega a la lista de artistas
    """
    artistfile = cf.data_dir + 'Spotify/spotify-artists-utf8-' + filesize + '.csv'
    input_file = csv.DictReader(
        open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    sortArtists(catalog)
    return model.artistSize(catalog)


def loadAlbums(catalog, filesize='large'):
    """
    Carga todos los álbumes del archivo y los agrega a la lista de álbumes
    """
    albumsfile = cf.data_dir + 'Spotify/spotify-albums-utf8-' + filesize + '.csv'
    input_file = csv.DictReader(
        open(albumsfile, encoding='utf-8'))
    for album in input_file:
        model.addAlbum(catalog, album)
    return model.albumSize(catalog)


# Funciones de requerimientos

def rankingArtistas(control, N):
    catalog = control['model']
    ai, af, lista = model.rankingArtistas(
        catalog
        ['artists'],
        N)

    return ai, af, lista


# Funciones de ordenamiento


def sortTracks(catalog):
    """
    Ordena las tracks mediante model.py
    """

    model.sortTracks(catalog["model"])


def sortArtists(catalog):
    model.sortArtists(catalog)


# Funciones de consulta sobre el catálogo

def getFirst(list):
    list = model.getFirst(list)

    return list


def getLast(list):
    list = model.getLast(list)

    return list
