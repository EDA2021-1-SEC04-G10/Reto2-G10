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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la función de inicialización del catalogo al modelo
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadVideos(catalog):
    """
    Carga los videos del archivo
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategoryId(catalog):
    """
    Carga las categorías del archivo
    """
    categoryidfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryidfile, encoding='utf-8'), delimiter='\t')
    for categoryid in input_file:
        model.addCategory(catalog, categoryid)

# Funciones de ordenamiento

def sortVideosByLikes(catalog):
    """
    Ordena los videos por 'likes'
    """
    return model.sortVideosByLikes(catalog)
# Funciones de consulta sobre el catálogo
def getCategoryId(catalog, categoryname):
    """
    Retorna el 'id' de una categoría por su nombre
    """
    return model.getCategoryId(catalog, categoryname)