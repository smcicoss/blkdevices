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

from mod.device import Device
from utiles.strutil import h2
from utiles.color import Color


class Volume(Device):
    def __init__(self, data):
        super().__init__(data)

        self.properties = [
            'name', 'kname', 'path', 'fsavail', 'fssize', 'fstype', 'fsused',
            'fsuse%', 'mountpoint', 'label', 'uuid', 'size', 'mode', 'rota',
            'type', 'pkname'
        ]

    def __str__(self):
        color = Color()
        if self.label is None:
            _str = h2(f"Volumen {self.path}", 70)
        else:
            _str = h2(f"Volumen {self.path} [{self.label}]", 70)
        _str += f"{color.MARRON}name: {color.VERDE}"
        _str += f"{self.name.rjust(64,'.')}{color.END}\n"

        _str += f"{color.MARRON}kname: {color.VERDE}"
        _str += f"{self.kname.rjust(63,'.')}{color.END}\n"

        _str += f"{color.MARRON}path: {color.VERDE}"
        _str += f"{self.path.rjust(64,'.')}{color.END}\n"

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
