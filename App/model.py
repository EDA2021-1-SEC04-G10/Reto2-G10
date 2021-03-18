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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista para guardar
    todos los videos y crea una Hash Table para guardar las category id
    Retorna el catálogo inicializado
    """
    catalog = {'videos': None,
                'categoryid': None}

    catalog['videos'] = lt.newList(datastructure='SINGLE_LINKED',
                                    cmpfunction=cmpVideos)
    catalog['category_id'] = mp.newMap(80,
                                    maptype="CHAINING",
                                    loadfactor=4.0,
                                    comparefunction=compareMapCategoryIds)

    return catalog
# Construccion de modelos

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    """
    Adiciona un video a la lista de videos
    """
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category_dict):
    """
    Añade una categoria al catalogo
    """
    category = createCategory(category_dict['name'], category_dict['id'])
    mp.put(catalog['category_id'], category_dict['name'], category)

# Funciones para creacion de datos

def createCategory(categoryId, categoryName):
    """
    Crea una categoria para poder añadirla al mapa
    """
    newCategory = {"categoryname": "",
                    "categoryid": ""}
    newCategory["categoryname"]=categoryName
    newCategory["categoryid"]=categoryId
    return newCategory

# Funciones de consulta
def getCategoryId(catalog, categoryname):
    """
    Obtiene el 'id' de una categoría por su nombre
    """
    for category in lt.iterator(catalog['categoryid']):
        if categoryname in category['name']:
            return category['id']

# Funciones utilizadas para comparar elementos dentro de una lista

def compareMapCategoryIds(key, category):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    entry = me.getKey(category)
    if key == entry:
        return 0
    elif key > entry:
        return 1
    else:
        return -1

def cmpVideos(videotitle, video):
    if (videotitle.lower() in video['title'].lower()):
        return -1
    return 0

# Funciones de ordenamiento
def sortVideosByLikes(catalog):
    """
    Ordena el catálogo de videos por su número de 'likes'
    """
    sortVideosByLikes = ms.sort(catalog, cmpVideosByLikes)
    return sortVideosByLikes
