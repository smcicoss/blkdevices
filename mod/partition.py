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

import os
import subprocess
from mod.mapped import Mapped
from utiles.strutil import h2
from utiles.color import Color


class PartitionType():
    def __init__(self):
        self.__parttype = [  # Lista de tipos de particiones
            {
                "nfdisk": "1",
                "uuid": "C12A7328-F81F-11D2-BA4B-00A0C93EC93B",
                "name": "EFI System"
            }, {
                "nfdisk": "2",
                "uuid": "024DEE41-33E7-11D3-9D69-0008C781F39F",
                "name": "MBR partition scheme"
            }, {
                "nfdisk": "3",
                "uuid": "D3BFE2DE-3DAF-11DF-BA40-E3A556D89593",
                "name": "Intel Fast Flash"
            }, {
                "nfdisk": "4",
                "uuid": "21686148-6449-6E6F-744E-656564454649",
                "name": "BIOS boot"
            }, {
                "nfdisk": "5",
                "uuid": "F4019732-066E-4E12-8273-346C5641494F",
                "name": "Sony boot partition"
            }, {
                "nfdisk": "6",
                "uuid": "BFBFAFE7-A34F-448A-9A5B-6213EB736C22",
                "name": "Lenovo boot partition"
            }, {
                "nfdisk": "7",
                "uuid": "9E1A2D38-C612-4316-AA26-8B49521E5A8B",
                "name": "PowerPC PReP boot"
            }, {
                "nfdisk": "8",
                "uuid": "7412F7D5-A156-4B13-81DC-867174929325",
                "name": "ONIE boot"
            }, {
                "nfdisk": "9",
                "uuid": "D4E6E2CD-4469-46F3-B5CB-1BFF57AFC149",
                "name": "ONIE config"
            }, {
                "nfdisk": "10",
                "uuid": "E3C9E316-0B5C-4DB8-817D-F92DF00215AE",
                "name": "Microsoft reserved"
            }, {
                "nfdisk": "11",
                "uuid": "EBD0A0A2-B9E5-4433-87C0-68B6B72699C7",
                "name": "Microsoft basic data"
            }, {
                "nfdisk": "12",
                "uuid": "5808C8AA-7E8F-42E0-85D2-E1E90434CFB3",
                "name": "Microsoft LDM metadata"
            }, {
                "nfdisk": "13",
                "uuid": "AF9B60A0-1431-4F62-BC68-3311714A69AD",
                "name": "Microsoft LDM data"
            }, {
                "nfdisk": "14",
                "uuid": "DE94BBA4-06D1-4D40-A16A-BFD50179D6AC",
                "name": "Windows recovery environment"
            }, {
                "nfdisk": "15",
                "uuid": "37AFFC90-EF7D-4E96-91C3-2D7AE055B174",
                "name": "IBM General Parallel Fs"
            }, {
                "nfdisk": "16",
                "uuid": "E75CAF8F-F680-4CEE-AFA3-B001E56EFC2D",
                "name": "Microsoft Storage Spaces"
            }, {
                "nfdisk": "17",
                "uuid": "75894C1E-3AEB-11D3-B7C1-7B03A0000000",
                "name": "HP-UX data"
            }, {
                "nfdisk": "18",
                "uuid": "E2A1E728-32E3-11D6-A682-7B03A0000000",
                "name": "HP-UX service"
            }, {
                "nfdisk": "19",
                "uuid": "0657FD6D-A4AB-43C4-84E5-0933C84B4F4F",
                "name": "Linux swap"
            }, {
                "nfdisk": "20",
                "uuid": "0FC63DAF-8483-4772-8E79-3D69D8477DE4",
                "name": "Linux filesystem"
            }, {
                "nfdisk": "21",
                "uuid": "3B8F8425-20E0-4F3B-907F-1A25A76F98E8",
                "name": "Linux server data"
            }, {
                "nfdisk": "22",
                "uuid": "44479540-F297-41B2-9AF7-D131D5F0458A",
                "name": "Linux root (x86)"
            }, {
                "nfdisk": "23",
                "uuid": "69DAD710-2CE4-4E3C-B16C-21A1D49ABED3",
                "name": "Linux root (ARM)"
            }, {
                "nfdisk": "24",
                "uuid": "4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709",
                "name": "Linux root (x86-64)"
            }, {
                "nfdisk": "25",
                "uuid": "B921B045-1DF0-41C3-AF44-4C6F280D3FAE",
                "name": "Linux root (ARM-64)"
            }, {
                "nfdisk": "26",
                "uuid": "993D8D3D-F80E-4225-855A-9DAF8ED7EA97",
                "name": "Linux root  (IA-64)"
            }, {
                "nfdisk": "27",
                "uuid": "8DA63339-0007-60C0-C436-083AC8230908",
                "name": "Linux reserved"
            }, {
                "nfdisk": "28",
                "uuid": "933AC7E1-2EB4-4F13-B844-0E14E2AEF915",
                "name": "Linux home"
            }, {
                "nfdisk": "29",
                "uuid": "A19D880F-05FC-4D3B-A006-743F0F84911E",
                "name": "Linux RAID"
            }, {
                "nfdisk": "30",
                "uuid": "BC13C2FF-59E6-4262-A352-B275FD6F7172",
                "name": "Linux extended boot"
            }, {
                "nfdisk": "31",
                "uuid": "E6D6D379-F507-44C2-A23C-238F2A3DF928",
                "name": "Linux LVM"
            }, {
                "nfdisk": "32",
                "uuid": "516E7CB4-6ECF-11D6-8FF8-00022D09712B",
                "name": "FreeBSD data"
            }, {
                "nfdisk": "33",
                "uuid": "83BD6B9D-7F41-11DC-BE0B-001560B84F0F",
                "name": "FreeBSD boot"
            }, {
                "nfdisk": "34",
                "uuid": "516E7CB5-6ECF-11D6-8FF8-00022D09712B",
                "name": "FreeBSD swap"
            }, {
                "nfdisk": "35",
                "uuid": "516E7CB6-6ECF-11D6-8FF8-00022D09712B",
                "name": "FreeBSD UFS"
            }, {
                "nfdisk": "36",
                "uuid": "516E7CBA-6ECF-11D6-8FF8-00022D09712B",
                "name": "FreeBSD ZFS"
            }, {
                "nfdisk": "37",
                "uuid": "516E7CB8-6ECF-11D6-8FF8-00022D09712B",
                "name": "FreeBSD Vinum"
            }, {
                "nfdisk": "38",
                "uuid": "48465300-0000-11AA-AA11-00306543ECAC",
                "name": "Apple HFS/HFS+"
            }, {
                "nfdisk": "39",
                "uuid": "55465300-0000-11AA-AA11-00306543ECAC",
                "name": "Apple UFS"
            }, {
                "nfdisk": "40",
                "uuid": "52414944-0000-11AA-AA11-00306543ECAC",
                "name": "Apple RAID"
            }, {
                "nfdisk": "41",
                "uuid": "52414944-5F4F-11AA-AA11-00306543ECAC",
                "name": "Apple RAID offline"
            }, {
                "nfdisk": "42",
                "uuid": "426F6F74-0000-11AA-AA11-00306543ECAC",
                "name": "Apple boot"
            }, {
                "nfdisk": "43",
                "uuid": "4C616265-6C00-11AA-AA11-00306543ECAC",
                "name": "Apple label"
            }, {
                "nfdisk": "44",
                "uuid": "5265636F-7665-11AA-AA11-00306543ECAC",
                "name": "Apple TV recovery"
            }, {
                "nfdisk": "45",
                "uuid": "53746F72-6167-11AA-AA11-00306543ECAC",
                "name": "Apple Core storage"
            }, {
                "nfdisk": "46",
                "uuid": "6A82CB45-1DD2-11B2-99A6-080020736631",
                "name": "Solaris boot"
            }, {
                "nfdisk": "47",
                "uuid": "6A85CF4D-1DD2-11B2-99A6-080020736631",
                "name": "Solaris root"
            }, {
                "nfdisk": "48",
                "uuid": "6A898CC3-1DD2-11B2-99A6-080020736631",
                "name": "Solaris /usr & Apple ZFS"
            }, {
                "nfdisk": "49",
                "uuid": "6A87C46F-1DD2-11B2-99A6-080020736631",
                "name": "Solaris swap"
            }, {
                "nfdisk": "50",
                "uuid": "6A8B642B-1DD2-11B2-99A6-080020736631",
                "name": "Solaris backup"
            }, {
                "nfdisk": "51",
                "uuid": "6A8EF2E9-1DD2-11B2-99A6-080020736631",
                "name": "Solaris /var"
            }, {
                "nfdisk": "52",
                "uuid": "6A90BA39-1DD2-11B2-99A6-080020736631",
                "name": "Solaris /home"
            }, {
                "nfdisk": "53",
                "uuid": "6A9283A5-1DD2-11B2-99A6-080020736631",
                "name": "Solaris alternate sector"
            }, {
                "nfdisk": "54",
                "uuid": "6A945A3B-1DD2-11B2-99A6-080020736631",
                "name": "Solaris reserved 1"
            }, {
                "nfdisk": "55",
                "uuid": "6A9630D1-1DD2-11B2-99A6-080020736631",
                "name": "Solaris reserved 2"
            }, {
                "nfdisk": "56",
                "uuid": "6A980767-1DD2-11B2-99A6-080020736631",
                "name": "Solaris reserved 3"
            }, {
                "nfdisk": "57",
                "uuid": "6A96237F-1DD2-11B2-99A6-080020736631",
                "name": "Solaris reserved 4"
            }, {
                "nfdisk": "58",
                "uuid": "6A8D2AC7-1DD2-11B2-99A6-080020736631",
                "name": "Solaris reserved 5"
            }, {
                "nfdisk": "59",
                "uuid": "49F48D32-B10E-11DC-B99B-0019D1879648",
                "name": "NetBSD swap"
            }, {
                "nfdisk": "60",
                "uuid": "49F48D5A-B10E-11DC-B99B-0019D1879648",
                "name": "NetBSD FFS"
            }, {
                "nfdisk": "61",
                "uuid": "49F48D82-B10E-11DC-B99B-0019D1879648",
                "name": "NetBSD LFS"
            }, {
                "nfdisk": "62",
                "uuid": "2DB519C4-B10E-11DC-B99B-0019D1879648",
                "name": "NetBSD concatenated"
            }, {
                "nfdisk": "63",
                "uuid": "2DB519EC-B10E-11DC-B99B-0019D1879648",
                "name": "NetBSD encrypted"
            }, {
                "nfdisk": "64",
                "uuid": "49F48DAA-B10E-11DC-B99B-0019D1879648",
                "name": "NetBSD RAID"
            }, {
                "nfdisk": "65",
                "uuid": "FE3A2A5D-4F32-41A7-B725-ACCC3285A309",
                "name": "ChromeOS kernel"
            }, {
                "nfdisk": "66",
                "uuid": "3CB8E202-3B7E-47DD-8A3C-7FF2A13CFCEC",
                "name": "ChromeOS root fs"
            }, {
                "nfdisk": "67",
                "uuid": "2E0A753D-9E48-43B0-8337-B15192CB1B5E",
                "name": "ChromeOS reserved"
            }, {
                "nfdisk": "68",
                "uuid": "85D5E45A-237C-11E1-B4B3-E89A8F7FC3A7",
                "name": "MidnightBSD data"
            }, {
                "nfdisk": "69",
                "uuid": "85D5E45E-237C-11E1-B4B3-E89A8F7FC3A7",
                "name": "MidnightBSD boot"
            }, {
                "nfdisk": "70",
                "uuid": "85D5E45B-237C-11E1-B4B3-E89A8F7FC3A7",
                "name": "MidnightBSD swap"
            }, {
                "nfdisk": "71",
                "uuid": "0394EF8B-237E-11E1-B4B3-E89A8F7FC3A7",
                "name": "MidnightBSD UFS"
            }, {
                "nfdisk": "72",
                "uuid": "85D5E45D-237C-11E1-B4B3-E89A8F7FC3A7",
                "name": "MidnightBSD ZFS"
            }, {
                "nfdisk": "73",
                "uuid": "85D5E45C-237C-11E1-B4B3-E89A8F7FC3A7",
                "name": "MidnightBSD Vinum"
            }, {
                "nfdisk": "74",
                "uuid": "45B0969E-9B03-4F30-B4C6-B4B80CEFF106",
                "name": "Ceph Journal"
            }, {
                "nfdisk": "75",
                "uuid": "45B0969E-9B03-4F30-B4C6-5EC00CEFF106",
                "name": "Ceph Encrypted Journal"
            }, {
                "nfdisk": "76",
                "uuid": "4FBD7E29-9D25-41B8-AFD0-062C0CEFF05D",
                "name": "Ceph OSD"
            }, {
                "nfdisk": "77",
                "uuid": "4FBD7E29-9D25-41B8-AFD0-5EC00CEFF05D",
                "name": "Ceph crypt OSD"
            }, {
                "nfdisk": "78",
                "uuid": "89C57F98-2FE5-4DC0-89C1-F3AD0CEFF2BE",
                "name": "Ceph disk in creation"
            }, {
                "nfdisk": "79",
                "uuid": "89C57F98-2FE5-4DC0-89C1-5EC00CEFF2BE",
                "name": "Ceph crypt disk in creation"
            }, {
                "nfdisk": "80",
                "uuid": "AA31E02A-400F-11DB-9590-000C2911D1B8",
                "name": "VMware VMFS"
            }, {
                "nfdisk": "81",
                "uuid": "9D275380-40AD-11DB-BF97-000C2911D1B8",
                "name": "VMware Diagnostic"
            }, {
                "nfdisk": "82",
                "uuid": "381CFCCC-7288-11E0-92EE-000C2911D0B2",
                "name": "VMware Virtual SAN"
            }, {
                "nfdisk": "83",
                "uuid": "77719A0C-A4A0-11E3-A47E-000C29745A24",
                "name": "VMware Virsto"
            }, {
                "nfdisk": "84",
                "uuid": "9198EFFC-31C0-11DB-8F78-000C2911D1B8",
                "name": "VMware Reserved"
            }, {
                "nfdisk": "85",
                "uuid": "824CC7A0-36A8-11E3-890A-952519AD3F61",
                "name": "OpenBSD data"
            }, {
                "nfdisk": "86",
                "uuid": "CEF5A9AD-73BC-4601-89F3-CDEEEEE321A1",
                "name": "QNX6 file system"
            }, {
                "nfdisk": "87",
                "uuid": "C91818F9-8025-47AF-89D2-F030D7000C2C",
                "name": "Plan 9 partition"
            }
        ]

    def find_type(self, uuid):
        n = 0
        for partype in self.__parttype:
            if partype['uuid'].lower() == uuid.lower():
                return self.__parttype[n]
            n += 1
        return None

    def get_nfdisk(self, num):
        if num > len(self.__parttype):
            return None
        if int(self.__parttype[num - 1]['nfdisk']) != num:
            return None
        else:
            return self.__parttype[num - 1]


