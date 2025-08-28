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

import random, time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

#Random mole position
def random_mole_position():
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    return row, col

#Hole and mole
def hole():
    return Panel("", width=9, height=3, box=box.ROUNDED, style="bold #A52A2A")

def mole():
    return Panel(":hamster:", width=9, height=3, box=box.ROUNDED, style="bold red on white")

#Make grid
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

    # Convert (row, col) to hole number 1–9
def pos_to_num(row, col):
    return row * 3 + col + 1   # (0,0)->1 , (0,1)->2 ... (2,2)->9

score = 0

for i in range(8):
    r, c = random_mole_position()
    mole_pos = pos_to_num(r, c)   # store mole's hole number (1–9)

    console.clear()
    panel = Panel(make_grid(r, c), box=box.DOUBLE, style="on #FFFDD0")
    console.print(panel, justify="center")

    # Ask player to whack
    choice = input("Whack a hole number (1–9): ").strip()

    if choice.isdigit():
        if int(choice) == mole_pos:
            score += 1
            console.print(f"[yellow]Hit! Score: {score}[/]")
        else:
            console.print(f"[blue]Miss! Mole was at {mole_pos}. Score: {score}[/]")
    else:
        console.print("[red]Invalid input! Enter a number 1–9.[/]")

    time.sleep(1.5)