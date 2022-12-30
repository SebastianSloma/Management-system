# import library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


# create class Managment


class Managment:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x750')
        self.root.title('EXPENSE SYSTEM MANAGMENT')

        # variables
        self.var_label_1 = StringVar()
        self.var_label_2 = StringVar()
        self.var_label_3 = StringVar()
        self.var_label_4 = StringVar()
        self.var_label_5 = StringVar()
        self.var_label_6 = StringVar()
        self.var_label_7 = StringVar()
        self.var_label_8 = StringVar()
        self.var_label_9 = StringVar()
        self.var_label_10 = StringVar()
        self.var_label_11 = StringVar()
        self.var_label_12 = StringVar()
        self.var_label_13 = StringVar()
        self.var_label_14 = StringVar()

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
        search_frame.place(x=10, y=0, width=1200, height=60)

        # search label
        search_label = Label(search_frame, font=(
            'modern', 11, 'bold'), text='Search', bg='red', fg='white')
        search_label.grid(row=0, column=0, sticky=W, padx=5)

        # combo box
        search_box = ttk.Combobox(search_frame, font=(
            'modern', 11, 'bold'), width=18, state='readonly')
        search_box['value'] = ('Select option', 'bla', 'bla', 'bla')
        search_box.current(0)
        search_box.grid(row=0, column=1, sticky=W, padx=5)

        search_text = ttk.Entry(search_frame, width=22, font=(
            "modern", 11, 'bold'))
        search_text.grid(row=0, column=2, padx=2, pady=7)

        # 1 label
        label_1 = Label(upper_frame, text="label1", font=(
            'modern', 11, 'bold'), bg='white')
        label_1.grid(row=0, column=0, padx=2, sticky=W)

        label_1_entry = ttk.Entry(upper_frame, textvariable=self.var_label_1, width=22, font=(
            'modern', 11, 'bold'))
        label_1_entry.grid(row=0, column=1, padx=2, sticky=W)

        # label no2
        label_2 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 2:", bg='white')
        label_2.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        label_2_entry = ttk.Entry(upper_frame, textvariable=self.var_label_2, width=22, font=(
            "modern", 11, 'bold'))
        label_2_entry.grid(row=0, column=3, padx=2, pady=7)

        # label no3
        label_3 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 3:", bg='white')
        label_3.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        label_3_entry = ttk.Entry(upper_frame, textvariable=self.var_label_3, width=22, font=(
            "modern", 11, 'bold'))
        label_3_entry.grid(row=1, column=1, padx=2, pady=7)

        # label no4
        label_4 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 4:", bg='white')
        label_4.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        label_4_entry = ttk.Entry(upper_frame, textvariable=self.var_label_4, width=22, font=(
            "modern", 11, 'bold'))
        label_4_entry.grid(row=1, column=3, padx=2, pady=7)

        # label no5
        label_5 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 5:", bg='white')
        label_5.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        label_5_entry = ttk.Entry(upper_frame, textvariable=self.var_label_5, width=22, font=(
            "modern", 11, 'bold'))
        label_5_entry.grid(row=2, column=1, padx=2, pady=7)

        # label no6
        label_6 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 6:", bg='white')
        label_6.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        label_6_entry = ttk.Entry(upper_frame, textvariable=self.var_label_6, width=22, font=(
            "modern", 11, 'bold'))
        label_6_entry.grid(row=2, column=3, padx=2, pady=7)

        # label no7
        label_7 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 7:", bg='white')
        label_7.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        label_7_entry = ttk.Entry(upper_frame, textvariable=self.var_label_7, width=22, font=(
            "modern", 11, 'bold'))
        label_7_entry.grid(row=3, column=1, padx=2, pady=7)

        # label no8
        label_8 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 8:", bg='white')
        label_8.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        label_8_entry = ttk.Entry(upper_frame, textvariable=self.var_label_8, width=22, font=(
            "modern", 11, 'bold'))
        label_8_entry.grid(row=3, column=3, padx=2, pady=7)

        # label no9
        label_9 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 9:", bg='white')
        label_9.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        label_9_entry = ttk.Entry(upper_frame, textvariable=self.var_label_9, width=22, font=(
            "modern", 11, 'bold'))
        label_9_entry.grid(row=4, column=1, padx=2, pady=7)

        # label no10
        label_10 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 10:", bg='white')
        label_10.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        label_10_entry = ttk.Entry(upper_frame, textvariable=self.var_label_10, width=22, font=(
            "modern", 11, 'bold'))
        label_10_entry.grid(row=4, column=3, padx=2, pady=7)

        # label no11
        label_11 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 11:", bg='white')
        label_11.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        label_11_entry = ttk.Entry(upper_frame, textvariable=self.var_label_11, width=22, font=(
            "modern", 11, 'bold'))
        label_11_entry.grid(row=0, column=5, padx=2, pady=7)

        # label no12
        label_12 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 12:", bg='white')
        label_12.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        label_12_entry = ttk.Entry(upper_frame, textvariable=self.var_label_12, width=22, font=(
            "modern", 11, 'bold'))
        label_12_entry.grid(row=1, column=5, padx=2, pady=7)

        # radio button
        radio_button1 = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_button1.place(x=520, y=90, width=190, height=30)

        # label no13 radio frame
        label_13 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 13:", bg='white')
        label_13.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        first_choice = Radiobutton(radio_button1, variable=self.var_label_13, text='xxx', value='xxx', font=(
            'modern', 9, 'bold'), bg='white')
        first_choice.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        second_choice = Radiobutton(radio_button1, variable=self.var_label_13, text='yyy', value='yyy', font=(
            'modern', 9, 'bold'), bg='white')
        second_choice.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # label no14 radio frame
        label_14 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 14:", bg='white')
        label_14.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # label no14 radio frame
        label_14 = Label(upper_frame, font=(
            "modern", 12, 'bold'), text="label 14:", bg='white')
        label_14.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # radio button2
        radio_button2 = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_button2.place(x=520, y=130, width=190, height=30)

        third_choice = Radiobutton(radio_button2, variable=self.var_label_14, text='qqq', value='qqq', font=(
            'modern', 9, 'bold'), bg='white')
        third_choice.grid(row=0, column=0, pady=2, padx=5, sticky=W)

        forth_choice = Radiobutton(radio_button2, variable=self.var_label_14, text='sss', value='sss', font=(
            'modern', 9, 'bold'), bg='white')
        forth_choice.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Button
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)

        # add btn
        btn_add = Button(button_frame, command=self.add_data, text='Save Record', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        # update btn
        btn_update = Button(button_frame, text='Update', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        # delete btn
        btn_delete = Button(button_frame, text='Delete', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        # clear btn
        btn_clear = Button(button_frame, text='Clear', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        # background image right side
        img_background = Image.open('images/IMG.jpg')
        img_background = img_background.resize((470, 245), Image.LANCZOS)
        self.photo_background = ImageTk.PhotoImage(img_background)

        self.img_background = Label(upper_frame, image=self.photo_background)
        self.img_background.place(x=730, y=0, width=470, height=245)

        # search button
        btn_delete = Button(search_frame, text='Search', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=3, padx=3, pady=5)

        # all button
        btn_clear = Button(search_frame, text='Show all', font=(
            'modern', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=4, padx=3, pady=5)

        # Table
        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1200, height=100)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.expense_table = ttk.Treeview(
            table_frame, columns=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.expense_table.xview)
        scroll_y.config(command=self.expense_table.yview)

        self.expense_table.heading('1', text='bla')
        self.expense_table.heading('2', text='bla')
        self.expense_table.heading('3', text='bla')
        self.expense_table.heading('4', text='bla')
        self.expense_table.heading('5', text='bla')
        self.expense_table.heading('6', text='bla')
        self.expense_table.heading('7', text='bla')
        self.expense_table.heading('8', text='bla')
        self.expense_table.heading('9', text='bla')
        self.expense_table.heading('10', text='bla')
        self.expense_table.heading('11', text='bla')
        self.expense_table.heading('12', text='bla')
        self.expense_table.heading('13', text='bla')
        self.expense_table.heading('14', text='bla')

        self.expense_table['show'] = 'headings'

        self.expense_table.column('1', width=100)
        self.expense_table.column('2', width=100)
        self.expense_table.column('3', width=100)
        self.expense_table.column('4', width=100)
        self.expense_table.column('5', width=100)
        self.expense_table.column('6', width=100)
        self.expense_table.column('7', width=100)
        self.expense_table.column('8', width=100)
        self.expense_table.column('9', width=100)
        self.expense_table.column('10', width=100)
        self.expense_table.column('11', width=100)
        self.expense_table.column('12', width=100)
        self.expense_table.column('13', width=100)
        self.expense_table.column('14', width=100)

        self.expense_table.pack(fill=BOTH, expand=1)

        self.expense_table.bind('<ButtonRelease>', self.get_cursor)

        self.fetch_data()

    # Add data function
    def add_data(self):
        if self.var_label_1.get() == '':
            messagebox.showerror('Error', 'All Fields ae required')
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='root', database='expense_management')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into expense1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

                    self.var_label_1.get(),
                    self.var_label_2.get(),
                    self.var_label_3.get(),
                    self.var_label_4.get(),
                    self.var_label_5.get(),
                    self.var_label_6.get(),
                    self.var_label_7.get(),
                    self.var_label_8.get(),
                    self.var_label_9.get(),
                    self.var_label_10.get(),
                    self.var_label_11.get(),
                    self.var_label_12.get(),
                    self.var_label_13.get(),
                    self.var_label_14.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Expense record has been added')
            except Exception as es:
                messagebox.showerror('Error', f'Due To{str(es)}')

    # Fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='root', database='expense_management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from expense1')
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.expense_table.delete(*self.expense_table.get_children())
            for i in data:
                self.expense_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    # get cursor

    def get_cursor(self, event=''):
        cursor_row = self.expense_table.focus()
        content = self.expense_table.item(cursor_row)
        data = content['values']

        self.var_label_1.set(data[0])
        self.var_label_2.set(data[1])
        self.var_label_3.set(data[2])
        self.var_label_4.set(data[3])
        self.var_label_5.set(data[4])
        self.var_label_6.set(data[5])
        self.var_label_7.set(data[6])
        self.var_label_8.set(data[7])
        self.var_label_9.set(data[8])
        self.var_label_10.set(data[9])
        self.var_label_11.set(data[10])
        self.var_label_12.set(data[11])
        self.var_label_13.set(data[12])
        self.var_label_14.set(data[13])

    #  update function
    def update_data(self):
        if self.var_label_1.get() == '':
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Are you sure update this expense record?')
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='root', database='expense_management')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update expense1 set expense1col1=%s, expense1col2=%s, expense1col3=%s, expense1col4=%s, expense1col5=%s, expense1col6=%s, expense1col7=%s, expense1col8=%s, expense1col9=%s, expense1col10=%s, expense1col11=%s, expense1col12=%s, expense1col13=%s, expense1col14=%s'(
                        self.var_label_1.get(),
                        self.var_label_2.get(),
                        self.var_label_3.get(),
                        self.var_label_4.get(),
                        self.var_label_5.get(),
                        self.var_label_6.get(),
                        self.var_label_7.get(),
                        self.var_label_8.get(),
                        self.var_label_9.get(),
                        self.var_label_10.get(),
                        self.var_label_11.get(),
                        self.var_label_12.get(),
                        self.var_label_13.get(),
                        self.var_label_14.get()

                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Expense record successfully updeted')
            except Exception as es:
                messagebox.showerror('Error', f'Due To{str(es)}')


if __name__ == '__main__':
    root = Tk()
    obj = Managment(root)
    root.mainloop()
