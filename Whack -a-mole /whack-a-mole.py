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
