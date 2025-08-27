from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
import time

console = Console()


def hole():
    return Panel(
        "",
        width=9,
        height=3,
        box=box.ROUNDED,
        style="bold #A52A2A",
    )

def mole():
    return Panel(
        "🐹",
        width=9,
        height=3,
        box=box.ROUNDED,
        style="bold red on white",
    )

def show_grid():
    # 👉 YOUR ORIGINAL STATIC GRID
    grid = Table.grid(padding=(1, 4), expand=True)  
    grid.add_row(hole(), hole(), hole())  
    grid.add_row(mole(), hole(), mole())  
    grid.add_row(hole(), mole(), hole())

    game_panel = Panel(
        grid,
        title="Whack-a-Mole",
        box=box.DOUBLE,
        style="on #FFFDD0",
        width=70,
        height=20,
    )
    console.print(game_panel, justify="center")

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

