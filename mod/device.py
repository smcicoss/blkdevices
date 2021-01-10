# -*- coding: utf-8 -*-
# ·

import os
import subprocess
from pathlib import Path
from mod.blkdevdata import BlkDevData
from mod.readdevice import read_device


class Device(BlkDevData):
    def __init__(self, data):
        if isinstance(data, str):
            # ha de ser un path al device
            if not os.path.exists(data) or not Path(data).is_block_device():
                raise ValueError(
                    f"El disco '{data}' no existe o no está conectado")
            _dev = read_device(data)[0]
        else:
            _dev = data

        super().__init__(_dev)

    def __getitem__(self, item):
        if item == 'children':
            return self.__children
        return super().__getitem__(item)

    def mount(self, mountpoint):
        if self.mountpoint is not None:
            # ya está montado
            return False

        if not os.path.exists(mountpoint):
            # no existe el punto de montado
            return False

        _result = subprocess.check_call("sudo mount -o defaults " +
                                        f"{self.path} {mountpoint}",
                                        shell=True)
        if _result == 0:
            self.mountpoint = mountpoint
            return True
        return False

    def umount(self):
        if self.mountpoint is None:
            raise OSError

        _result = subprocess.check_call(f"sudo umount {self.path}", shell=True)

        if _result == 0:
            self.mountpoint = None
            return True
        return False
