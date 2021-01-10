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

from mod.device import Device
from mod.partition import Partition
from mod.readdevice import find_children
from utiles.strutil import h2
from utiles.color import Color


class Disk(Device):
    def __init__(self, data):

        super().__init__(data)

        if self.type != 'disk':
            raise ValueError(
                f"Los datos no corresponden a un disco ({self.type})")

        self.properties = [
            "name", "kname", "path", "ptuuid", "pttype", "hotplug", "model",
            "serial", "size", "state", "mode", "type", "wwn", "rand", "hctl",
            "tran", "subsystems", "rev", "vendor", "zoned"
        ]

        _childdevs = find_children(self.path)
        if len(_childdevs) > 0:
            self.__partitions = []
            for childpath in _childdevs:
                self.__partitions.append(Partition(childpath))
        else:
            self.__partitions = None

    def __str__(self):
        color = Color()
        if self.model is None:
            _str = h2(f"Disco {self.path}", 70)
        else:
            _str = h2(f"Disco {self.path} [{self.model}]", 70)
        _str += f"{color.MARRON}name: {color.VERDE}"
        _str += f"{self.name.rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}kname: {color.VERDE}"
        _str += f"{self.kname.rjust(63,'.')}{color.END}\n"

        _str += f"{color.MARRON}path: {color.VERDE}"
        _str += f"{self.path.rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}wwn: {color.VERDE}"
        _str += f"{self.wwn.rjust(65,'.')}{color.END}\n"

        _str += f"{color.MARRON}model: {color.VERDE}"
        _str += f"{self.model.rjust(63,'.')}{color.END}\n"

        _str += f"{color.MARRON}vendor: {color.VERDE}"
        _str += f"{self.vendor.strip().rjust(62,'.')}{color.END}\n"

        _str += f"{color.MARRON}serial: {color.VERDE}"
        _str += f"{self.serial.strip().rjust(62,'.')}{color.END}\n"

        _str += f"{color.MARRON}size: {color.VERDE}"
        _str += f"{self.size.strip().rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}tran: {color.VERDE}"
        _str += f"{self.tran.strip().rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}rota: {color.VERDE}"
        _rota = str(self.rota)
        _str += f"{_rota.rjust(64,'.')}{color.END}\n"

        if self.label is not None:
            _str += f"{color.MARRON}label: {color.VERDE}"
            _str += f"{self.label.rjust(63,'.')}{color.END}\n"

        if self.uuid is not None:
            _str += f"{color.MARRON}uuid: {color.VERDE}"
            _str += f"{self.uuid.rjust(64,'.')}{color.END}\n"

        if self.fstype is not None:
            _str += f"{color.MARRON}fstype: {color.VERDE}"
            _str += f"{self.fstype.rjust(62,'.')}{color.END}\n"

        if self.fssize is not None:
            _str += f"{color.MARRON}fssize: {color.VERDE}"
            _str += f"{self.fssize.rjust(62,'.')}{color.END}\n"

            _usado = f"{self.fsused} - {self.fsuse}"
            _str += f"{color.MARRON}usado: {color.VERDE}"
            _str += f"{_usado.rjust(63,'.')}{color.END}\n"

            _str += f"{color.MARRON}libre: {color.VERDE}"
            _str += f"{self.fsavail.rjust(63,'.')}{color.END}\n"

        if self.mountpoint is not None:
            _str += f"{color.MARRON}mountpoint: {color.VERDE}"
            _str += f"{self.mountpoint.rjust(68,'.')}{color.END}\n"

        return _str

    @property
    def partitions(self):
        return self.__partitions
