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

from mod.blkdevices import BlockDevices

if __name__ == '__main__':
    # instancio la clase colección
    misDevices = BlockDevices()

    # sumario de dispositivos
    ndev = len(misDevices.ListDevices)
    print(f"El sistema cuenta con {ndev} ", end='')
    print("dispositivos de bloque")
    print(f"de los cuales {len(misDevices.ListDisks)} son discos físicos")
    print(f"y de estos {len(misDevices.find_usb_disks())} son unidades USB")
    print(
        f"y {len(misDevices.find_ssd_disks())} son unidades estáticas SSD\n\n")

    # listo particiones
    for dev in misDevices.ListDisks:
        for part in dev.partitions:
            print(f"Partición {part.kname} con label {part.label}")
            print(f"\t device {part.path} montado en {part.mountpoint}")
            for map in part.mapped:
                print(f"\t\tMapeado {map.kname} con label {map.label}")
                print(f"\t\t\t device {map.path} montado en {map.mountpoint}")

    # obtengo los datos del dispositivo montado en direcotrio
    directorio = "/home/simo/Datos/Externos-USB/Passport-Ultra"
    pm = misDevices.mounted_in(directorio)
    if pm is not None:
        print(f"\n\nEn '/' está montado el {pm.path} de tipo {pm.type}")
        print(f"\tcon label {pm.label} y UUID {pm.uuid}")
        print(f"El systema de archivos es de tipo {pm.fstype}")
        print(
            f"\t con una capacidad de {pm.fssize} y utilizado en un {pm.fsuse}"
        )
        print(f"\ttiene disponibles {pm.fsavail}")

    print("\n\nVerificar si una unidad está conectada")
    uuid = input("Introduzca el UUID de la unidad: ")
    if uuid == "":
        exit(0)
    if misDevices.is_connected(uuid):
        print(f"la unidad {uuid} está conectada")
    else:
        print(f"La unidad {uuid} no existe o no está conectada")

    dev = misDevices.full_search_uuid(uuid)
    dev = dev[dev['en']]
    montados = misDevices.has_mounted(uuid)
    if montados is not None:
        if len(montados) > 0:
            print(f"El {dev.type} {dev.path} tiene montados:")
            for dmontado in montados:
                print(f"{dmontado.type} - " +
                      f"{dmontado.path} en {dmontado.mountpoint}")
        else:
            print(f"El {dev.type} {dev.path} no tiene nada montado")

    PassportUltra = misDevices.full_search_path("/dev/mapper/Passport-Ultra")

    print(f"\n{PassportUltra.kname} - " +
          f"{PassportUltra.name} {PassportUltra.fsavail}")

    PassportUltra = misDevices.full_search_name("Passport-Ultra")
    if PassportUltra is not None:
        print(f"\n{PassportUltra.kname} - " +
              f"{PassportUltra.name} {PassportUltra.fsavail}")
