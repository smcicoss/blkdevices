# BLKDEVICES

Dispositivos de Bloques

## Módulo Python 3

Módulo para la obtención de información sobre los dispositivos de bloques instalados en el sistema.
Basado en los resultados del comando de Linux lsblk.

### Ficheros

- blkdevices.py: Contiene la clase con la coleción de objetos de primer nivel.
- device.py: Contiene la clase de objetos de primer nivel (discos, cd-roms, loops).
- partition.py: Contiene la clase de objetos de segundo nivel (particiones).
- mapped.py: Contiene la clase de objetos de tercer nivel (Crypto Luks, volumenes, etc).
- test-demo.py: ejecutable de demostración y prueba.
