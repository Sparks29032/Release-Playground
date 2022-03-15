from tkinter import Canvas, PhotoImage, NW


class Character:
    def __init__(self, d):
        # get dimensions of screen
        self.s_width = d.winfo_screenwidth()
        self.s_height = d.winfo_screenheight()

        # the dimensions of the base image
        self.base = PhotoImage(file="Images/Base.png")
        w = self.base.width()
        h = self.base.height()

        # use the dimensions of the base image to create the canvas
        self.canvas = Canvas(d, bg='#00ff00', width=w, height=h)
        self.canvas.pack()

        # buffer actions
        self.l_buffer = False
        self.r_buffer = False

        # define the mouse
        self.mouse = PhotoImage(file="Images/Mouse.png")

        # base location of mouse on canvas
        self.mouse_w = 75
        self.mouse_h = 350

        # max pixels mouse can move in any direction
        self.mouse_b = 25

        # define the left hand
        self.l_hand = PhotoImage(file="Images/Left_Hand.png")

        # location of left hand relative to the mouse
        self.l_hand_w = 20
        self.l_hand_h = -10

        # define the keyboard
        self.keyboard = PhotoImage(file="Images/Keyboard.png")

        # location of keyboard
        self.keyboard_w = 200
        self.keyboard_h = 350

        # define the right hand
        self.r_hand = PhotoImage(file="Images/Right_Hand.png")

        # location of right hand relative to the keyboard
        self.r_hand_w = 75
        self.r_hand_h = -20

        # draw the base image
        self.draw_base()

        # holds the current position of the mouse
        self.curr_x = self.mouse_w
        self.curr_y = self.mouse_h

        # define the canvas objects
        self.c_mouse = None
        self.c_l_hand = None
        self.c_keyboard = None
        self.c_r_hand = None

        # draw the mouse and left hand
        self.draw_mouse()

        # draw the keyboard and right hand
        self.draw_keyboard()

    # draws teh base image
    def draw_base(self):
        self.canvas.create_image(0, 0, anchor=NW, image=self.base)

    # draws the mouse and left hand
    def draw_mouse(self):
        self.c_mouse = self.canvas.create_image(self.mouse_w, self.mouse_h, anchor=NW, image=self.mouse)
        self.c_l_hand = self.canvas.create_image(self.mouse_w + self.l_hand_w,
                                                 self.mouse_h + self.l_hand_h,
                                                 anchor=NW, image=self.l_hand)

    # draws the keyboard
    def draw_keyboard(self):
        self.c_keyboard = self.canvas.create_image(self.keyboard_w, self.keyboard_h, anchor=NW, image=self.keyboard)
        self.c_r_hand = self.canvas.create_image(self.keyboard_w + self.r_hand_w,
                                                 self.keyboard_h + self.r_hand_h,
                                                 anchor=NW, image=self.r_hand)

    # moves the mouse to desired location
    def get_motion(self, x, y):

        # convert the x, y into location on canvas
        conv_x = (x - (self.s_width / 2)) / self.mouse_b
        conv_y = (y - (self.s_height / 2)) / self.mouse_b

        # move the mouse using helper function
        self.position_mouse(int(conv_x), int(conv_y))

    # moves the mouse to a new desired location
    def position_mouse(self, c_x, c_y):
        # move the hand and mouse
        self.canvas.move(self.c_mouse,
                         c_x + self.mouse_w - self.curr_x,
                         c_y + self.mouse_h - self.curr_y)
        self.canvas.move(self.c_l_hand,
                         c_x + self.mouse_w - self.curr_x,
                         c_y + self.mouse_h - self.curr_y)

        # identify new current position
        self.curr_x = c_x + self.mouse_w
        self.curr_y = c_y + self.mouse_h

    # shows a mouse clicking animation
    def click_mouse(self, c_x, c_y):
        # check if other actions in place
        if self.l_buffer:
            return

        # prevent other actions on the left side
        self.l_buffer = True

        # do the clicking animation
        self.canvas.move(self.c_l_hand, c_x, c_y)

    # put the left hand back to where it started on the mouse
    def reset_l_hand(self):
        self.canvas.delete(self.c_l_hand)
        self.c_l_hand = self.canvas.create_image(self.curr_x + self.l_hand_w,
                                                 self.curr_y + self.l_hand_h,
                                                 anchor=NW, image=self.l_hand)

        # allow other actions on the left side
        self.l_buffer = False

    # shows a keyboard-button pressing animation
    def keyboard_press(self, c_x, c_y):
        # check if other actions in place
        if self.r_buffer:
            self.reset_r_hand()

        # prevent other actions on the right side
        self.r_buffer = True

        # do the pressing animation
        self.canvas.move(self.c_r_hand, c_x, c_y)

    # put the right hand back to where it started relative to the keyboard
    def reset_r_hand(self):
        self.canvas.delete(self.c_r_hand)
        self.c_r_hand = self.canvas.create_image(self.keyboard_w + self.r_hand_w,
                                                 self.keyboard_h + self.r_hand_h,
                                                 anchor=NW, image=self.r_hand)

        # allow other actions on the right side
        self.r_buffer = False
