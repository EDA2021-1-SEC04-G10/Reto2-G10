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
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos
"""

# Construcción de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista para guardar
    los videos. Se crean indices (maps) por los siguientes
    criterios:
    category
    category ids
    """
    catalog = {'videos': None,
               'category': None, 
               'categoryids': None}
    
    """
    Esta lista contiene los videos del archivo. Los videos son
    referenciados por los indices creados a continuación
    """
    catalog['videos'] = lt.newList('SINGLE_LINKED', compareVideosids)

    """
    Se crean indices (maps) por diferentes criterios para llegar
    a la información consultada
    """

    """
    Este indice crea un map cuya llave es el category name del video
    """
    catalog['category'] = mp.newMap(50, 
                                      maptype='PROBING', 
                                      loadfactor=0.30,
                                      comparefunction=compareCategory)
    
    """
    Este indice crea un map cuya llave es el category id del video
    """
    catalog['categoryids'] = mp.newMap(50,
                                        maptype='PROBING',
                                        loadfactor=0.30,
                                        comparefunction=compareCategoryids)
    
    return catalog

# Funciones para agregar información al catálogo

def addVideo(catalog, video):
    """
    Adiciona un video a la lista de videos, adicionalmente, crea una entrada en el map de category ids para indicar
    que el video pertenece a una category id específica
    """
    lt.addLast(catalog['videos'], video)
    addCategoryids(catalog, video)

def addCategory(catalog, category):
    """
    Adiciona las categorías al map de category, donde la llave es
    el name y el valor es el id de la categoría
    """
    mp.put(catalog['category'], category['name'], category['id'])

def addCategoryids(catalog, video):
    """
    Adiciona un video a la lista de videos de una categoría específica,
    las categorías se guardan en un map, donde la llave es el id de la
    categoría y el valor es la lista de videos de esa categoría
    """
    try:
        categoryids = catalog['categoryids']
        videoCategoryid = video['category_id']
        existcategoryid = mp.contains(categoryids, videoCategoryid)
        if existcategoryid:
            entry = mp.get(categoryids, videoCategoryid)
            categoryid = me.getValue(entry)
        else:
            categoryid = newVideoCategory(videoCategoryid)
            mp.put(categoryids, videoCategoryid, categoryid)
        lt.addLast(categoryid['videos'], video)
        categoryid['total_videos'] = lt.size(categoryid['videos'])
    except Exception:
        return None

# Funciones para creación de datos

def newVideoCategory(id):
    """
    Esta función crea la estructura de videos asociados a
    una categoría específica
    """
    category = {'id': '', 
                'total_videos': 0,
                'videos': None}
    
    category['id'] = id
    category['videos'] = lt.newList()
    return category

# Funciones de consulta

def videosSize(catalog):
    """
    Número de videos cargados en el catálogo
    """
    return lt.size(catalog['videos'])

def categorySize(catalog):
    """
    Número de categorías cargadas en el catálogo
    """
    return mp.size(catalog['category'])

def getCategoryid(catalog, name):
    """
    Retorna el id de una categoría
    """
    categoryname = " " + name
    entry = mp.get(catalog['category'], categoryname)
    if entry:
        categoryid = me.getValue(entry)
        return categoryid
    else:
        return None

def getVideosByCategory(catalog, category):
    """
    Retorna los videos de una categoría específica
    """
    category = mp.get(catalog['categoryids'], category)
    if category:
        return me.getValue(category)['videos']

# Funciones utilizadas para comparar elementos

def compareVideosids(id1, id2):
    """
    Compara los ids de dos videos
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareCategory(name, category):
    """
    Compara los category name de dos videos, name es el 
    nombre de la categoría y category una pareja llave-valor
    """
    categoryentry = me.getKey(category)
    if (name == categoryentry):
        return 0
    elif (name > categoryentry):
        return 1
    else:
        return -1

def compareCategoryids(id, category):
    """
    Compara los category ids de dos videos, id es un identificador
    de la categoría y category una pareja llave-valor
    """
    categoryentry = me.getKey(category)
    if (int(id) == int(categoryentry)):
        return 0
    elif (int(id) > int(categoryentry)):
        return 1
    else:
        return -1

def compareVideosByLikes(video1, video2):
    """
    Compara dos videos por su número de likes
    """
    return (float(video1['likes']) > float(video2['likes']))

# Funciones de ordenamiento

def sortVideosByLikes(catalog):
    """
    Ordena el catálogo de videos por su número de likes
    """
    sortVideosByLikes = ms.sort(catalog, compareVideosByLikes)
    return sortVideosByLikes