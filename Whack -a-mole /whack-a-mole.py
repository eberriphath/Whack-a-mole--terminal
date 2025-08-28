from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.live import Live
import random, time

console = Console()


def hole():
    return Panel("", width=9, height=3, box=box.ROUNDED, style="bold #A52A2A")

def mole():
    return Panel("🐹", width=9, height=3, box=box.ROUNDED, style="bold red on white")


def make_grid(mole_pos):
    grid = Table.grid(padding=(1, 4), expand=True)
    cells = []
    for i in range(9):
        if i == mole_pos:
            cells.append(mole())
        else:
            cells.append(hole())
    grid.add_row(cells[0], cells[1], cells[2])
    grid.add_row(cells[3], cells[4], cells[5])
    grid.add_row(cells[6], cells[7], cells[8])
    return grid

def show_grid(mole_pos=None, delay=1):
 
    with Live(console=console, refresh_per_second=4, screen=False) as live:
        if mole_pos is None:  
            mole_pos = random.randint(0, 8)
        game_panel = Panel(
            make_grid(mole_pos),
            title="Whack-a-Mole",
            box=box.DOUBLE,
            style="on #FFFDD0",
            width=70,
            height=20,
        )
        live.update(game_panel)
        time.sleep(delay)
    return mole_pos

def update_score(score, hit):
    if hit:
        return score + 1
    else:
        return score



def play_round(score):
    mole_pos = random.randint(0, 8)
    show_grid(mole_pos)

    move = input("Enter row col: ")
    try:
        row, col = map(int, move.split())
        row -= 1
        col -= 1
        chosen_pos = row * 3 + col
    except:
        
        return update_score(score, False)

    hit = chosen_pos == mole_pos
    if hit:
        console.print(" +1")
    else:
        console.print(" 0")
    return update_score(score, hit)


def game_loop():
    score = 0
    game_time = 40  
    console.print(f"[yellow]You have {game_time} seconds to play![/]")
    start_time = time.time()

    while True:
        
        if time.time() - start_time >= game_time:
            console.print(f"[red]Final Score: {score}[/]")
            break

        console.print("\n[bold green]Menu: [S]tart ")
        choice = input("==> ").strip().lower()

        if choice == "s": 
            console.print("[yellow]Game started![/]")
            score = play_round(score)
            console.print(f"[cyan]Score: {score}[/]")

        else:
            console.print("[red]Invalid choice, try again![/]")
            time.sleep(1)

if __name__ == "__main__":
    game_loop()
