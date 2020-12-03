# -*- coding: utf-8 -*-
# ·
"""
===============================================================================
                               blkdevices.py
===============================================================================

Clases y colecciones representando los dispositivos de bloques
para su uso en smbackup.

Uso exclusivo en Linux.
Requiere permisos root.

-------------------------------------------------------------------------------
    Autor: Simón Martínez <simon@cicoss.net>
    Fecha: lun nov 23 22:35:24 CET 2020
-------------------------------------------------------------------------------
"""

import os
import shutil
import tempfile
import json
import re
import time

from mod.device import Device


def dehumanize(str_human):
    """
    dehumanize deshumaniza

    Convierte Números con formato humanizado en enteros

    Args:
        str_human (str): cadena con formato humanizado
                         K,KIB,M,MiB,G,GiB,T,TiB potencias de 2
                         KB,MB,GB,TB potencias de 10

    Returns:
        int: valor entero
    """
    # TODO: añadir formatos de multiplos internacionales
    #       KB, MB, GB, TB potencias de 10

    # patron = "^[0-9]+?(\.[0-9]{3})? ?(KiB|K|k)$"
    patron = " ?(KiB|K|MiB|M|GiB|G|TiB|T){1}$"
    prog = re.compile(patron)
    str_human = str_human.replace(',', '.')
    match = prog.search(str_human)
    if match is not None:
        pos = match.regs[0][0]
        numero = str_human[0:pos].strip()
        pot = str_human[pos:].strip()
    else:
        try:
            return round(float(str_human))
        except ValueError:
            return None

    if pot[0] == 'K':
        mult = 2**10
    elif pot[0] == 'M':
        mult = 2**20
    elif pot[0] == 'G':
        mult = 2**30
    else:
        mult = 2**40

    try:
        return round(float(numero) * mult)

    except ValueError:
        return None


