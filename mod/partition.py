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

from mod.partitiontype import PartitionType
from mod.device import Device
from mod.volume import Volume
from mod.readdevice import find_children, is_volume_open
from mod.readdevice import open_volume, close_volume
from utiles.strutil import h2
from utiles.color import Color


class Partition(Device):
    def __init__(self, data):
        super().__init__(data)

        self.properties = self.part_properties

        self.__find_volume()

    def __str__(self):
        color = Color()
        if self.label is None:
            _str = h2(f"Partición {self.path}", 70)
        else:
            _str = h2(f"Partición {self.path} [{self.label}]", 70)
        _str += f"{color.MARRON}name: {color.VERDE}"
        _str += f"{self.name.rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}kname: {color.VERDE}"
        _str += f"{self.kname.rjust(63,'.')}{color.END}\n"

        _str += f"{color.MARRON}path: {color.VERDE}"
        _str += f"{self.path.rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}parttype: {color.VERDE}"
        _str += f"{self.parttype.rjust(60,'.')}{color.END}\n"

        _parttype = PartitionType().find_type(self.parttype)
        if _parttype is not None:
            _parttypename = _parttype['name']
            _str += f"{color.VERDE}{_parttypename.rjust(70)}{color.END}\n"

        if self.label is not None:
            _str += f"{color.MARRON}label: {color.VERDE}"
            _str += f"{self.label.rjust(63,'.')}{color.END}\n"

        if self.uuid is not None:
            _str += f"{color.MARRON}uuid: {color.VERDE}"
            _str += f"{self.uuid.rjust(64,'.')}{color.END}\n"

        if self.size is not None:
            _str += f"{color.MARRON}size: {color.VERDE}"
            _str += f"{self.size.rjust(64,'.')}{color.END}\n"

        if self.fstype is not None:
            _str += f"{color.MARRON}fstype: {color.VERDE}"
            _str += f"{self.fstype.rjust(62,'.')}{color.END}\n"

        if self.fssize is not None:
            _str += f"{color.MARRON}fssize: {color.VERDE}"
            _str += f"{self.fssize.rjust(62,'.')}{color.END}\n"

        if self.fsused is not None and self.fsuse is not None:
            _usado = f"{self.fsused} - {self.fsuse}"
            _str += f"{color.MARRON}usado: {color.VERDE}"
            _str += f"{_usado.rjust(63,'.')}{color.END}\n"

        if self.fsavail is not None:
            _str += f"{color.MARRON}libre: {color.VERDE}"
            _str += f"{self.fsavail.rjust(63,'.')}{color.END}\n"

        if self.mountpoint is not None:
            _str += f"{color.MARRON}mountpoint: {color.VERDE}"
            _str += f"{self.mountpoint.rjust(58,'.')}{color.END}\n"
        else:
            _str += f"{color.MARRON}mountpoint: {color.VERDE}"
            _str += f"{'None'.rjust(58,'.')}{color.END}\n"

        return _str

    def __find_volume(self):
        _childdevs = find_children(self.path)
        if len(_childdevs) > 0:
            self.__volume = Volume(_childdevs[0])
        else:
            self.__volume = None

    @property
    def volume(self):
        return self.__volume

    def open_volume(self, name, llave=None):
        if self.fstype != 'crypto_LUKS':
            raise RuntimeError(f'{self.name} no contiene volumen cifrado')
        if is_volume_open(name):
            return True

        _result = open_volume(self.path, name, llave)
        if _result:
            self.__find_volume()
        return _result

    def close_volume(self):
        if self.fstype != 'crypto_LUKS' or self.volume is None:
            raise RuntimeError("No dispongo de ningún volumen abierto")

        if self.volume.mountpoint is not None:
            self.volume.umount()
        if close_volume(self.volume.name):
            self.__find_volume()
