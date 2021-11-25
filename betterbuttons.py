# Necessary imports.
import tkinter
from tkinter import Canvas, Button, PhotoImage
import os


# Creating The "Program" Class.
class Program:
    # Main Function.
    def __init__(self, root):
        # Function for make him red. (RED)
        def red_anim_on(event):
            self.red_button_anim.config(image=self.img_red_button_selec)

        # Function to return to default. (RED)
        def red_anim_off(event):
            self.red_button_anim.config(image=self.img_red_button)

        # Function for make him green. (GREEN)
        def green_anim_on(event):
            self.green_button_anim.config(image=self.img_green_button_selec)

        # Function to return to default. (GREEN)
        def green_anim_off(event):
            self.green_button_anim.config(image=self.img_green_button)

        # Function for make him blue. (BLUE)
        def blue_anim_on(event):
            self.blue_button_anim.config(image=self.img_blue_button_selec)

        # Function to return to default. (BLUE)
        def blue_anim_off(event):
            self.blue_button_anim.config(image=self.img_blue_button)

        # Path of the images.
        self.dirname = os.path.dirname(os.path.abspath(__file__))

        # Red Button.
        self.img_red_button = PhotoImage(
            file=f'{self.dirname}/images/red-button.png')
        self.red_button = Button(root,
                                 highlightcolor='#FF0000',
                                 borderwidth=0,
                                 bg='#191919',
                                 activebackground='#191919',
                                 relief='flat',
                                 image=self.img_red_button,
                                 command=lambda: print('Red Button'))
        self.red_button.place(x=90.5, y=76)

        # Red button animated.
        self.red_button_anim = Button(root,
                                      highlightcolor='#FF0000',
                                      borderwidth=0,
                                      bg='#191919',
                                      activebackground='#191919',
                                      relief='flat',
                                      image=self.img_red_button,
                                      command=lambda: print('Red Button Animated'))
        self.red_button_anim.place(x=240.5, y=76)
        self.red_button_anim.bind('<Enter>', red_anim_on)
        self.red_button_anim.bind('<Leave>', red_anim_off)

        # Red button selected.
        self.img_red_button_selec = PhotoImage(
            file=f'{self.dirname}/images/red-button-selec.png')
        self.red_button_selec = Button(root,
                                       highlightcolor='#FF0000',
                                       borderwidth=0,
                                       bg='#191919',
                                       activebackground='#191919',
                                       relief='flat',
                                       image=self.img_red_button_selec,
                                       command=lambda: print('Red Button Selected'))
        self.red_button_selec.place(x=390.5, y=76)

        # Green button.
        self.img_green_button = PhotoImage(
            file=f'{self.dirname}/images/green-button.png')
        self.green_button = Button(root,
                                   highlightcolor='#FF0000',
                                   borderwidth=0,
                                   bg='#191919',
                                   activebackground='#191919',
                                   relief='flat',
                                   image=self.img_green_button,
                                   command=lambda: print('Green Button'))
        self.green_button.place(x=90.5, y=176)

        # Green button animated.
        self.green_button_anim = Button(root,
                                        highlightcolor='#FF0000',
                                        borderwidth=0,
                                        bg='#191919',
                                        activebackground='#191919',
                                        relief='flat',
                                        image=self.img_green_button,
                                        command=lambda: print('Green Button Animated'))
        self.green_button_anim.place(x=240.5, y=176)
        self.green_button_anim.bind('<Enter>', green_anim_on)
        self.green_button_anim.bind('<Leave>', green_anim_off)

        # Green button selected.
        self.img_green_button_selec = PhotoImage(
            file=f'{self.dirname}/images/green-button-selec.png')
        self.green_button_selec = Button(root,
                                            highlightcolor='#FF0000',
                                            borderwidth=0,
                                            bg='#191919',
                                            activebackground='#191919',
                                            relief='flat',
                                            image=self.img_green_button_selec,
                                            command=lambda: print('Green Button Selected'))
        self.green_button_selec.place(x=390.5, y=176)

        # Blue button.
        self.img_blue_button = PhotoImage(
            file=f'{self.dirname}/images/blue-button.png')
        self.blue_button = Button(root,
                                  highlightcolor='#FF0000',
                                  borderwidth=0,
                                  bg='#191919',
                                  activebackground='#191919',
                                  relief='flat',
                                  image=self.img_blue_button,
                                  command=lambda: print('Blue Button'))
        self.blue_button.place(x=90.5, y=276)

        # Blue button animated.
        self.blue_button_anim = Button(root,
                                       highlightcolor='#FF0000',
                                       borderwidth=0,
                                       bg='#191919',
                                       activebackground='#191919',
                                       relief='flat',
                                       image=self.img_blue_button,
                                       command=lambda: print('Blue Button Animated'))
        self.blue_button_anim.place(x=240.5, y=276)
        self.blue_button_anim.bind('<Enter>', blue_anim_on)
        self.blue_button_anim.bind('<Leave>', blue_anim_off)

        # Blue button selected.
        self.img_blue_button_selec = PhotoImage(
            file=f'{self.dirname}/images/blue-button-selec.png')
        self.blue_button_selec = Button(root,
                                        highlightcolor='#FF0000',
                                        borderwidth=0,
                                        bg='#191919',
                                        activebackground='#191919',
                                        relief='flat',
                                        image=self.img_blue_button_selec,
                                        command=lambda: print('Blue Button Selected'))
        self.blue_button_selec.place(x=390.5, y=276)


# For start Tkinter.
root = tkinter.Tk()

# Title of the window.
root.title('Buttons')

# Make it impossible to change the screen size.
root.resizable(width=False, height=False)

# Program window.
canvas = Canvas(root, width=600,
                height=400,
                bg='#191919',
                relief='flat')
canvas.pack()

# Function to run only the main program.
if __name__ == '__main__':
    App = Program(root)
    root.mainloop()