class BlockDevices:
    """
    Dispositivos de bloques

    Mantiene y da acceso a una lista de dipositivos de bloques
    existentes en el sistema en un momento dado
    """
    def __init__(self):
        """
        __init__ Constructor

        Genera directorio y archivo temporal
        para el volcado del comando lsblk
        """

        self.__TempDir = tempfile.mkdtemp(prefix="smb_")

        self.__FileBlockDevices = open(os.path.join(self.__TempDir,
                                                    "BlkDev.json"),
                                       mode='wt')
        self.__FileBlockDevices.write('\n')
        self.__FileBlockDevices.close()

        self.__time = time.time()
        self.__read_fs()

    def __del__(self):
        """
        __del__ Destructor

        Elimina el directorio temporal y su contenido
        """
        shutil.rmtree(self.__TempDir)
        del self.__TempDir

    def __read_fs(self, force=False):
        """
        __read_fs Lee el sistema de ficheros

        Realiza un bolcado sobre fichero temporal del
        resultado del comando Linux lsblk en formato json

        Returns:
            bool: True si no hay errores, False en caso contrario
        """

        # si no se le fuerza actualiza despues de 30 seg
        if not force and ((time.time() - self.__time) > 30):
            return True

        # sintaxis de comando
        cmd_shell = "sudo lsblk -aOJ >{0}".format(self.__FileBlockDevices.name)

        # ejecuto
        result = os.system(cmd_shell)
        if result != 0:
            # ocurrió un error
            return False

        # leo y parseo el contenido del fichero
        with open(self.__FileBlockDevices.name, 'r') as file_json:
            data = json.load(file_json)

        # almaceno el resultado
        self.__myDevices = []
        self.__myDisks = []
        for BDevice in data['blockdevices']:
            device = Device(BDevice)
            self.__myDevices.append(device)
            if device.type == 'disk':
                self.__myDisks.append(device)

        return True

    @property
    def ListDevices(self):
        """
        ListDevices Lista Dispositivos

        Lista completa de los dispositivos detectados
        junto con sus caracteristicas

        Returns:
            list: [objeto Clase Device, ...]
        """
        if not self.__read_fs():
            return None

        return self.__myDevices

    @property
    def ListDisks(self):
        """
        ListDisks

        Lista completa de los dispositivos tipo 'disk'

        Returns:
            list: lista de objetos Device
            None: si falla
        """
        if not self.__read_fs():
            return None

        return self.__myDisks

    def update(self):
        return self.__read_fs(True)

    def get_dev(self, uuid):
        """
        get_dev obtinete el dispositivo

        devuelve el path completo al dispositivo
        util para montado y desmontado

        Args:
            uuid (str): UUID

        Returns:
            str: path (/dev/sdxn)
        """
        dev = self.full_search_uuid(uuid)
        if dev is None:
            return None
        return dev.path

    def find_cdroms(self):
        """
        find_cdroms

        busca las unidades CDROM

        Returns:
            list: lista de objetos Device
        """
        if not self.__read_fs():
            return None

        cdroms = []
        for dev in self.__myDevices:
            if dev.type == "rom":
                cdroms.append(dev)

        return cdroms

    def find_usb_disks(self):
        """
        find_usb_disks

        busca los discos USB

        Returns:
            list: lista de objetos Device
            None: si falla
        """
        if not self.__read_fs():
            return None

        usbdisks = []
        for dev in self.__myDisks:
            if dev.tran == 'usb':
                usbdisks.append(dev)

        return usbdisks

    def find_ssd_disks(self):
        """
        find_ssd_disks

        busca los discos ssd

        Returns:
            list: lista de objetos Device
            None: si falla
        """
        if not self.__read_fs():
            return None

        staticdisks = []
        for dev in self.__myDisks:
            if not dev.rota:
                staticdisks.append(dev)

        return staticdisks

    def find_disk_ptuuid(self, ptuuid):
        """
        find_disk_ptuuid

        busca el disco con la tabla de particiones 'uuid'

        Args:
            ptuuid (string): uuid

        Returns:
            Device: dispositivo buscado o None
        """
        if self.__read_fs():
            for dev in self.__myDisks:
                if ptuuid == dev.ptuuid:
                    return dev

        return None

    def find_disks_with_part_label(self, label):
        """
        find_disks_with_part_label

        busca los discos que contengan una partición con etiqueta 'label'

        Args:
            label (string): etiqueta

        Returns:
            list: lista de diccionarios {'device': disco,
                                         'parts':lista de particiones}
        """
        if not self.__read_fs():
            return None

        devok = []
        for dev in self.__myDisks:
            parts_with_label = dev.find_parts_with_label(label)
            if len(parts_with_label) >= 1:
                devok.append({'device': dev, 'parts': parts_with_label})

        return devok

    def find_disk_with_part_uuid(self, uuid):
        """
        find_disk_with_part_uuid

        busca el disco que contiene una partición con uuid

        Args:
            uuid (string): UUID

        Returns:
            Device: el disco buscado o None
        """
        if not self.__read_fs():
            return None

        for dev in self.__myDisks:
            part_with_uuid = dev.find_part_with_uuid(uuid)
            if part_with_uuid is not None:
                return {'device': dev, 'part': part_with_uuid}

    def find_disks_model(self, model):
        """
        find_disks_model

        Econtrar discos de un determinado modelo

        Args:
            model (string): modelo

        Returns:
            list: lista de objetos device o None si no encuentra
        """
        if not self.__read_fs():
            return None

        disks = []
        for dev in self.__myDisks:
            if dev.model:
                if model in dev.model:
                    disks.append(dev)

        return disks

    def find_disks_gt_size(self, minsize):
        """
        find_disks_gt_size

        busca los dispositivos de tamaño mayor que 'minsize'

        Args:
            minsize (string|integer): tamaño en formato humado o entero

        Returns:
            list: lista de objetos Device
        """
        if not self.__read_fs():
            return None

        minsize = dehumanize(minsize)

        disks = []
        if minsize is None:
            return disks

        for dev in self.__myDisks:
            if dev.size is not None:
                if round(dehumanize(dev.size)) >= minsize:
                    disks.append(dev)
            else:
                # para depuración (punto de interrupción)
                pass

        return disks

    def find_disk_kname(self, kname):
        """
        find_disk_kname encontrar disco con kname

        Busca un disco cuyo kname sea 'kname'

        Args:
            kname (string): kname

        Returns:
            Object class Device: el objeto buscado
        """
        if self.__read_fs():
            for dev in self.__myDisks:
                if dev.kname == kname:
                    return dev
        return None

    def find_disk_with_map_uuid(self, mapuuid):
        """
        find_disk_with_map_uuid

        busca un disco con una partición que tenga un fs mapeado con uuid

        Args:
            mapuuid (string): UUID

        Returns:
            dictionary: {'device':Object Device,
                        'part': Object Partition,
                        'mapped': Object Mapper}
            None: Si no lo encuentra
        """
        if self.__read_fs():
            for dev in self.__myDisks:
                map = dev.find_part_with_mapped_uuid(mapuuid)
                if map is not None:
                    return {
                        'device': dev,
                        'part': map['part'],
                        'mapped': map['mapped']
                    }

        return None

    def full_search_uuid(self, uuid):
        """
        full_search_uuid busca UUID

        Busca un uuid en todo el arbol de dispositivos
        ya sea disco, partición o mapped

        Args:
            uuid (str): UUID a buscar

        Returns:
            dictionary: objeto de clase device, Partition y Mapper
            None: si no lo encuentra
        """

        # campos que pueden contener un uuid:
        # uuid, ptuuid, partuuid
        campos_uuid = ('uuid', 'ptuuid', 'partuuid')
        for dev in self.__myDevices:
            for campo in campos_uuid:
                if getattr(dev, campo, None) == uuid:
                    return {'en': "device", 'campo': campo, 'device': dev}
            for part in dev.partitions:
                for campo in campos_uuid:
                    if getattr(part, campo, None) == uuid:
                        return {
                            'en': "partition",
                            'campo': campo,
                            'device': dev,
                            'partition': part
                        }
                for mapp in part.mapped:
                    for campo in campos_uuid:
                        if getattr(mapp, campo, None) == uuid:
                            return {
                                'en': "mapped",
                                'campo': campo,
                                'device': dev,
                                'partition': part,
                                'mapped': mapp
                            }

        return None

    def is_connected(self, uuid):
        """
        is_conected Si esta conectada

        Comprueba si el dispositivo está conectado
        Util en caso de unidades USB
        Si es accesible está conectado

        Args:
            uuid (str): UUID

        Returns:
            bool: True si está conectado
        """
        disp = self.full_search_uuid(uuid)
        if disp is None:
            return False
        return True

    def is_mounted(self, uuid):
        """
        is_mounted ¿está montado?

        Comprueba si el device correspondiente al UUID pasado
        está montado

        Args:
            uuid (str): UUID

        Return:
            bool: True si está montado, False en caso contrario
        """
        disp = self.full_search_uuid(uuid)
        if disp is None:
            return False

        attr = disp['en']
        if disp[attr].mountpoint is None:
            return False
        return True

    def has_mounted(self, uuid):
        dev = self.full_search_uuid(uuid)
        if dev is None:
            return None
        mounted = []
        dev = dev[dev['en']]
        if dev.mountpoint is not None:
            mounted.append(dev)
        if dev.type in ('disk', 'part'):
            for son in dev.sons:
                if son.mountpoint is not None:
                    mounted.append(son)

    def mounted_in(self, mountpoint):
        """
        mounted_in Dispositivo montado en mountpoint

        Args:
            mountpoint (str): path

        Returns:
            objeto: Device, Partition o Mapped
            None: si falla
        """
        for dev in self.__myDevices:
            if dev.mountpoint == mountpoint:
                return dev
            for part in dev.partitions:
                if part.mountpoint == mountpoint:
                    return part
                for map in part.mapped:
                    if map.mountpoint == mountpoint:
                        return map
        return None

    def mountpoint(self, uuid):
        """
        mountpoint Punto de montado

        Devuelve el path completo al punto de montado
        del dispositivo uuid

        Args:
            uuid (str): UUID

        Returns:
            str: path
            None: si no está montado o no existe la unidad
        """
        disp = self.full_search_uuid(uuid)
        if disp is None:
            return None

        return disp.mountpoint

    def mount(self, uuid, path):
        dev = self.full_search_uuid(uuid)
        if dev is None:
            return False
        dev = dev[dev['en']]
        if dev.fstype in (None, 'crypto_LUKS', 'swap', 'squashfs'):
            return False
        if self.is_mounted(uuid):
            return False

        _path = os.path.abspath(os.path.expanduser(path))
        if not os.path.isdir(_path):
            return False

        cmd = f"sudo mount -o exec {dev.path} {_path}"
        result = os.system(cmd)
        if result > 0:
            return False
        return True

    def umount(self, uuid):
        dev = self.full_search_uuid(uuid)
        if dev is None:
            return False
        dev = dev[dev['en']]
        if not self.is_mounted(uuid):
            return True
        cmd = f"sudo umount {dev.path} &>/dev/null"
        result = os.system(cmd)
        if result > 0:
            return False
        return True

    def eject(self, uuid):
        dev = self.full_search_uuid(uuid)
        if dev is None:
            return False
        dev = dev[dev['en']]
        if self.is_mounted(uuid):
            if not self.umount(uuid):
                return False
        if dev.type == 'disk':
            cmd = f"udisksctl power-off -b {dev.path}"
