from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
