#!/usr/bin/python3
"""
Module pour valider l'encodage UTF-8
"""


def validUTF8(data):
    nombre_octets_attendus = 0
    for entier in data:
        octet = entier & 255
        octet_bin = bin(octet)[2:].zfill(8)

        if nombre_octets_attendus == 0:
            if octet_bin.startswith("0"):
                nombre_octets_attendus = 0

            elif octet_bin.startswith("110"):
                nombre_octets_attendus = 1

            elif octet_bin.startswith("1110"):
                nombre_octets_attendus = 2

            elif octet_bin.startswith("11110"):
                nombre_octets_attendus = 3

            else:
                return False

        else:
            if octet_bin.startswith("10"):
                nombre_octets_attendus -= 1
            else:
                return False

    return nombre_octets_attendus == 0
