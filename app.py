from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Managment:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x750+0+0')
        self.root.title('EXPENSE SYSTEM MANAGMENT')

        label_title = Label(self.root, text='EXPENSE SYSTEM MANAGMENT', font=(
            'modern', 40, 'bold'), bg='black', fg='white')
        label_title.place(x=0, y=0, width=1300, height=70)


if __name__ == '__main__':
    root = Tk()
    obj = Managment(root)
    root.mainloop()
