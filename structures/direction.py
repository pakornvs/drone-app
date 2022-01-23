from enum import Enum

from .point import Point


class Direction(Enum):
    NORTH = Point(0, 1)
    EAST = Point(1, 0)
    SOUTH = Point(0, -1)
    WEST = Point(-1, 0)

    def __str__(self):
        return {
            "NORTH": "NORTH ⬆️",
            "EAST": "EAST  ➡️",
            "SOUTH": "SOUTH ⬇️",
            "WEST": "WEST  ⬅️",
        }[self.name]
