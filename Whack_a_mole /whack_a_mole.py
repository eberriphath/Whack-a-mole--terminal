from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


def hole():
    return Panel(
        "",
        width=9,
        height=3,
        box=box.ROUNDED,
        style="bold #A52A2A",  # brown color in hex
    )


def mole():
    return Panel(
        "🐹",
        width=9,
        height=3,
        box=box.ROUNDED,
        style="bold red on white",
    )


# Create a centered grid
grid = Table.grid(padding=(1, 4), expand=True)  # expand lets it stretch
grid.add_row(hole(), hole(), hole())
grid.add_row(mole(), hole(), mole())
grid.add_row(hole(), mole(), hole())

# Wrap the grid inside a centered panel
game_panel = Panel(
    grid,
    title="Whack-a-Mole",
    box=box.DOUBLE,
    style="on #FFFDD0",
    width=70,
    height=20,
)

console.print(game_panel, justify="center")  # center in terminal

import random

def random_mole_position():
    """Return a random (row, col) position for the mole in a 3x3 grid."""
    row = random.randint(0, 2)  # pick a row: 0, 1, or 2
    col = random.randint(0, 2)  # pick a column: 0, 1, or 2
    return (row, col)

#Test the random mole position function
print("\nTesting mole randomizer...")
for i in range(5):  # run 5 times
    pos = random_mole_position()
    print(f"Test {i+1}: Mole appeared at {pos}")