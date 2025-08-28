import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()
GRID_SIZE = 3

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

def draw_grid(mole_pos):
    grid = Table.grid(padding=(1, 4), expand=True)
    for row in range(GRID_SIZE):
        row_cells = []
        for col in range(GRID_SIZE):
            if (row, col) == mole_pos:
                row_cells.append(mole())
            else:
                row_cells.append(hole())
        grid.add_row(*row_cells)

    game_panel = Panel(
        grid,
        title="Whack-a-Mole",
        box=box.DOUBLE,
        style="on #FFFDD0",
        width=70,
        height=20,
    )
    console.print(game_panel, justify="center")

def random_mole_position():
    return (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

def main():
    running = False
    game_over = False
    console.print("Commands: [bold green]start[/], [bold yellow]pause[/], [bold cyan]resume[/], [bold red]end[/]", style="bold")

    mole_pos = random_mole_position()

    while not game_over:
        if running:
            console.clear()  # clear previous grid
            draw_grid(mole_pos)
            time.sleep(1)  # wait 1 second

            mole_pos = random_mole_position()  # mole changes position each second

        # Check for commands
        if not running:
            cmd = input("> ").strip().lower()
            if cmd == "start" or cmd == "resume":
                running = True
            elif cmd == "pause":
                running = False
                console.print("[yellow]Game paused.[/yellow]")
            elif cmd == "end":
                game_over = True
                console.print("[bold red]Game Over! Thanks for playing 🐹[/bold red]")
            else:
                console.print("[red]Unknown command. Use start, pause, resume, or end.[/red]")

if __name__ == "__main__":
    main()


