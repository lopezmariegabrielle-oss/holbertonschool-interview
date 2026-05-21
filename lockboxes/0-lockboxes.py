#!/usr/bin/python3
"""
Module pour résoudre le problème des lockboxes.
"""


def canUnlockAll(boxes):
    """
    Détermine si toutes les boîtes verrouillées peuvent être ouvertes.
    """

    opened_boxes = [0]
    i = 0

    while i < len(opened_boxes):
        current_box = opened_boxes[i]

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.append(key)
        i += 1

    return len(opened_boxes) == len(boxes)
