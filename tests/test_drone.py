import json
from dataclasses import asdict
from datetime import datetime

import pytest
from drone import Drone
from structures import Direction, Point


@pytest.fixture
def drone():
    drone = Drone(state_path="test_state.json")
    return drone


@pytest.mark.parametrize(
    "position, direction, expected_position, expected_direction",
    [
        (Point(2, 2), Direction.NORTH, Point(2, 3), Direction.NORTH),
        (Point(2, 2), Direction.EAST, Point(3, 2), Direction.EAST),
        (Point(2, 2), Direction.SOUTH, Point(2, 1), Direction.SOUTH),
        (Point(2, 2), Direction.WEST, Point(1, 2), Direction.WEST),
    ],
)
def test_move_forward(
    drone, position, direction, expected_position, expected_direction
):
    drone.position = position
    drone.direction = direction
    drone.move_forward()
    assert drone.position == expected_position
    assert drone.direction == expected_direction


@pytest.mark.parametrize(
    "position, direction, expected_position, expected_direction",
    [
        (Point(1, 1), Direction.NORTH, Point(1, 1), Direction.WEST),
        (Point(1, 1), Direction.WEST, Point(1, 1), Direction.SOUTH),
        (Point(1, 1), Direction.SOUTH, Point(1, 1), Direction.EAST),
        (Point(1, 1), Direction.EAST, Point(1, 1), Direction.NORTH),
    ],
)
def test_turn_left(drone, position, direction, expected_position, expected_direction):
    drone.position = position
    drone.direction = direction
    drone.turn_left()
    assert drone.position == expected_position
    assert drone.direction == expected_direction


@pytest.mark.parametrize(
    "position, direction, expected_position, expected_direction",
    [
        (Point(1, 1), Direction.NORTH, Point(1, 1), Direction.EAST),
        (Point(1, 1), Direction.EAST, Point(1, 1), Direction.SOUTH),
        (Point(1, 1), Direction.SOUTH, Point(1, 1), Direction.WEST),
        (Point(1, 1), Direction.WEST, Point(1, 1), Direction.NORTH),
    ],
)
def test_turn_right(drone, position, direction, expected_position, expected_direction):
    drone.position = position
    drone.direction = direction
    drone.turn_right()
    assert drone.position == expected_position
    assert drone.direction == expected_direction


def test_reset(drone):
    drone.area == Point(7, 7)
    drone.position == Point(3, 3)
    drone.direction == Direction.EAST
    drone.reset()
    assert drone.area == Point(5, 5)
    assert drone.position == Point(1, 1)
    assert drone.direction == Direction.NORTH


def test_area_out_of_range(drone):
    with pytest.raises(Exception):
        drone.area = Point(0, 0)


def test_position_out_of_range(drone):
    with pytest.raises(Exception):
        drone.position = Point(6, 6)


def test_get_current_location(drone):
    drone.position = Point(2, 3)
    drone.direction = Direction.SOUTH
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert drone.get_current_location() == f"{now} | SOUTH ⬇️   | (2, 3)"


def test_save_state(drone):
    drone.save_state()
    data = json.dumps(
        {
            "area": asdict(drone.area),
            "position": asdict(drone.position),
            "direction": drone.direction.name,
        },
        indent=4,
    )
    assert drone.state_path.read_text() == data


def test_load_state(drone):
    drone.area == Point(5, 5)
    drone.position == Point(1, 1)
    drone.direction == Direction.NORTH
    drone.save_state()
    drone.load_state()
    assert drone.area == Point(5, 5)
    assert drone.position == Point(1, 1)
    assert drone.direction == Direction.NORTH
