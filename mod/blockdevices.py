# -*- coding: utf-8 -*-
# ·

import os
import shutil
import tempfile
import json
import time

from mod.device import Device
from mod.disk import Disk
from utiles.strutil import dehumanize


class BlockDevices:
    def __init__(self):

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
        # si no se le fuerza actualiza despues de 30 seg
        if not force and ((time.time() - self.__time) > 30):
            return True

        # sintaxis de comando
        cmd_shell = "sudo lsblk -aOJ >{0}".format(self.__FileBlockDevices.name)

        # ejecuto
        result = os.system(cmd_shell)
        if result != 0:
            # ocurrió un error
            raise OSError(f"Error al ejecutar '{cmd_shell}'")

        # leo y parseo el contenido del fichero
        with open(self.__FileBlockDevices.name, 'r') as file_json:
            data = json.load(file_json)

        # almaceno el resultado
        self.__myDevices = []
        self.__myDisks = []
        for BDevice in data['blockdevices']:
            if BDevice['type'] == 'disk':
                self.__myDisks.append(Disk(BDevice))
            else:
                self.__myDevices.append(Device(BDevice))

        self.__time = time.time()

        return True

    @property
    def Devices(self):
        if not self.__read_fs():
            return None

        return self.__myDevices

    @property
    def Disks(self):
        if not self.__read_fs():
            return None

        return self.__myDisks

    @property
    def CDROM(self):
        if not self.update():
            return None

        cdroms = []
        for dev in self.__myDevices:
            if dev.type == "rom":
                cdroms.append(dev)

        return cdroms

    @property
    def DisksUSB(self):
        if not self.update():
            return None

        _usbdisks = []
        for _disc in self.__myDisks:
            if _disc.tran == 'usb':
                _usbdisks.append(_disc)

        return _usbdisks

    @property
    def SSDDisks(self):
        if not self.update():
            return None

        _staticdisks = []
        for _disc in self.__myDisks:
            if not _disc.rota:
                _staticdisks.append(_disc)

        return _staticdisks

    def update(self):
        return self.__read_fs(True)
        if not self.update():
            return None

        usbdisks = []
        for dev in self.__myDisks:
            if dev.tran == 'usb':
                usbdisks.append(dev)

        return usbdisks

    def get_disk_wwn(self, wwn):
        if self.update():
            for _disc in self.__myDisks:
                if wwn == _disc.wwn:
                    return _disc

        return None

    def find_disks_model(self, model):
        if not self.__read_fs():
            return None

        _disks = []
        for _disk in self.__myDisks:
            if _disk.model is not None:
                if model in _disk.model:
                    _disks.append(_disk)

        return _disks

    def find_disks_gt_size(self, minsize):
        if not self.__read_fs():
            return None

        minsize = dehumanize(minsize)

        _disks = []
        if minsize is None:
            return self.__myDisks

        for _disk in self.__myDisks:
            if _disk.size is not None:
                if round(dehumanize(_disk.size)) >= minsize:
                    _disks.append(_disk)
            else:
                # para depuración (punto de interrupción)
                pass

        return _disks

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
            for _disk in self.__myDisks:
                if _disk.kname == kname:
                    return _disk
        return None

    def find_disks_with_part_label(self, label):
        if not self.__read_fs():
            return None

        _discs = []
        for _disc in self.__myDisks:
            for _part in _disc.partitions:
                if _part.label == label:
                    _discs.append({'disk': _disc, 'partition': _part})

        return _discs

    def find_disk_with_part_uuid(self, uuid):
        if not self.__read_fs():
            return None

        _discs = []
        for _disc in self.__myDisks:
            for _part in _disc.partitions:
                if _part.uuid == uuid:
                    _discs.append({'disk': _disc, 'partition': _part})

        return _discs

    def is_USB_connected(self, wwn):
        """
        is_conected Si esta conectado

        Comprueba si el dispositivo está conectado
        Util en caso de unidades USB
        Si es accesible está conectado

        Args:
            uuid (str): UUID

        Returns:
            bool: True si está conectado
        """
        for _discusb in self.DisksUSB:
            if _discusb.wwn == wwn:
                return True
        return False

    def has_mounted(self, wwn):

        # resuelve el dispositivo
        _disk = self.get_disk_wwn(wwn)
        if _disk is None:
            return None

        mounted = []
        for _part in _disk:
            if _part.mountpoint is not None:
                mounted.append(_part)
            elif _part.volume is not None:
                if _part.volume.mountpoint is not None:
                    mounted.append(_part.volume)

        if len(mounted) == 0:
            return None

        return mounted

    def has_open(self, wwn):
        _disk = self.get_disk_wwn(wwn)
        if _disk is not None:
            raise ValueError(f"No encuentro disco {wwn}")
        for _part in _disk.partitions:
            if _part.volume is not None:
                return True
        return False

    def eject(self, wwn):
        _disk = self.get_disk_wwn(wwn)
        if _disk is None:
            raise ValueError(f"No encuentro el disco {wwn}")
        if _disk.hotplug:
            for _part in _disk.partitions:
                if _part.mountpoint is not None:
                    _part.umount()
                elif _part.volume is not None:
                    if _part.volume.mountpoint is not None:
                        _part.volume.umount()
                    _part.close_volume()

            _cmd = f"sudo udisksctl power-off -b {_disk.path}"
            result = os.system(_cmd)
            if result != 0:
                # ocurrió un error
                raise OSError(f"No se pudo expulsar '{wwn}'")

        self.update()
