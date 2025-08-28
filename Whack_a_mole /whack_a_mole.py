import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

# -------------------------
# Draw a hole
# -------------------------
def hole():
    return Panel(" O ", width=9, height=3, box=box.ROUNDED, style="bold #A52A2A")

# -------------------------
# Draw the mole
# -------------------------
def mole():
    return Panel(" M ", width=9, height=3, box=box.ROUNDED, style="bold red on white")

# -------------------------
# Show the 3x3 grid
# -------------------------
def show_grid(mole_pos):
    grid = Table.grid(padding=(1, 4), expand=True)
    for r in range(3):
        row_items = []
        for c in range(3):
            if (r, c) == mole_pos:
                row_items.append(mole())
            else:
                row_items.append(hole())
        grid.add_row(*row_items)

    game_panel = Panel(grid, title="Whack-a-Mole", box=box.DOUBLE, style="on #FFFDD0")
    console.print(game_panel, justify="center")

# -------------------------
# Random mole position
# -------------------------
def random_mole_position():
    return (random.randint(0, 2), random.randint(0, 2))

# -------------------------
# Update score
# -------------------------
def update_score(score, hit):
    if hit:
        return score + 1
    else:
        return score - 1

# -------------------------
# Play one round of the game
# -------------------------
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
        return score

    hit = (row, col) == mole_pos
    if hit:
        print("Hit! +1\n")
    else:
        print("Miss! -1\n")

    return update_score(score, hit)

# -------------------------
# Main game loop with timer
# -------------------------
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

# -------------------------
# Run the game
# -------------------------
if __name__ == "__main__":
    game_loop()
