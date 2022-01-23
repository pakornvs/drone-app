from time import sleep

import typer

from drone import Drone
from structures import Point

app = typer.Typer(add_completion=False)
drone = Drone()


@app.command(help="Reset drone to initial state")
def reset():
    typer.echo("Resetting drone...")
    drone.reset()
    sleep(1)  # Simulate drone action
    typer.echo("Drone reset")


@app.command(help="Start moving drone")
def start(
    width: int = typer.Option(None, help="Set width of area (wah)"),
    height: int = typer.Option(None, help="Set height of area (wah)"),
    file: typer.FileText = typer.Option(
        "input.txt",
        help="Path to txt file containing commands to execute",
    ),
):
    cmds = []
    for line in file:
        cmds += [x.strip() for x in line.split(",")]

    if cmds:
        try:
            if width:
                drone.area = Point(width, drone.area.y)
            if height:
                drone.area = Point(drone.area.x, height)
            typer.echo("")
            typer.echo("      Date Time     | Direction | Position")
            typer.echo("--------------------+-----------+----------")
            typer.echo(drone.get_current_location())
            for cmd in cmds:
                if cmd == "M":
                    drone.move_forward()
                elif cmd == "L":
                    drone.turn_left()
                elif cmd == "R":
                    drone.turn_right()
                else:
                    raise ValueError(f"Unknown command: {cmd}")
                sleep(0.5)  # Simulate drone action
                typer.echo(drone.get_current_location())
        except Exception as e:
            typer.echo(f"\n{e}")


if __name__ == "__main__":
    app()
