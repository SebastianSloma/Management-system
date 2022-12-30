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
        Main_frame.place(x=10, y=80, width=1250, height=550)

        # Upper frame
        upper_frame = LabelFrame(
            Main_frame, bd=2, relief=RIDGE, text="bla bla bla")
        upper_frame.place(x=10, y=10, width=1220, height=280)
        # Down frame
        down_frame = LabelFrame(
            Main_frame, bd=2, relief=RIDGE, text="bla bla bla")
        down_frame.place(x=10, y=320, width=1220, height=200)

        # Search frame
        search_frame = LabelFrame(
            down_frame, bd=2, relief=RIDGE, text='Search', bg='white')
        search_frame.place(x=10, y=0, width=1200, height=50)

        # search label
        search_label = Label(search_frame, font=(
            'modern', 11, 'bold'), text='Search', bg='red', fg='white')
        search_label.grid(row=0, column=0, sticky=W, padx=5)

        search_box = ttk.Combobox(search_frame, font=('modern',11,'bold'),width=18, state='readonly')
        search_box['value'] = ('Select option', 'bla', 'bla', 'bla')
        search_box.current(0)
        search_box.grid(row=0, column=1, sticky=W, padx=5)

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
            "modern", 11, 'bold'))
        label_2_entry.grid(row=0, column=3, padx=2, pady=7)

        # label no3
        label_3 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 3:", bg='white')
        label_3.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        label_3_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_3_entry.grid(row=1, column=1, padx=2, pady=7)

        # label no4
        label_4 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 4:", bg='white')
        label_4.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        label_4_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_4_entry.grid(row=1, column=3, padx=2, pady=7)

        # label no5
        label_5 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 5:", bg='white')
        label_5.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        label_5_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_5_entry.grid(row=2, column=1, padx=2, pady=7)

        # label no6
        label_6 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 6:", bg='white')
        label_6.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        label_6_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_6_entry.grid(row=2, column=3, padx=2, pady=7)

        # label no7
        label_7 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 7:", bg='white')
        label_7.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        label_7_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_7_entry.grid(row=3, column=1, padx=2, pady=7)

        # label no8
        label_8 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 8:", bg='white')
        label_8.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        label_8_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_8_entry.grid(row=3, column=3, padx=2, pady=7)

        # label no9
        label_9 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 9:", bg='white')
        label_9.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        label_9_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_9_entry.grid(row=4, column=1, padx=2, pady=7)

        # label no10
        label_10 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 10:", bg='white')
        label_10.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        label_10_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_10_entry.grid(row=4, column=3, padx=2, pady=7)

        # label no11
        label_11 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 11:", bg='white')
        label_11.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        label_11_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_11_entry.grid(row=0, column=5, padx=2, pady=7)

        # label no12
        label_12 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 12:", bg='white')
        label_12.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        label_12_entry = ttk.Entry(upper_frame, width=22, font=(
            "modern", 11, 'bold'))
        label_12_entry.grid(row=1, column=5, padx=2, pady=7)

        # label no13
        label_13 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 13:", bg='white')
        label_13.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        # label no14
        label_14 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 14:", bg='white')
        label_14.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # radio button
        radio_button1 = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_button1.place(x=520, y=90, width=190, height=30)

        first_choice = Radiobutton(radio_button1, text='xxx', value='xxx', font=(
            'modern', 9, 'bold'), bg='white')
        first_choice.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        second_choice = Radiobutton(radio_button1, text='yyy', value='yyy', font=(
            'modern', 9, 'bold'), bg='white')
        second_choice.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # radio button2
        radio_button2 = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_button2.place(x=520, y=130, width=190, height=30)

        third_choice = Radiobutton(radio_button2, text='qqq', value='qqq', font=(
            'modern', 9, 'bold'), bg='white')
        third_choice.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        forth_choice = Radiobutton(radio_button2, text='sss', value='sss', font=(
            'modern', 9, 'bold'), bg='white')
        forth_choice.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Button
        radio_button3 = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_button3.place(x=5, y=200, width=620, height=45)

        # add btn
        btn_add = Button(radio_button3, text='Save Record', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        # update btn
        btn_update = Button(radio_button3, text='Update', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        # delete btn
        btn_delete = Button(radio_button3, text='Delete', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        # clear btn
        btn_clear = Button(radio_button3, text='Clear', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        # background image right side
        img_background = Image.open('images/IMG.jpg')
        img_background = img_background.resize((470, 245), Image.ANTIALIAS)
        self.photo_background = ImageTk.PhotoImage(img_background)

        self.img_background = Label(upper_frame, image=self.photo_background)
        self.img_background.place(x=730, y=0, width=470, height=245)


if __name__ == '__main__':
    root = Tk()
    obj = Managment(root)
    root.mainloop()
