import os


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
