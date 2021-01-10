# -*- coding: utf-8 -*-
# ·

import subprocess
import json
import os


def read_device(pathdev):
    _cmd_shell = "sudo lsblk -OJ {0}".format(pathdev)
    _blkdevs = subprocess.run(_cmd_shell,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    if _blkdevs.returncode != 0:
        return None
    return json.loads(_blkdevs.stdout.decode('UTF-8'))['blockdevices']


def find_children(pathdev):
    _cmd_shell = "sudo lsblk -Jo PATH,PKNAME {0}".format(pathdev)
    _blkdevs = subprocess.run(_cmd_shell,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
    if _blkdevs.returncode != 0:
        return None
    _devblks = json.loads(_blkdevs.stdout.decode('UTF-8'))['blockdevices']
    _pkname = os.path.split(pathdev)[1]
    _children = []
    for _dev in _devblks:
        if _dev['pkname'] == _pkname:
            _children.append(_dev['path'])
    return _children


def is_volume_open(name):
    _cmd = f"sudo cryptsetup status {name} >/dev/null"

    if subprocess.call(_cmd, shell=True) == 0:
        return True
    else:
        return False


def open_volume(pathdev, name, llave=None):
    if llave is None or not os.path.isfile(llave):
        _cmd = f"sudo cryptsetup luksOpen {pathdev} {name} >/dev/null"
    else:
        _cmd = f"sudo cryptsetup --key-file={llave} " + \
                f"luksOpen {pathdev} {name} >/dev/null"

    _result = subprocess.run(_cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
    if _result.returncode == 0:
        return True
    else:
        print(_result.stderr.decode('UTF-8'))
        return False


def close_volume(name):
    if not is_volume_open(name):
        return True
    _cmd = f'sudo cryptsetup close {name} &>/dev/null'
    if subprocess.call(_cmd, shell=True) == 0:
        return True
    else:
        raise OSError(f"No se ha podido cerrar el volumen {name}")
