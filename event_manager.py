from pynput import keyboard, mouse
from display_character import Character


def manage(character: Character):
    # when a key is pressed
    def k_on_press(key):
        # check if an alphanumeric key is pressed
        try:
            # alphanumeric key has .char object
            key.char

            # keyboard events given key pressed
            if key.char == 'q':
                character.keyboard_press(46, 38)
            if key.char == 'w':
                character.keyboard_press(36, 38)
            if key.char == 'e':
                character.keyboard_press(26, 38)
            if key.char == 'r':
                character.keyboard_press(16, 38)
            if key.char == 't':
                character.keyboard_press(6, 38)
            if key.char == 'y':
                character.keyboard_press(-4, 38)
            if key.char == 'u':
                character.keyboard_press(-14, 38)
            if key.char == 'i':
                character.keyboard_press(-24, 38)
            if key.char == 'o':
                character.keyboard_press(-34, 38)
            if key.char == 'p':
                character.keyboard_press(-44, 38)
            if key.char == 'a':
                character.keyboard_press(42, 31)
            if key.char == 's':
                character.keyboard_press(32, 31)
            if key.char == 'd':
                character.keyboard_press(22, 31)
            if key.char == 'f':
                character.keyboard_press(12, 31)
            if key.char == 'g':
                character.keyboard_press(2, 31)
            if key.char == 'h':
                character.keyboard_press(-8, 31)
            if key.char == 'j':
                character.keyboard_press(-18, 31)
            if key.char == 'k':
                character.keyboard_press(-28, 31)
            if key.char == 'l':
                character.keyboard_press(-38, 31)
            if key.char == 'z':
                character.keyboard_press(38, 23)
            if key.char == 'x':
                character.keyboard_press(28, 23)
            if key.char == 'c':
                character.keyboard_press(18, 23)
            if key.char == 'v':
                character.keyboard_press(8, 23)
            if key.char == 'b':
                character.keyboard_press(-2, 23)
            if key.char == 'n':
                character.keyboard_press(-12, 23)
            if key.char == 'm':
                character.keyboard_press(-22, 23)
            if key.char == '1':
                character.keyboard_press(50, 45)
            if key.char == '2':
                character.keyboard_press(40, 45)
            if key.char == '3':
                character.keyboard_press(30, 45)
            if key.char == '4':
                character.keyboard_press(20, 45)
            if key.char == '5':
                character.keyboard_press(10, 45)
            if key.char == '6':
                character.keyboard_press(0, 45)
            if key.char == '7':
                character.keyboard_press(-10, 45)
            if key.char == '8':
                character.keyboard_press(-20, 45)
            if key.char == '9':
                character.keyboard_press(-30, 45)
            if key.char == '0':
                character.keyboard_press(-40, 45)

        # handles non-alphanumeric key presses
        except AttributeError:
            # keyboard events given key pressed
            if str(key) == "Key.space":
                character.keyboard_press(0, 15)

    # when a key is released
    def k_on_release(key):
        # reset the position of the hand
        character.reset_r_hand()

    # when the mouse is moved
    def m_on_move(x, y):
        # move the virtual mouse as well
        character.get_motion(x, y)

    # when the mouse is clicked
    def m_on_click(x, y, button, pressed):
        # if the button is pressed down
        if pressed:
            # various mouse buttons
            if str(button) == "Button.right":
                character.click_mouse(-30, 20)
            if str(button) == "Button.middle":
                character.click_mouse(-20, 20)
            if str(button) == "Button.left":
                character.click_mouse(-10, 20)

        # otherwise, release it
        else:
            character.reset_l_hand()

    # create a keyboard listener
    k_listener = keyboard.Listener(
        on_press=k_on_press,
        on_release=k_on_release)

    # deploy keyboard listener
    k_listener.start()

    # create a mouse listener
    m_listener = mouse.Listener(
        on_move=m_on_move,
        on_click=m_on_click)

    # deploy mouse listener
    m_listener.start()
