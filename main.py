from tkinter import *
from tkinter import Tk, ttk, messagebox
import sqlite3

BIG_FONT = ("Helvetica", 22, "bold")
SMALL_FONT = ("Helvetica", 12, "bold")
SUBSCRIPTION_TYPES = ("YEAR", "MONTH", "WEEK", "DAY")
AVAILABLE_SECTIONS = ("CrossFit", "Swimming", "Calisthenics", "Rock Climbing", "Boxing", "Wrestling")
BUTTON_WIDTH = 18
COLUMNS = ("Subscription Type", "First Name", "Last Name", "BirthDate", "Phone Number", "RegistrationDate", "Section")


class SportGym:
    def __init__(self, window):
        self.window = window
        self.window.title("Sport Gym Management System")
        self.window.geometry("1400x800+0+0")
        # data variables:
        self.subscription_type = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.birthdate = StringVar()
        self.phone = StringVar()
        self.register = StringVar()
        self.section = StringVar()

        title_label = Label(self.window, bd=20, relief=GROOVE, text="SPORT GYM MEMBERS MANAGEMENT SYSTEM",
                            fg="chocolate", bg="white", font=BIG_FONT)
        title_label.pack(side=TOP, fill=X)
        # Frames Section:
        main_frame = Frame(self.window, bd=10, relief=RIDGE)
        main_frame.place(width=1360, height=380, x=0, y=75)
        # --------------------------------------- ENTER ------------------------------------------------ #
        enter_info = LabelFrame(main_frame, text="Gym Members Information", labelanchor="n", bd=5, padx=10,
                                relief=RIDGE, font=SMALL_FONT)
        enter_info.place(width=430, height=360, x=0, y=0)
        # labels inside enter_info LabelFrame:
        # first column:
        subscription_name = Label(enter_info, text="Type Of Subscription", font=SMALL_FONT, padx=10, pady=10)
        subscription_name.grid(row=0, column=0, sticky=W)
        first_name = Label(enter_info, text="First Name", font=SMALL_FONT, padx=10, pady=10)
        first_name.grid(row=1, column=0, sticky=W)
        second_name = Label(enter_info, text="Last Name", font=SMALL_FONT, padx=10, pady=10)
        second_name.grid(row=2, column=0, sticky=W)
        birth_date = Label(enter_info, text="Date Of Birth", font=SMALL_FONT, padx=10, pady=10)
        birth_date.grid(row=3, column=0, sticky=W)
        personal_number = Label(enter_info, text="Mobile Number", font=SMALL_FONT, padx=10, pady=10)
        personal_number.grid(row=4, column=0, sticky=W)
        register_date = Label(enter_info, text="Registration Date", font=SMALL_FONT, padx=10, pady=10)
        register_date.grid(row=5, column=0, sticky=W)
        section_label = Label(enter_info, text="Choose Section", font=SMALL_FONT, padx=10, pady=10)
        section_label.grid(row=6, column=0, sticky=W)
        # second column:
        subscription_box = ttk.Combobox(enter_info, font=SMALL_FONT, textvariable=self.subscription_type,
                                        justify="center", state="readonly")
        subscription_box["values"] = SUBSCRIPTION_TYPES
        subscription_box.current(0)
        subscription_box.grid(row=0, column=1)
        first_entry = Entry(enter_info, font=SMALL_FONT, textvariable=self.first_name, width=22, justify="center")
        first_entry.grid(row=1, column=1)
        second_entry = Entry(enter_info, font=SMALL_FONT, textvariable=self.last_name, width=22, justify="center")
        second_entry.grid(row=2, column=1)
        birth_entry = Entry(enter_info, font=SMALL_FONT, textvariable=self.birthdate, width=22, justify="center")
        birth_entry.grid(row=3, column=1)
        phone_entry = Entry(enter_info, font=SMALL_FONT, textvariable=self.phone, width=22, justify="center")
        phone_entry.grid(row=4, column=1)
        register_entry = Entry(enter_info, font=SMALL_FONT, textvariable=self.register, width=22, justify="center")
        register_entry.grid(row=5, column=1)
        section_box = ttk.Combobox(enter_info, font=SMALL_FONT, textvariable=self.section, justify="center",
                                   state="readonly")
        section_box["values"] = AVAILABLE_SECTIONS
        section_box.current(0)
        section_box.grid(row=6, column=1)

        # --------------------------------------- DESCRIPTION --------------------------------------------- #
        output_info = LabelFrame(main_frame, text="Description", labelanchor="n", bd=5, padx=10, relief=RIDGE,
                                 font=SMALL_FONT)
        output_info.place(width=450, height=360, x=430, y=0)
        self.desc_left = Text(output_info, font=SMALL_FONT, width=47, height=17)
        self.desc_left.grid(row=0, column=0)

        # --------------------------------------- SQL Query ----------------------------------------------- #
        sql_query = LabelFrame(main_frame, text="SQL Query", labelanchor="n", bd=5, padx=10, relief=RIDGE,
                               font=SMALL_FONT)
        sql_query.place(width=460, height=360, x=880, y=0)
        self.sql_command = Text(sql_query, font=("Euphemia", 15, "bold"), width=47, height=17, fg="dark slate gray")
        self.sql_command.grid(row=0, column=0)

        # Buttons Section:
        button_frame = Frame(self.window, bd=10, relief=RIDGE)
        button_frame.place(width=1360, height=55, x=0, y=455)
        # ------------------------------------ BUTTONS ------------------------------------ #
        submit_button = Button(button_frame, text="Submit", bg="dark blue", fg="white", font=SMALL_FONT,
                               width=BUTTON_WIDTH, height=1, command=self.insert_data)
        submit_button.grid(row=0, column=0)

        subscription_button = Button(button_frame, text="Subscription Data", bg="dark slate gray", fg="white",
                                     font=SMALL_FONT, width=BUTTON_WIDTH, height=1,
                                     command=self.display_subscription_data)
        subscription_button.grid(row=0, column=1)

        delete_button = Button(button_frame, text="Delete", bg="red", fg="white", font=SMALL_FONT,
                               width=BUTTON_WIDTH, height=1, command=self.delete_record)
        delete_button.grid(row=0, column=2)

        update_button = Button(button_frame, text="Update", bg="blue violet", fg="white", font=SMALL_FONT,
                               width=BUTTON_WIDTH, height=1, command=self.update_record)
        update_button.grid(row=0, column=3)

        clear_button = Button(button_frame, text="Clear", bg="dark orange", fg="white", font=SMALL_FONT,
                              width=BUTTON_WIDTH, height=1, command=self.clear_fields)
        clear_button.grid(row=0, column=4)

        execute_button = Button(button_frame, text="Execute Query", bg="green", fg="white", font=SMALL_FONT,
                                width=BUTTON_WIDTH, height=1, command=self.display_sql_query)
        execute_button.grid(row=0, column=5)

        exit_button = Button(button_frame, text="Exit", bg="chocolate", fg="white", font=SMALL_FONT, width=19,
                             height=1, command=self.close_window)
        exit_button.grid(row=0, column=6)

        # SQL Table Section:
        table_frame = Frame(self.window, bd=10, relief=RIDGE)
        table_frame.place(width=1360, height=170, x=0, y=510)
        # ----------------------------------------- TABLE ----------------------------------------------- #
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", backgroung="silver", foreground="black", rowheight=25, fieldbackground="silver")
        style.map("Treeview", background=[("selected", "medium sea green")])
        style.configure("Treeview.Heading", background="light steel blue", font=("Arial", 10, "bold"))

        self.gym_members_table = ttk.Treeview(table_frame, columns=COLUMNS)

        scroll_x_label = ttk.Scrollbar(table_frame, orient=HORIZONTAL, command=self.gym_members_table.xview)
        scroll_y_label = ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.gym_members_table.yview)
        scroll_x_label.pack(side=BOTTOM, fill=X)
        scroll_y_label.pack(side=RIGHT, fill=Y)

        self.gym_members_table.heading(COLUMNS[0], text=COLUMNS[0], anchor=W)
        self.gym_members_table.heading(COLUMNS[1], text=COLUMNS[1], anchor=W)
        self.gym_members_table.heading(COLUMNS[2], text=COLUMNS[2], anchor=W)
        self.gym_members_table.heading(COLUMNS[3], text=COLUMNS[3], anchor=W)
        self.gym_members_table.heading(COLUMNS[4], text=COLUMNS[4], anchor=W)
        self.gym_members_table.heading(COLUMNS[5], text=COLUMNS[5], anchor=W)
        self.gym_members_table.heading(COLUMNS[6], text=COLUMNS[6], anchor=W)
        self.gym_members_table["show"] = "headings"
        self.gym_members_table.pack(fill=BOTH, expand=1)
        self.gym_members_table.bind("<ButtonRelease-1>", self.become_sensitive)
        self.display_data()

    # ---------------------------------- FUNCTIONALITY ------------------------------------ #
    def insert_data(self):
        conn = sqlite3.connect('sport_gym.db')
        curr = conn.cursor()

        curr.execute(f'''INSERT INTO gym_members(subscription_type, first_name, last_name, birthdate, phone, 
        register_date, section) 
        VALUES ('{self.subscription_type.get()}', '{self.first_name.get()}', '{self.last_name.get()}', 
        '{self.birthdate.get()}', '{self.phone.get()}', '{self.register.get()}', '{self.section.get()}');''')

        conn.commit()
        conn.close()
        self.display_data()
        messagebox.showinfo(title="About Submit", message="Record Has Been Inserted, Successfully!")

    def display_data(self):
        conn = sqlite3.connect('sport_gym.db')
        curr = conn.cursor()

        rows = curr.execute('''SELECT * FROM gym_members;''').fetchall()
        if len(rows) > 0:
            self.gym_members_table.delete(*self.gym_members_table.get_children())
            for item in rows:
                self.gym_members_table.insert("", END, values=item)

        conn.commit()
        conn.close()

    def get_input(self):
        value = self.sql_command.get("1.0", "end-1c")
        return value

    def add_highlighter(self):
        self.sql_command.tag_add("start", "1.0", "1.6", "1.9", "1.14")
        self.sql_command.tag_add("start", "2.0", "2.6")
        self.sql_command.tag_add("start", "3.0", "3.3")
        self.sql_command.tag_add("start", "4.0", "4.3")
        self.sql_command.tag_add("start", "5.0", "5.3")
        self.sql_command.tag_add("start", "6.0", "6.3")
        self.sql_command.tag_add("start", "7.0", "7.3")
        self.sql_command.tag_add("start", "8.0", "8.3")
        self.sql_command.tag_config("start", foreground="blue")

    def display_sql_query(self):
        conn = sqlite3.connect('sport_gym.db')
        curr = conn.cursor()

        sql_command = self.get_input()
        rows = curr.execute(f'''{sql_command}''').fetchall()
        if len(rows) > 0:
            self.gym_members_table.delete(*self.gym_members_table.get_children())
            for item in rows:
                self.gym_members_table.insert("", END, values=item)

        conn.commit()
        conn.close()
        self.add_highlighter()

    def update_record(self):
        conn = sqlite3.connect('sport_gym.db')
        curr = conn.cursor()

        curr.execute(f'''UPDATE gym_members
        SET subscription_type = '{self.subscription_type.get()}',
            first_name = '{self.first_name.get()}',
            last_name = '{self.last_name.get()}',
            birthdate = '{self.birthdate.get()}',
            phone = '{self.phone.get()}',
            register_date = '{self.register.get()}',
            section = '{self.section.get()}'
        WHERE first_name = '{self.first_name.get()}'
           OR last_name = '{self.last_name.get()}'
           OR phone = '{self.phone.get()}'
        ''')

        conn.commit()
        conn.close()
        self.display_data()
        messagebox.showinfo(title="About Update", message="Record Has Been Updated, Successfully!")

    def become_sensitive(self, event=""):
        table_row = self.gym_members_table.focus()
        table_content = self.gym_members_table.item(table_row)
        current_row = table_content["values"]
        self.subscription_type.set(current_row[0])
        self.first_name.set(current_row[1])
        self.last_name.set(current_row[2])
        self.birthdate.set(current_row[3])
        self.phone.set(current_row[4])
        self.register.set(current_row[5])
        self.section.set(current_row[6])

    def display_subscription_data(self):
        self.desc_left.delete("1.0", END)
        self.desc_left.insert(END, "1. Subscription Type:\t\t\t" + self.subscription_type.get() + "\n" + "\n" + "\n")
        self.desc_left.insert(END, "2. First Name:\t\t\t" + self.first_name.get() + "\n" + "\n" + "\n")
        self.desc_left.insert(END, "3. Last Name:\t\t\t" + self.last_name.get() + "\n" + "\n" + "\n")
        self.desc_left.insert(END, "4. BirthDate:\t\t\t" + self.birthdate.get() + "\n" + "\n" + "\n")
        self.desc_left.insert(END, "5. Phone Number:\t\t\t" + self.phone.get() + "\n" + "\n" + "\n")
        self.desc_left.insert(END, "6. Registration Date:\t\t\t" + self.register.get() + "\n" + "\n" + "\n")
        self.desc_left.insert(END, "7. Selection Type:\t\t\t" + self.section.get())

    def delete_record(self):
        conn = sqlite3.connect('sport_gym.db')
        curr = conn.cursor()

        curr.execute(f'''DELETE FROM gym_members
        WHERE first_name = '{self.first_name.get()}'
           OR last_name = '{self.last_name.get()}'
           OR phone = '{self.phone.get()}'
           ''')

        conn.commit()
        conn.close()
        self.display_data()
        messagebox.showinfo(title="About Delete", message="Record Has Been Deleted, Successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.first_name.set("")
        self.last_name.set("")
        self.birthdate.set("")
        self.phone.set("")
        self.register.set("")
        self.desc_left.delete("1.0", END)
        self.sql_command.delete("1.0", END)

    def close_window(self):
        confirm = messagebox.askyesno(title="Sport Gym Management System", message="Do You Want To Close Program?")
        if confirm > 0:
            self.window.destroy()
            return
        else:
            pass


screen = Tk()
window_object = SportGym(screen)


screen.mainloop()
