from tkinter import Tk
from event_manager import *


if __name__ == "__main__":
    # create our window titled "Wolfy"
    display = Tk()
    display.title("Wolfy")

    # sets all white colored items to clear (no white color allowed on any sprites)
    display.attributes('-transparentcolor', '#00ff00')

    # create our character
    character = Character(display)

    # manage mouse and keyboard events
    manage(character)

    # display the character
    display.mainloop()
