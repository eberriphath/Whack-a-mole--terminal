def game_loop():
    while True:
        console.print("\n[bold green]Menu: [S]tart  [P]ause  [C]ontinue  [E]nd[/]")
        choice = input(">> ").strip().lower()

        if choice == "s":  # Start game
            console.print("[yellow]Game started![/]")
            show_grid()  # display your grid
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