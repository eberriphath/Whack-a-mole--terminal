from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
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

def update_score(score, hit):
    if hit:
        return score + 1
    else:
        return score - 1

def play_game(duration=20):
    """Play game for given duration (seconds)"""
    score = 0
    start_time = time.time()

    while time.time() - start_time < duration:
        mole_pos = random.randint(0, 8)

        # Clear screen and show new mole
        console.clear()
        console.print(Panel(make_grid(mole_pos), title="Whack-a-Mole", style="on #FFFDD0"))

        move = input("Whack the mole! Enter row col (1-3 1-3): ")
        move = move.replace("-", " ").replace(",", " ")
        try:
            row, col = map(int, move.split())
            row -= 1
            col -= 1
            chosen_pos = row * 3 + col
        except:
            console.print("[red]Bad input, you missed![/]")
            score = update_score(score, False)
            continue

        hit = chosen_pos == mole_pos
        if hit:
            console.print("[green]Hit! +1[/]")
        else:
            console.print("[red]Miss! -1[/]")
        score = update_score(score, hit)

        console.print(f"[cyan]Score: {score}[/]")
        time.sleep(0.5)  # short delay before next mole

    console.print(f"\n[bold red]Time's up! Final Score: {score}[/]")

if __name__ == "__main__":
    console.print("[yellow]Welcome to Whack-a-Mole![/]")
    play_game(duration=20)  # play for 20 seconds
