from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3

with sqlite3.connect('login.db') as db:
    c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()


class Menu:
    def __init__(self, master):
        self.mainframe = Frame(master)
        self.mainframe.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.mainframe.configure(width=125)
        self.bg_label = Label(self.mainframe)
        self.attend_btn = Button(self.mainframe)
        self.attend_info = Button(self.mainframe)
        self.gen_info = Button(self.mainframe)
        self.exit = Button(self.mainframe)

    def valid(self):
        with sqlite3.connect('login.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(app.user_Entry.get()), (app.user_Pass.get())])
        result = c.fetchall()
        if result:
            messagebox.showinfo("SUCCESS!!!", "Logged in Successfully")
            app.startframe.place_forget()
            self.bg_label.place(relx=0.0, rely=0.0, height=400, width=650)

            self._img0 = PhotoImage(file="background.png")
            self.bg_label.configure(image=self._img0)

            self.attend_btn.place(relx=0.123, rely=0.025, height=184, width=197)
            self._img1 = PhotoImage(file="attendence.png")
            self.attend_btn.configure(image=self._img1)
            self.attend_btn.configure(pady="0", width=197)

            self.attend_info.place(relx=0.569, rely=0.025, height=184, width=197)
            self._img2 = PhotoImage(file="PicsArt_03-15-05.44.10.png")
            self.attend_info.configure(image=self._img2)
            self.attend_info.configure(pady="0", width=197, command=a.attend)

            self.gen_info.place(relx=0.354, rely=0.525, height=184, width=197)
            self._img3 = PhotoImage(file="820841618.png")
            self.gen_info.configure(image=self._img3)
            self.gen_info.configure(pady="0")

            self.exit.place(relx=0.862, rely=0.875, height=34, width=67)
            self.exit.configure(background="#d88a9f", font="Arial", text="Exit", width=67, pady=0, command=root.quit)
        else:
            messagebox.showerror("Error", "Username or Password is wrong")
            app.user_Entry.set("")
            app.user_Pass.set("")

    def new_user(self):
        with sqlite3.connect('login.db') as db:
            c = db.cursor()
        find_user = 'SELECT * FROM user WHERE username = ?'
        c.execute(find_user, [(app.new_user_Entry.get())])
        if c.fetchall():
            messagebox.showerror('Error!', 'Username Taken Try a Diffrent One.')
            self.clear_new_entry()
        else:
            insert = 'INSERT INTO user(username,password,subject) VALUES(?,?,?)'
            c.execute(insert, [(app.new_user_Entry.get()), (app.new_user_Pass.get()), (app.new_user_Sub.get())])
            db.commit()
            messagebox.showinfo("SUCCESS!!!", "Account Created Successfully!")
            self.clear_new_entry()

    def clear_new_entry(self):
        app.new_user_Entry.set("")
        app.new_user_Pass.set("")
        app.new_user_Sub.set("")
        app.startframe.place()


class Login:
    def __init__(self, master):
        self.startframe = Frame(master)
        self.startframe.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.startframe.configure(width=645)
        self.Label1 = Label(self.startframe)
        self.Label2 = Label(self.startframe)
        self.user_Entry = StringVar()
        self.user_Pass = StringVar()
        self.Entry1 = Entry(self.startframe, textvariable=self.user_Entry)
        self.Entry2 = Entry(self.startframe, show="*", textvariable=self.user_Pass)
        self.Button1 = Button(self.startframe)
        self.TSeparator1 = ttk.Separator(self.startframe)
        self.Label3 = Label(self.startframe)
        self.Label4 = Label(self.startframe)
        self.Label5 = Label(self.startframe)
        self.new_user_Entry = StringVar()
        self.Entry3 = Entry(self.startframe, textvariable=self.new_user_Entry)
        self.new_user_Pass = StringVar()
        self.Entry4 = Entry(self.startframe, show="*", textvariable=self.new_user_Pass)
        self.new_user_Sub = StringVar()
        self.Entry5 = Entry(self.startframe, textvariable=self.new_user_Sub)
        self.Button2 = Button(self.startframe)
        self.Label6 = Label(self.startframe)
        self.Label7 = Label(self.startframe)

    def front_window(self):
        self.Label1.place(relx=0.0, rely=0.257, height=25, width=90)
        self.Label1.configure(anchor='e')
        self.Label1.configure(font="Arial")
        self.Label1.configure(text='''Username''')
        self.Label1.configure(width=94)

        self.Label2.place(relx=0.0, rely=0.371, height=25, width=90)
        self.Label2.configure(anchor='e')
        self.Label2.configure(font="Arial")
        self.Label2.configure(text='''Password''')
        self.Label2.configure(width=94)

        self.Entry1.place(relx=0.17, rely=0.257, height=30, relwidth=0.253)
        self.Entry1.configure(background="White")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=164)

        self.Entry2.place(relx=0.17, rely=0.371, height=30, relwidth=0.253)
        self.Entry2.configure(background="White")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=164)

        self.Button1.place(relx=0.139, rely=0.514, height=34, width=67)
        self.Button1.configure(background="#20b9d8", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        self.Button1.configure(text='''Log in''')
        self.Button1.configure(width=67, foreground="#ffffff")
        self.Button1.configure(command=m.valid, font=("Arial Black", 10))

        self.TSeparator1.place(relx=0.448, rely=-0.029, relheight=1.343)
        self.TSeparator1.configure(orient="vertical")

        self.Label3.place(relx=0.463, rely=0.257, height=25, width=120)
        self.Label3.configure(anchor='e')
        self.Label3.configure(font="Arial")
        self.Label3.configure(text='''Enter Username''')
        self.Label3.configure(width=94)

        self.Label4.place(relx=0.463, rely=0.371, height=25, width=120)
        self.Label4.configure(anchor='e')
        self.Label4.configure(font="Arial")
        self.Label4.configure(text='''Enter Password''')
        self.Label4.configure(width=94)

        self.Label5.place(relx=0.463, rely=0.486, height=25, width=120)
        self.Label5.configure(anchor='e')
        self.Label5.configure(font="Arial")
        self.Label5.configure(text='''Subject''')
        self.Label5.configure(width=94)

        self.Entry3.place(relx=0.679, rely=0.257, height=30, relwidth=0.253)
        self.Entry3.configure(background="White")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=164)

        self.Entry4.place(relx=0.679, rely=0.371, height=30, relwidth=0.253)
        self.Entry4.configure(background="White")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=164)

        self.Entry5.place(relx=0.679, rely=0.486, height=30, relwidth=0.253)
        self.Entry5.configure(background="White")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(width=164)

        self.Button2.place(relx=0.648, rely=0.629, height=34, width=67)
        self.Button2.configure(background="#20b9d8", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        self.Button2.configure(text='''Sign up''', foreground="#ffffff")
        self.Button2.configure(width=67, command=m.new_user, font=("Arial Black", 10))

        self.Label6.place(relx=0.139, rely=0.657)
        self.Label6.configure(font="Arial")
        self.Label6.configure(text='''New User?''')

        self.Label7.place(relx=0.123, rely=0.714)
        self.Label7.configure(text='''Please sign up''', font="Arial")


class AttendInfo:
    def __init__(self, master):
        self.Frame1 = Frame(master)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Label1 = Label(self.Frame1)
        self.view_btn = Button(self.Frame1)
        self.exit_btn = Button(self.Frame1)
        self.lecture_entry = StringVar()
        self.lec_entry = Entry(self.Frame1, textvariable=self.lecture_entry)
        self.cls_entry = StringVar()
        self.class_entry = Entry(self.Frame1, textvariable=self.cls_entry)
        self.treeview2 = ttk.Treeview(self.Frame1, column=("column1", "column2", "column3"), show='headings')
        self.vsb = ttk.Scrollbar(self.Frame1, orient="vertical", command=self.treeview2.yview)

    def attend(self):
        m.mainframe.place_forget()
        self.Frame1.configure(width=645)

        self.Label1.place(relx=0.0, rely=0.0, height=400, width=650)
        self._img0 = PhotoImage(file="background2.png")
        self.Label1.configure(image=self._img0)
        self.Label1.configure(width=644)

        self.view_btn.place(relx=0.646, rely=0.2, height=34, width=67)
        self.view_btn.configure(background="#5983d8", foreground="#ffffff", text='''View''', width=67,
                                command=self.view)
        self.view_btn.configure(font=("Arial Black", 12))

        self.exit_btn.place(relx=0.862, rely=0.85, height=34, width=67)
        self.exit_btn.configure(background="#5983d8", foreground="#ffffff", text='''Exit''', width=67,
                                command=root.quit)
        self.exit_btn.configure(font=("Arial Black", 12))

        self.lec_entry.place(relx=0.323, rely=0.275, height=30, relwidth=0.252)
        self.lec_entry.configure(width=164, background="white")

        self.class_entry.place(relx=0.323, rely=0.15, height=30, relwidth=0.252)
        self.class_entry.configure(width=164, background="white")

        self.treeview2.heading("#1", text="Roll")
        self.treeview2.heading("#2", text="First Name")
        self.treeview2.heading("#3", text="Lecture Status", anchor=W)
        self.treeview2.configure(yscrollcommand=self.vsb.set)
        self.treeview2.place(relx=0.015, rely=0.375, relheight=0.593, relwidth=0.815)

        self.vsb.place(relx=0.0, rely=0.0)

    def view(self):
        records = self.treeview2.get_children()
        for shahid in records:
            self.treeview2.delete(shahid)
        with sqlite3.connect('login.db') as db:
            c = db.cursor()
        view_attend = 'SELECT Roll, first_name, {lecture} FROM maths WHERE class = ?'.format(lecture=self.lec_entry.get())
        c.execute(view_attend, [(self.cls_entry.get())])
        rows = c.fetchall()
        for row in rows:
            print(row)
            self.treeview2.insert("", END, values=row)
        c.close()
        self.cls_entry.set("")
        self.lecture_entry.set("")


if __name__ == '__main__':
    root = Tk()
    root.title("AttendEdu")
    root.geometry("650x400")
    root.resizable(width=False, height=False)
    a = AttendInfo(root)
    m = Menu(root)
    app = Login(root)
    app.front_window()
    root.mainloop()