class Partition:
    """
    Particiones

    Clase de objetos partición de disco
    """
    def __init__(self, son):
        """
        __init__ Constructor

        Trasfiere los datos en formato dictionary (resultado de lectura json)
        a formato propiedades

        Args:
            son (dictionary): Datos provinientes de la carga json
        """
        self.__name = son['name']
        self.__kname = son['kname']
        self.__path = son['path']
        self.__fsavail = son['fsavail']
        self.__fssize = son['fssize']
        self.__fstype = son['fstype']
        self.__fsused = son['fsused']
        self.__fsuse = son['fsuse%']
        self.__mountpoint = son['mountpoint']
        self.__label = son['label']
        self.__uuid = son['uuid']
        self.__parttype = son['parttype']
        self.__partlabel = son['partlabel']
        self.__partuuid = son['partuuid']
        self.__size = son['size']
        self.__mode = son['mode']
        self.__rota = son['rota']
        self.__type = son['type']
        self.__pkname = son['pkname']
        self.__mapped = []
        if "children" in son:
            for mapp in son['children']:
                self.__mapped.append(Mapped(mapp))

    def __str__(self):
        color = Color()
        if self.label is None:
            _str = h2(f"Partición {self.path}", 60)
        else:
            _str = h2(f"Partición {self.path} [{self.label}]", 60)
        _str += f"{color.MARRON}name: {color.VERDE}"
        _str += f"{self.name.rjust(54,'.')}{color.END}\n"

        _str += f"{color.MARRON}kname: {color.VERDE}"
        _str += f"{self.kname.rjust(53,'.')}{color.END}\n"

        _str += f"{color.MARRON}path: {color.VERDE}"
        _str += f"{self.path.rjust(54,'.')}{color.END}\n"

        _str += f"{color.MARRON}parttype: {color.VERDE}"
        _str += f"{self.parttype.rjust(50,'.')}{color.END}\n"

        _parttype = PartitionType()
        _parttypename = _parttype.find_type(self.parttype)['name']
        _str += f"{color.VERDE}{_parttypename.rjust(60)}{color.END}\n"

        if self.label is not None:
            _str += f"{color.MARRON}label: {color.VERDE}"
            _str += f"{self.label.rjust(53,'.')}{color.END}\n"

        _str += f"{color.MARRON}uuid: {color.VERDE}"
        _str += f"{self.uuid.rjust(54,'.')}{color.END}\n"

        _str += f"{color.MARRON}fstype: {color.VERDE}"
        _str += f"{self.fstype.rjust(52,'.')}{color.END}\n"

        if self.fssize is not None:
            _str += f"{color.MARRON}fssize: {color.VERDE}"
            _str += f"{self.fssize.rjust(52,'.')}{color.END}\n"

            _usado = f"{self.fsused} - {self.fsuse}"
            _str += f"{color.MARRON}usado: {color.VERDE}"
            _str += f"{_usado.rjust(53,'.')}{color.END}\n"

            _str += f"{color.MARRON}libre: {color.VERDE}"
            _str += f"{self.fsavail.rjust(53,'.')}{color.END}\n"

        _str += f"{color.MARRON}fstype: {color.VERDE}"
        _str += f"{self.fstype.rjust(52,'.')}{color.END}\n"

        if self.mountpoint is not None:
            _str += f"{color.MARRON}mountpoint: {color.VERDE}"
            _str += f"{self.mountpoint.rjust(48,'.')}{color.END}\n"

        return _str

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

    @property
    def sons(self):
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

    def mount(self, mountpoint):
        if self.__mountpoint is not None:
            # ya está montado
            return False

        if not os.path.exists(mountpoint):
            # no existe el punto de montado
            return False

        _result = subprocess.check_call("sudo mount -o defaults " +
                                        f"{self.__path} {mountpoint}",
                                        shell=True)
        if _result == 0:
            return True
        return False

    def umount(self):
        if self.__mountpoint is None:
            return False
        _result = subprocess.check_call(f"sudo umount {self.__path}",
                                        shell=True)

        if _result == 0:
            return True
        return False
