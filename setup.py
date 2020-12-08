# -*- coding: utf-8 -*-
# ·

from setuptools import setup, find_packages

setup(
    name="blkdevices",
    version="0.1.1",
    description=
    "Módulo para información del los dispositivos de bloque en el sistema",
    author="Simón Martínez",
    author_email='simon@cicoss.net',
    license="GPL",
    url="https://avueltasconlinux.wordpress.com/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Operating System :: Linux",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    test_suite="test-demo",
    scripts=["test-demo/test-blkdevices.py"],
)
