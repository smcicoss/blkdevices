#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ·
"""
===========================================================
                        test-demo.py
-----------------------------------------------------------
autor:  Simón Martínez <simon@cicoss.net>
fecha:  mar dic  1 21:24:35 CET 2020

script para la prueba y demostración de uso de
blkdevices
"""

import os
from mod.blockdevices import BlockDevices

miSistema = BlockDevices()

PassportUltra = miSistema.get_disk_wwn("0x50014ee6052b08c5")
print(PassportUltra)

for disk in miSistema.Disks:
    print(f"{disk.path} {disk.wwn.rjust(30,'.')}")

print(PassportUltra.partitions[0])
PassportUltra.partitions[0].open_volume('PassportUltra')

PassportUltra.partitions[0].volume.mount('/mnt/smbackup/PassportUltra')
print(PassportUltra.partitions[0].volume)

for filename in os.listdir(PassportUltra.partitions[0].volume.mountpoint):
    print(filename)

miSistema.eject(PassportUltra.wwn)
