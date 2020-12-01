# -*- coding: utf-8 -*-
# ·
"""
Device

Definición de la clase Device

-------------------------------------------------------------------------------
    Autor: Simón Martínez <simon@cicoss.net>
    Fecha: sáb nov 28 22:28:14 CET 2020
-------------------------------------------------------------------------------

"""

from mod.partition import Partition


class Device:
    """
    Dispositivo de Bloques

    Mantiene lo datos relativos a un dispositivo de bloques
    existente en el sistema
    """
    def __init__(self, bdevice):
        """
        __init__ Constructor

        Trasfiere los datos en formato dictionary (resultado de lectura json)
        a formato propiedades

        Args:
            bdevice (dictionary): Datos provinientes de la carga json
        """
        self.__name = bdevice['name']
        self.__kname = bdevice['kname']
        self.__path = bdevice['path']
        self.__fsavail = bdevice['fsavail']
        self.__fssize = bdevice['fssize']
        self.__fstype = bdevice['fstype']
        self.__fsused = bdevice['fsused']
        self.__fsuse = bdevice['fsuse%']
        self.__mountpoint = bdevice['mountpoint']
        self.__label = bdevice['label']
        self.__uuid = bdevice['uuid']
        self.__ptuuid = bdevice['ptuuid']
        self.__pttype = bdevice['pttype']
        self.__hotplug = bdevice['hotplug']
        self.__model = bdevice['model']
        self.__size = bdevice['size']
        self.__state = bdevice['state']
        self.__mode = bdevice['mode']
        self.__rota = bdevice['rota']
        self.__type = bdevice['type']
        self.__tran = bdevice['tran']
        self.__subsystems = bdevice['subsystems']
        self.__rev = bdevice['rev']
        self.__vendor = bdevice['vendor']
        self.__partitions = []
        if 'children' in bdevice:
            for child in bdevice['children']:
                self.__partitions.append(Partition(child))

    @property
    def name(self):
        """
        name nombre del device

        Nombre asignado por el sistema
        Ej.: sda
        Suele coincidir con el KNAME

        Returns:
            string: Ejemplo: sda
        """
        return self.__name

    @property
    def kname(self):
        """
        kname nombre del device

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

        path al dispositivo
        Ej.: /dev/sda5

        Returns:
            string: path
        """

        return self.__path

    @property
    def fsavail(self):
        """
        fsavail file system available

        espacio disponible en el sistema de archivos
        solo válido en type loop y rom

        Returns:
            string: tamaño libre (generalmente 0)
            None: si no dispone del dato
        """
        return self.__fsavail

    @property
    def fssize(self):
        """
        fssize file system size

        tamaño del sistema de archivos
        solo válido para type loop y rom

        Returns:
            string: Ej.: '4G'
        """
        return self.__fssize

    @property
    def fstype(self):
        """
        fstype file system type

        tipo del sistema de archivos
        solo válido par type loop y rom

        Returns:
            string: tipo
        """
        return self.__fstype

    @property
    def fsused(self):
        """
        fsused file system usado

        valor absoluto del espacio usado en el filesystem
        solo tiene significado en dispositivos type loop y rom

        Returns:
            string: Ej.: '95G'
        """
        return self.__fsused

    @property
    def fsuse(self):
        """
        fsuse file system use

        tanto por ciento de uso del sistema de archivos
        Solo los dispositivos loop y rom disponen de este dato

        Returns:
            string: Ej.: '37%'
        """
        return self.__fsuse

    @property
    def mountpoint(self):
        """
        mountpoint Punto de Montado

        Directorio en el que está montado el dispositivo
        Solo los de type rom y loop disponen de este dato si están montados

        Returns:
            string: path completo al punto de montaje o None
        """
        return self.__mountpoint

    @property
    def label(self):
        """
        label etiqueta

        Normalmente no disponen de este dato más que los de type 'rom'

        Returns:
            string: label
        """
        return self.__label

    @property
    def uuid(self):
        """
        uuid Identificador único

        Normalmente no disponen de este valor más que los de type 'rom'

        Returns:
            string: UUID o None
        """
        return self.__uuid

    @property
    def ptuuid(self):
        """
        ptuuid PartitionTableUuid

        UUID de la tabla de particiones
        el más inequívoco identificador de un disco

        Returns:
            string: uuid
        """
        return self.__ptuuid

    @property
    def pttype(self):
        """
        pttype PartitionTableType

        Tipo de tabla de particiones

        Returns:
            string: tipo de tabla ('gpt' | 'dos' | ...)
        """
        return self.__pttype

    @property
    def hotplug(self):
        """
        hotplug Conexión en caliente

        informa si es un dispositivo que se pueda conectar
        con el ordenador funcionando

        Returns:
            bool: True conectable, False al contrario
        """
        return self.__hotplug

    @property
    def model(self):
        """
        model Modelo

        Indica el modelo de Disco

        Returns:
            string: model
        """
        return self.__model

    @property
    def size(self):
        """
        size Tamaño

        Capacidad en formato humano k, M, G, T

        Returns:
            string: P. Ej.: "931,5G"
        """
        return self.__size

    @property
    def state(self):
        """
        state Estado

        Estado del disco: "runnyng" o None

        Returns:
            string: state
        """
        return self.__state

    @property
    def mode(self):
        """
        mode Modo

        Permisos del device. P. ej.: "brw-rw----"
        Supongo que se refiere al fichero especial /dev/sdx

        Returns:
            string: mode
        """
        return self.__mode

    @property
    def rota(self):
        """
        rota Gira

        Indica si es un dispositivo de rotación electro-mecánica o virtual
        o estatico (ssd)

        Returns:
            bool: True mecánico, False estático
        """
        return self.__rota

    @property
    def type(self):
        """
        type tipo

        Tipo de dispositivo

        Returns:
            string: "loop" | "disk" | "rom" ...
        """
        return self.__type

    @property
    def tran(self):
        """
        tran Transporte

        Tipo de conexión con el sistema "sata", "usb", ...

        Returns:
            string: tran
        """
        return self.__tran

    @property
    def subsystems(self):
        """
        subsystems Subsistemas

        Se refiere a los subsistemas "block", "scsi", "pci", "usb"
        Suele pertenecer a varios subsistemas simultáneamente

        Returns:
            lista: subsistemas (["block","scsi",...])
        """
        return self.__subsystems.split(':')

    @property
    def rev(self):
        """
        rev revisión

        Revisión del modelo de disco

        Returns:
            string: número exa
        """
        return self.__rev

    @property
    def vendor(self):
        """
        vendor Vendedor

        Vendedor o fabricante del disco

        Returns:
            string: vendor
        """
        return self.__vendor

    @property
    def partitions(self):
        """
        particiones hijas

        Lista de objetos de classe Partition conteniendo
        las particiones del disco

        Returns:
            list:
        """
        return self.__partitions

    def count_partitions(self):
        """
        count_partitions cuenta particiones

        Numero de particiones en el dispositivo

        Returns:
            int: numero de particiones
        """
        return len(self.__partitions)

    def find_parts_with_label(self, label):
        partitions = []
        if self.__partitions is not None:
            for part in self.__partitions:
                if part.label == label:
                    partitions.append(part)
        return partitions

    def find_part_with_uuid(self, uuid):
        """
        find_part_with_uuid

        Busca la partición con UUID 'uuid'

        Args:
            uuid (string): UUID

        Returns:
            Partition: objeto Partition
        """
        if self.__partitions is not None:
            for part in self.__partitions:
                if part.uuid == uuid:
                    return part

        return None

    def find_part_with_mapped_uuid(self, mapuuid):
        """
        find_part_with_mapped_uuid

        encontrar una partición con un fs mapped con uuid

        Args:
            mapuuid (string): UUID del fs mapped

        Returns:
            dictionary: {'part':Partition, 'mapped':Mapper}
            None: si no lo encuentra
        """
        if self.__partitions is not None:
            for part in self.__partitions:
                map = part.find_mapped_with_uuid(mapuuid)
                if map is not None:
                    return {'part': part, 'mapped': map}
        return None
