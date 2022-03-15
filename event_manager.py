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
                character.keyboard_press(48, 38)
            if key.char == 'w':
                character.keyboard_press(43, 38)
            if key.char == 'e':
                character.keyboard_press(38, 38)
            if key.char == 'r':
                character.keyboard_press(33, 38)
            if key.char == 'g':
                character.keyboard_press(26, 31)
            if key.char == 'z':
                character.keyboard_press(44, 23)
            if key.char == 'x':
                character.keyboard_press(39, 23)
            if key.char == '1':
                character.keyboard_press(50, 45)
            if key.char == '2':
                character.keyboard_press(45, 45)
            if key.char == '3':
                character.keyboard_press(40, 45)
            if key.char == '4':
                character.keyboard_press(35, 45)

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
            if str(button) == "Button.left":
                character.click_mouse(-30, 20)
            if str(button) == "Button.middle":
                character.click_mouse(-20, 20)
            if str(button) == "Button.right":
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
