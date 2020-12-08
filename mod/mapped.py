# -*- coding: utf-8 -*-
# ·
"""
Mapped

Definición de la clase Mapped

-------------------------------------------------------------------------------
    Autor: Simón Martínez <simon@cicoss.net>
    Fecha: sáb nov 28 22:37:13 CET 2020
-------------------------------------------------------------------------------

"""


class Mapped:
    """
    Clase objetos mapeados en una partición

    Objetos contenidos por una partición
    como volúmenes, o particiones cifradas

    Las descripciones de las propiedades son equivalentes
    a las de las particiones
    """
    def __init__(self, mapp):
        """
        __init__ Constructor

        Trasfiere datos del dictionary mapp
        a propiedades

        Args:
            mapp (dictionary): mapper
        """

        self.__name = mapp['name']
        self.__kname = mapp['kname']
        self.__path = mapp['path']
        self.__fsavail = mapp['fsavail']
        self.__fssize = mapp['fssize']
        self.__fstype = mapp['fstype']
        self.__fsused = mapp['fsused']
        self.__fsuse = mapp['fsuse%']
        self.__mountpoint = mapp['mountpoint']
        self.__label = mapp['label']
        self.__uuid = mapp['uuid']
        self.__size = mapp['size']
        self.__mode = mapp['mode']
        self.__rota = mapp['rota']
        self.__type = mapp['type']
        self.__pkname = mapp['pkname']

    @property
    def name(self):
        return self.__name

    @property
    def kname(self):
        return self.__kname

    @property
    def path(self):
        return self.__path

    @property
    def fsavail(self):
        return self.__fsavail

    @property
    def fssize(self):
        return self.__fssize

    @property
    def fstype(self):
        return self.__fstype

    @property
    def fsused(self):
        return self.__fsused

    @property
    def fsuse(self):
        return self.__fsuse

    @property
    def mountpoint(self):
        return self.__mountpoint

    @property
    def label(self):
        return self.__label

    @property
    def uuid(self):
        return self.__uuid

    @property
    def size(self):
        return self.__size

    @property
    def mode(self):
        return self.__mode

    @property
    def rota(self):
        return self.__rota

    @property
    def type(self):
        return self.__type

    @property
    def pkname(self):
        return self.__pkname

    @property
    def sons(self):
        return None
