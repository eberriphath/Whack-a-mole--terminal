from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.live import Live
import random, time

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

# --- NEW: function that runs one round of the game
def show_grid(rounds=10, delay=1.5):
    with Live(console=console, refresh_per_second=4, screen=False) as live:
        for _ in range(rounds):  # number of mole moves
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

# Menu loop
def game_loop():
    while True:
        console.print("\n[bold green]Menu: [S]tart  [P]ause  [C]ontinue  [E]nd[/]")
        choice = input(">> ").strip().lower()

        if choice == "s":  # Start game
            console.print("[yellow]Game started![/]")
            show_grid()
        elif choice == "c":  # Continue
            console.print("[cyan]Game continues...[/]")
            show_grid()
        elif choice == "p":  # Pause
            console.print("[blue]Game paused. Press Enter to resume.[/]")
            input()
        elif choice == "e":  # End
            console.print("[red]Game Over! Exiting...[/]")
            break
        else:
            console.print("[red]Invalid choice, try again![/]")
            time.sleep(1)

if __name__ == "__main__":
    game_loop()



	
# Mohamed Amin Abdiwahid
# 3:10 PM






def update_score(score, hit):
    if hit:
        return score + 1
    else:
        return score - 1


def play_round(score):
    mole_pos = random_mole_position()
    show_grid(mole_pos)

move = input("Whack the mole! Enter row col (1-3 1-3, e.g., 2 3): ")
move = move.replace("-", " ").replace(",", " ")  # flexible input

try:
    row, col = map(int, move.split())
    row -= 1
    col -= 1
except:
    print("Bad input, you missed!\n")
  

hit = (row, col) == mole_pos
if hit:
    print("Hit! +1\n")
else:
    print("Miss! -1\n")



def game_loop():
    score = 0
    total_time = 30  # total game time in seconds
    start_time = time.time()

print("Welcome to Whack-a-Mole!")
print(f"You have {total_time} seconds to hit as many moles as possible!\n")

while time.time() - start_time < total_time:
    remaining = int(total_time - (time.time() - start_time))
    print(f"Time left: {remaining} seconds")
    score = play_round(score)
    print("Current Score:", score, "\n")

print("Time's up! Final Score:", score)

if name == "main":
    game_loop()
