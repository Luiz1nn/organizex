import time
from art import text2art
from animate_text.clear_screen import clear_screen


def animate_text():
    """
    Displays an animated ASCII art of the text "organizex" in the terminal.

    The animation gradually "types" the ASCII art of the text "organizex" on the screen,
    using a custom green color (RGB: #16C64F), and clears the screen after each character
    is displayed to create a typing effect.

    The function uses the `art` library to generate the ASCII art and `animate_text.clear_screen`
    to clear the screen at each animation step.

    The animation is displayed character by character, 
    with a brief time interval between each display.
    """

    ascii_art = text2art("organizex")

    custom_green = "\033[38;2;22;198;79m"

    for i in range(1, len(ascii_art)+1):
        clear_screen()
        print(custom_green + ascii_art[:i])
        time.sleep(0.001)
