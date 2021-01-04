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

from mod.blkdevdata import BlkDevData


class Volume(BlkDevData):
    def __init__(self, data=None):
        super().__init__(data)
        self.properties = [
            'name', 'kname', 'path', 'fsavail', 'fssize', 'fstype', 'fsused',
            'fsuse%', 'mountpoint', 'label', 'uuid', 'size', 'mode', 'rota',
            'type', 'pkname'
        ]

        if type(data) == tyep(dict) or \
                type(data) == type(BlkDevData) or \
                type(data) == type(Volume):
            for prop in self.properties:
                self[prop] == data[prop]

    @property
    def children(self):
        return None
