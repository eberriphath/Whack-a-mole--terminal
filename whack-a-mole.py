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
        style="bold #A52A2A"  # brown color in hex
    )


def mole():
    return Panel(
        "🐹", 
        width=9, 
        height=3, 
        box=box.ROUNDED, 
        style="bold red on white"
    )

grid = Table.grid(padding=(1, 4)) 
grid.add_row(hole(), hole(), hole())
grid.add_row(mole(), hole(), mole())
grid.add_row(hole(), mole(), hole())




game_panel = Panel(
    
    grid,
    title="Whack-a-Mole",
    box=box.DOUBLE,
    style="on #FFFDD0",
    width=70,
    height=30
)

console.print(game_panel)
