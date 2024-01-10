#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    visited_boxes = []
    keys = [0]

    while len(visited_boxes) < len(boxes) and len(keys) >= 1:
        new_keys = []
        for key in keys:
            if key not in visited_boxes and 0 <= key < len(boxes):
                new_keys += boxes[key]
                visited_boxes.append(key)
        keys = new_keys
    if len(visited_boxes) != len(boxes):
        return False
    else:
        return True
