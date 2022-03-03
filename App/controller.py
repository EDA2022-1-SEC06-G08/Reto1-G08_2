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


def newController(artists_liststr):
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog(
        artists_liststr)
    return control


# Funciones para la carga de datos

def loadData(filesize, control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    tracks = loadTracks(catalog, filesize)
    artists = loadArtists(catalog, filesize)
    albums = loadAlbums(catalog, filesize)

    tracks_3i = getFirstTracks(catalog)
    tracks_3f = getLastTracks(catalog)

    artists_3i = getFirstArtists(catalog)
    artists_3f = getLastArtists(catalog)

    albums_3i = getFirstAlbums(catalog)
    albums_3f = getLastAlbums(catalog)

    # sort(catalog)
    return tracks, artists, albums, tracks_3i, tracks_3f, artists_3i, artists_3f, albums_3i, albums_3f


def loadTracks(catalog, filesize='large'):
    """
    Carga todos los tracks del archivo y los agrega a la lista de tracks
    """
    tracksfile = cf.data_dir + 'Spotify/spotify-tracks-utf8-' + filesize + '.csv'
    input_file = csv.DictReader(
        open(tracksfile, encoding='utf-8'))
    for track in input_file:
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


# Funciones de ordenamiento

def sort(catalog):
    """
    Llama a otras funciones para ordenar el catalog entero
    """
    sortTracks(catalog)
    sortArtists(catalog)
    sortAlbums(catalog)


def sortTracks(catalog):
    """
    Ordena las tracks mediante model.py
    """

    model.sortTracks(catalog)


def sortArtists(catalog):
    """
    Ordena los artistas mediante model.py
    """

    model.sortArtists(catalog)


def sortAlbums(catalog):
    """
    Ordena los álbumes mediante model.py
    """

    model.sortAlbums(catalog)


# Funciones de consulta sobre el catálogo

def getFirstTracks(catalog):
    """
    Obtiene los primeros 3 tracks de la lista de tracks
    """

    tracks = model.getFirstTracks(catalog)

    return tracks


def getLastTracks(catalog):
    """
    Obtiene los últimos 3 tracks de la lista de tracks
    """

    tracks = model.getLastTracks(catalog)

    return tracks


def getFirstArtists(catalog):
    """
    Obtiene los primeros 3 artistas de la lista de artistas
    """

    artists = model.getFirstArtists(catalog)

    return artists


def getLastArtists(catalog):
    """
    Obtiene los últimos 3 artistas de la lista de artistas
    """

    artists = model.getLastArtists(catalog)

    return artists


def getFirstAlbums(catalog):
    """
    Obtiene los primeros 3 álbumes de la lista de álbumes
    """

    albums = model.getFirstAlbums(catalog)

    return albums


def getLastAlbums(catalog):
    """
    Obtiene los últimos 3 álbumes de la lista de álbumes
    """

    albums = model.getLastAlbums(catalog)

    return albums

def sort(sort_type, catalog):
    time = model.sort(sort_type, catalog["model"])
    
    return time
