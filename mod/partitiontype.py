# -*- coding: utf-8 -*-
# ·


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
                "nfdisk": "70",
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
        for partype in self.__parttype:
            if partype['uuid'].lower() == uuid.lower():
                return partype
        return None

    def get_nfdisk(self, num):
        if num > len(self.__parttype):
            return None
        if int(self.__parttype[num - 1]['nfdisk']) != num:
            return None
        else:
            return self.__parttype[num - 1]
