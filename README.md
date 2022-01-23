# Automatic Drone Farmer

A command-line application for Automatic Drone Farmer Challenge.

## Requirements

- Python 3.8+
- [Poetry](https://python-poetry.org/docs/#installation")

## Installation

Use Poetry to install all dependencies:

```text
poetry install
```

## Basic usage

To start moving drone simply run:

```text
poetry run python app.py start --width 10 --height 10
```

Example output:

```text
      Date Time     | Direction | Position
--------------------+-----------+----------
2022-01-23 07:39:46 | NORTH ⬆️  | (1, 1)
2022-01-23 07:39:46 | NORTH ⬆️  | (1, 2)
2022-01-23 07:39:47 | NORTH ⬆️  | (1, 3)
2022-01-23 07:39:47 | EAST  ➡️  | (1, 3)
2022-01-23 07:39:48 | EAST  ➡️  | (2, 3)
2022-01-23 07:39:48 | SOUTH ⬇️  | (2, 3)
2022-01-23 07:39:49 | SOUTH ⬇️  | (2, 2)
```

To see all command options:

```text
poetry run python app.py start --help
```

The output will looks like:

```text
Usage: app.py start [OPTIONS]

  Start moving drone

Options:
  --width INTEGER   Set width of area (wah)
  --height INTEGER  Set height of area (wah)
  --file FILENAME   Path to txt file containing commands to execute  [default:input.txt]
  --help            Show this message and exit.
```

To reset drone to its initial state:

```text
poetry run python app.py reset
```

## Testing

To see test coverage report run:

```text
poetry run coverage run -m pytest && poetry run coverage report -m
```
