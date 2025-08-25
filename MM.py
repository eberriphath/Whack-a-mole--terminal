from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.align import Align
from rich.text import Text

console = Console()

holes = """
   🕳️     🕳️     🕳️

   🐹     🕳️     🐹

   🕳️     🐹     🕳️
"""

# Make it a Rich Text renderable
holes_text = Text(holes)

# Center horizontally & vertically
aligned_holes = Align.center(holes_text, vertical="middle")

# Put inside a panel
panel = Panel(
    aligned_holes,
    title="Whack-a-Mole",
    style="on #FFFDD0",  # cream background
    box=box.SQUARE,
    width=150,
    height=50
)

console.print(panel)