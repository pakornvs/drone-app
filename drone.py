import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from structures import Direction, Point


class Drone:
    def __init__(
        self,
        area=Point(5, 5),
        position=Point(1, 1),
        direction=Direction.NORTH,
        state_path=None,
    ):
        self.area = area
        self.position = position
        self.direction = direction
        self.state_path = Path(state_path or "state.json")
        self.load_state()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value.x < 1 or value.y < 1 or value.x > self.area.x or value.y > self.area.y:
            raise Exception(f"{value} is out of area")
        self._position = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value.x < 1 or value.y < 1:
            raise Exception("area must be greater than 0")
        self._area = value

    def get_current_location(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{now} | {self.direction}   | {self.position}"

    def move_forward(self):
        self.position = self.position + self.direction.value
        self.save_state()

    def turn_left(self):
        self.direction = Direction(
            Point(-self.direction.value.y, self.direction.value.x)
        )
        self.save_state()

    def turn_right(self):
        self.direction = Direction(
            Point(self.direction.value.y, -self.direction.value.x)
        )
        self.save_state()

    def reset(self):
        self.area = Point(5, 5)
        self.position = Point(1, 1)
        self.direction = Direction.NORTH
        self.save_state()

    def save_state(self):
        data = {
            "area": asdict(self.area),
            "position": asdict(self.position),
            "direction": self.direction.name,
        }
        with self.state_path.open("w+") as f:
            json.dump(data, f, indent=4)

    def load_state(self):
        if self.state_path.exists():
            with self.state_path.open() as f:
                data = json.load(f)
            if data.get("area"):
                self.area = Point(**data["area"])
            if data.get("position"):
                self.position = Point(**data["position"])
            if data.get("direction"):
                self.direction = Direction[data["direction"]]
