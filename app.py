# import library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# create class Managment


class Managment:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x750+0+0')
        self.root.title('EXPENSE SYSTEM MANAGMENT')

        # create window
        label_title = Label(self.root, text='EXPENSE SYSTEM MANAGMENT', font=(
            'modern', 40, 'bold'), bg='black', fg='white')
        label_title.place(x=0, y=0, width=1300, height=70)

        # Main frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=200, width=1250, height=400)

        # Upper frame
        upper_frame = LabelFrame(
            Main_frame, bd=2, relief=RIDGE, text="bla bla bla")
        upper_frame.place(x=10, y=10, width=1220, height=160)
        # Down frame
        down_frame = LabelFrame(
            Main_frame, bd=2, relief=RIDGE, text="bla bla bla")
        down_frame.place(x=10, y=200, width=1220, height=160)

        # Search frame
        search_frame = LabelFrame(
            down_frame, bd=2, relief=RIDGE, text='Search', bg='white')
        search_frame.place(x=10, y=0, width=1200, height=50)

        # 1 label
        label_1 = Label(upper_frame, text="label1", font=(
            'modern', 11, 'bold'), bg='white')
        label_1.grid(row=0, column=0, padx=2, sticky=W)

        label_1_entry = ttk.Entry(upper_frame, width=22, font=(
            'modern', 11, 'bold'))
        label_1_entry.grid(row=0, column=1, padx=2, sticky=W)

        # label no2
        label_2 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 2:", bg='white')
        label_2.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        label_2_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 12, 'bold'))
        label_2_entry.grid(row=0, column=3, padx=2, pady=7)


if __name__ == '__main__':
    root = Tk()
    obj = Managment(root)
    root.mainloop()
