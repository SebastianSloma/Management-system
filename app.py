from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Managment:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x750+0+0')
        self.root.title('SYSTEM MANAGMENT')


if __name__ == '__main__':
    root = Tk()
    obj = Managment(root)
    root.mainloop()
