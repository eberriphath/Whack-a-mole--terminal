	
# Abdihakim Ali
# 2:42 PM







# from rich.console import Console
# from rich.panel import Panel
# from rich.table import Table
# from rich import box

# console = Console()

# def hole():
#     return Panel(
#         "",
#         width=9,
#         height=3,
#         box=box.ROUNDED,
#         style="bold #A52A2A",  # brown color in hex
#     )

# def mole():
#     return Panel(
#         ":hamster:",
#         width=9,
#         height=3,
#         box=box.ROUNDED,
#         style="bold red on white",
#     )

# Create a centered grid
# grid = Table.grid(padding=(1, 4), expand=True)  # expand lets it stretch
# grid.add_row(hole(), hole(), hole())
# grid.add_row(mole(), hole(), mole())
# grid.add_row(hole(), mole(), hole())

# Wrap the grid inside a centered panel
# game_panel = Panel(
#     grid,
#     title="Whack-a-Mole",
#     box=box.DOUBLE,
#     style="on #FFFDD0",
#     width=70,
#     height=20,
# )

# console.print(game_panel, justify="center")  # center in terminal

import random, time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


def random_mole_position():
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    return row, col


def hole():
    return Panel("", width=9, height=3, box=box.ROUNDED, style="bold #A52A2A")

def mole():
    return Panel(":hamster:", width=9, height=3, box=box.ROUNDED, style="bold red on white")


def make_grid(r, c):
    grid = Table.grid(padding=(1, 4), expand=True)
    for i in range(3):
        row = []
        for j in range(3):
            if i == r and j == c:
                row.append(mole())
            else:
                row.append(hole())
        grid.add_row(*row)
    return grid

#Test random mole positions
print("\nTesting mole randomizer...")
for i in range(8):
    pos = random_mole_position()
    print("Test", i+1, ": Mole appeared at", pos)

#Display grid with random mole positions
for i in range(8):
    r, c = random_mole_position()
    console.clear()
    panel = Panel(make_grid(r, c), title="Round " + str(i+1), box=box.DOUBLE, style="on #FFFDD0")
    console.print(panel, justify="center")
    time.sleep(1)