# -*- coding: utf-8 -*-
# ·
"""
Device

Definición de la clase Partition

-------------------------------------------------------------------------------
    Autor: Simón Martínez <simon@cicoss.net>
    Fecha: sáb nov 28 22:33:09 CET 2020
-------------------------------------------------------------------------------

"""

from mod.mapped import Mapped


class Partition:
    """
    Particiones

    Clase de objetos partición de disco
    """
    def __init__(self, child):
        """
        __init__ Constructor

        Trasfiere los datos en formato dictionary (resultado de lectura json)
        a formato propiedades

        Args:
            child (dictionary): Datos provinientes de la carga json
        """
        self.__name = child['name']
        self.__kname = child['kname']
        self.__path = child['path']
        self.__fsavail = child['fsavail']
        self.__fssize = child['fssize']
        self.__fstype = child['fstype']
        self.__fsused = child['fsused']
        self.__fsuse = child['fsuse%']
        self.__mountpoint = child['mountpoint']
        self.__label = child['label']
        self.__uuid = child['uuid']
        self.__parttype = child['parttype']
        self.__partlabel = child['partlabel']
        self.__partuuid = child['partuuid']
        self.__size = child['size']
        self.__mode = child['mode']
        self.__rota = child['rota']
        self.__type = child['type']
        self.__pkname = child['pkname']
        self.__mapped = []
        if "children" in child:
            for mapp in child['children']:
                self.__mapped.append(Mapped(mapp))

    @property
    def name(self):
        """
        name nombre de la partición

        Nombre asignado por el sistema

        Returns:
            string: Ejemplo: sda1
        """
        return self.__name

    @property
    def kname(self):
        """
        kname nombre de la partición

        Es el nombre usado por el sistema
        No tengo muy clara la diferencia entre name y kname
        en las particiones mapeadas a sistemas crypt el
        name es el que se le da en configuración de device
        y kname es el dm-x. En todos los demás casos vistos
        por mi el name y el kname es el mismo.

        Returns:
            string: kname
        """
        return self.__kname

    @property
    def path(self):
        """
        path path de acceso

        path para usar en el p. ej. el montado
        /dev/sda5

        Returns:
            string: path
        """
        return self.__path

    @property
    def fsavail(self):
        """
        fsavail FileSystem Available

        Espacio disponible en el sistema de archivos

        Returns:
            string: valor formato humano
        """
        return self.__fsavail

    @property
    def fssize(self):
        """
        fssize Tamaño sistema de archivos

        Tamaño total de la partición para alojar archivos

        Returns:
            string: valor en formato humano
        """
        return self.__fssize

    @property
    def fstype(self):
        """
        fstype Tipo de sistema de archivos

        "ext4", "ntfs", ...

        Returns:
            string: fstype
        """
        return self.__fstype

    @property
    def fsused(self):
        """
        fsused Tamaño usado del Sistema de archivos

        Tamaño utilizado por los archivos

        Returns:
            str: fsused en formato humano
        """
        return self.__fsused

    @property
    def fsuse(self):
        """
        fsuse Tamaño usado

        Porcentaje de utilización del sistema de archivos

        Returns:
            string: porcentaje (p. ej.: '57%')
        """
        return self.__fsuse

    @property
    def mountpoint(self):
        """
        mountpoint Punto de montado

        Path absoluto al punto de montado de la partición

        Returns:
            string: path
        """
        return self.__mountpoint

    @property
    def label(self):
        """
        label Etiqueta

        Etiqueta asignada en el formateo de la partición

        Returns:
            string: label
        """
        return self.__label

    @property
    def uuid(self):
        """
        uuid UUID

        ID único de indentificación de la partición
        Se utiliza para montado de la partición

        Returns:
            string: UUID
        """
        return self.__uuid

    @property
    def parttype(self):
        """
        parttype UUID del typo de partición

        Identificador único del tipo de partición

        Returns:
            string: partype
        """
        return self.__parttype

    @property
    def partlabel(self):
        """
        partlabel Etiqueta de partición

        Desconozco para que sirve ni que identifica

        Returns:
            string: partlabel
        """
        return self.__partlabel

    @property
    def partuuid(self):
        """
        partuuid UUID de partición

        Desconoaco su uso. No usar para el montado

        Returns:
            string: partuuid
        """
        return self.__partuuid

    @property
    def size(self):
        """
        size tamaño

        Espacio de disco utilizado por la partición

        Returns:
            string: tamaño en formato humano
        """
        return self.__size

    @property
    def mode(self):
        """
        mode modo de acceso

        Returns:
            string: mode
        """
        return self.__mode

    @property
    def rota(self):
        """
        rota Giro

        Igual que en el disco padre

        Returns:
            bool: igual que en el disco
        """
        return self.__rota

    @property
    def type(self):
        """
        type typo de objeto

        Disco, partición, etc

        Returns:
            string: type
        """
        return self.__type

    @property
    def pkname(self):
        """
        pkname parent kname

        Kname del contenedor padre

        Returns:
            string: kname
        """
        return self.__pkname

    @property
    def mapped(self):
        """
        mapeados hijos

        colección de objetos mapper
        contenidos en la partición

        Returns:
            list: mappers
        """
        return self.__mapped

    def count_mapped(self):
        """
        count_mapped

        Número de fs mapeados

        Returns:
            int: cuenta
        """
        if self.__mapped is None:
            return 0
        return len(self.__mapped)

    def find_mapped_with_uuid(self, mapuuid):
        """
        find_mapped_with_uuid

        busca un fs mapeado don uuid mapuuid

        Args:
            mapuuid (string): UUID

        Returns:
            Mapped: objeto buscado
        """
        if self.count_mapped() > 0:
            for map in self.__mapped:
                if map.uuid == mapuuid:
                    return map
        return None
