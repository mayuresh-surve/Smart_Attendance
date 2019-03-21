from tkinter import *
import sqlite3

with sqlite3.connect('login.db') as db:
    c = db.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()


class TakeAttendance:
    def __init__(self, master):
        self.take_gui = Frame(master)
        self.take_gui.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Label12 = Label(self.take_gui)
        self.view_btn1 = Button(self.take_gui)
        self.exit_btn1 = Button(self.take_gui)
        self.lecture_entry1 = StringVar()
        self.lec_entry2 = Entry(self.take_gui, textvariable=self.lecture_entry1)
        self.cls_entry1 = StringVar()
        self.class_entry1 = Entry(self.take_gui, textvariable=self.cls_entry1)

    def attend_gui(self):
        self.take_gui.configure(width=645)

        self.Label12.place(relx=0.0, rely=0.0, height=400, width=650)
        self._img01 = PhotoImage(file="background2.png")
        self.Label12.configure(image=self._img01)
        self.Label12.configure(width=644)

        self.view_btn1.place(relx=0.231, rely=0.425, height=44, width=167)
        self.view_btn1.configure(background="#5983d8", foreground="#ffffff", text='''Take Attendence''', width=67, command=alt.att)
        self.view_btn1.configure(font=("Arial Black", 12))

        self.exit_btn1.place(relx=0.862, rely=0.85, height=34, width=67)
        self.exit_btn1.configure(background="#5983d8", foreground="#ffffff", text='''Exit''', width=67,
                                 command=root.quit)
        self.exit_btn1.configure(font=("Arial Black", 12))

        self.lec_entry2.place(relx=0.323, rely=0.275, height=30, relwidth=0.252)
        self.lec_entry2.configure(width=164, background="white")

        self.class_entry1.place(relx=0.323, rely=0.15, height=30, relwidth=0.252)
        self.class_entry1.configure(width=164, background="white")


class Attendance:
    def __init__(self, master):
        self.frame = Frame(master)
        self.x = 0
        self.z = 1
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.y4 = 0
        self.y5 = 0
        self.y6 = 0
        self.btn = []
        self.btn1 = []
        self.btn2 = []
        self.btn3 = []
        self.btn4 = []
        self.btn5 = []

    def addcol(self):
        with sqlite3.connect('login.db') as db:
            c = db.cursor()
        gen_col = 'ALTER TABLE maths ADD {lecture} INTEGER DEFAULT "0"'.format(lecture=t.lecture_entry1.get())
        c.execute(gen_col)

    def colour(self, y1):
        self.a = self.btn[y1]
        if self.a['bg'] == 'red':
            self.a['bg'] = 'green'
            with sqlite3.connect('login.db') as db:
                c = db.cursor()
            add_attend = 'UPDATE maths SET {lec}=1 WHERE Roll = ?'.format(lec=t.lecture_entry1.get())
            c.execute(add_attend, [int(y1)])
            db.commit()
            c.close()
        else:
            self.a['bg'] = 'red'

    def colour1(self, y2):
        self.a = self.btn1[y2]
        if self.a['bg'] == 'red':
            self.a['bg'] = 'green'
            with sqlite3.connect('login.db') as db:
                c = db.cursor()
            add_attend = 'UPDATE maths SET {lec}=1 WHERE Roll = ?'.format(lec=t.lecture_entry1.get())
            c.execute(add_attend, [int(y2)])
            db.commit()
            c.close()
        else:
            self.a['bg'] = 'red'

    def colour2(self, y3):
        self.a = self.btn2[y3]
        if self.a['bg'] == 'red':
            self.a['bg'] = 'green'
        else:
            self.a['bg'] = 'red'

    def colour3(self, y4):
        self.a = self.btn3[y4]
        if self.a['bg'] == 'red':
            self.a['bg'] = 'green'
        else:
            self.a['bg'] = 'red'

    def colour4(self, y5):
        self.a = self.btn4[y5]
        if self.a['bg'] == 'red':
            self.a['bg'] = 'green'
        else:
            self.a['bg'] = 'red'

    def colour5(self, y6):
        print(y6)
        self.a = self.btn5[y6]
        if self.a['bg'] == 'red':
            self.a['bg'] = 'green'
        else:
            self.a['bg'] = 'red'

    def att(self):
        self.addcol()
        t.take_gui.place_forget()
        self.frame.place(anchor=NW)
        self.exit = Button(self.frame, text="Done", bg="blue", fg="white", font=("Arial", 20), command=root.quit)
        self.exit.grid(row=7, column=11, sticky=SE)

        self.n = 60
        for i in range(10):
            self.btn.append(Button(self.frame, width=3, bg="red", fg="white", font=("Arial", 20)))

        for j in self.btn:
            j.grid(row=1, column=self.x)
            self.x = self.x+1
            j['text'] = str(self.z)
            self.z += 1
            self.y1 += 1
        self.b0 = self.btn[0]
        self.b0['command'] = lambda: self.colour(0)

        self.b1 = self.btn[1]
        self.b1['command'] = lambda: self.colour(1)

        self.b2 = self.btn[2]
        self.b2['command'] = lambda: self.colour(2)

        self.b3 = self.btn[3]
        self.b3['command'] = lambda: self.colour(3)

        self.b4 = self.btn[4]
        self.b4['command'] = lambda: self.colour(4)

        self.b5 = self.btn[5]
        self.b5['command'] = lambda: self.colour(5)

        self.b6 = self.btn[6]
        self.b6['command'] = lambda: self.colour(6)

        self.b7 = self.btn[7]
        self.b7['command'] = lambda: self.colour(7)

        self.b8 = self.btn[8]
        self.b8['command'] = lambda: self.colour(8)

        self.b9 = self.btn[9]
        self.b9['command'] = lambda: self.colour(9)

        for i in range(10):
            self.btn1.append(Button(self.frame, width=3, text="x", bg="red", fg="white", font=("Arial", 20)))
        self.x = 0
        for j in self.btn1:
            j.grid(row=2, column=self.x)
            self.x = self.x+1
            j['text'] = str(self.z)
            self.z += 1

        self.btn1[0]['command'] = lambda: self.colour1(0)

        self.btn1[1]['command'] = lambda: self.colour1(1)

        self.btn1[2]['command'] = lambda: self.colour1(2)

        self.btn1[3]['command'] = lambda: self.colour1(3)

        self.btn1[4]['command'] = lambda: self.colour1(4)

        self.btn1[5]['command'] = lambda: self.colour1(5)

        self.btn1[6]['command'] = lambda: self.colour1(6)

        self.btn1[7]['command'] = lambda: self.colour1(7)

        self.btn1[8]['command'] = lambda: self.colour1(8)

        self.btn1[9]['command'] = lambda: self.colour1(9)

        for i in range(10):
            self.btn2.append(Button(self.frame, width=3, text="x", bg="red", fg="white", font=("Arial", 20)))
        self.x = 0
        for j in self.btn2:
            j.grid(row=3, column=self.x)
            self.x = self.x+1
            j['text'] = str(self.z)
            self.z += 1

        self.btn2[0]['command'] = lambda: self.colour2(0)
        self.btn2[1]['command'] = lambda: self.colour2(1)
        self.btn2[2]['command'] = lambda: self.colour2(2)
        self.btn2[3]['command'] = lambda: self.colour2(3)
        self.btn2[4]['command'] = lambda: self.colour2(4)
        self.btn2[5]['command'] = lambda: self.colour2(5)
        self.btn2[6]['command'] = lambda: self.colour2(6)
        self.btn2[7]['command'] = lambda: self.colour2(7)
        self.btn2[8]['command'] = lambda: self.colour2(8)
        self.btn2[9]['command'] = lambda: self.colour2(9)

        for i in range(10):
            self.btn3.append(Button(self.frame, width=3,text="x", bg="red",fg="white", font=("Arial", 20)))
        self.x = 0
        for j in self.btn3:
            j.grid(row=4, column=self.x)
            self.x = self.x+1
            j['text'] = str(self.z)
            self.z += 1

        self.btn3[0]['command'] = lambda: self.colour3(0)
        self.btn3[1]['command'] = lambda: self.colour3(1)
        self.btn3[2]['command'] = lambda: self.colour3(2)
        self.btn3[3]['command'] = lambda: self.colour3(3)
        self.btn3[4]['command'] = lambda: self.colour3(4)
        self.btn3[5]['command'] = lambda: self.colour3(5)
        self.btn3[6]['command'] = lambda: self.colour3(6)
        self.btn3[7]['command'] = lambda: self.colour3(7)
        self.btn3[8]['command'] = lambda: self.colour3(8)
        self.btn3[9]['command'] = lambda: self.colour3(9)

        for i in range(10):
            self.btn4.append(Button(self.frame,width=3, text="x", bg="red", fg="white", font=("Arial", 20)))
        self.x = 0
        for j in self.btn4:
            j.grid(row=5, column=self.x)
            self.x = self.x+1
            j['text'] = str(self.z)
            self.z += 1

        self.btn4[0]['command'] = lambda: self.colour4(0)
        self.btn4[1]['command'] = lambda: self.colour4(1)
        self.btn4[2]['command'] = lambda: self.colour4(2)
        self.btn4[3]['command'] = lambda: self.colour4(3)
        self.btn4[4]['command'] = lambda: self.colour4(4)
        self.btn4[5]['command'] = lambda: self.colour4(5)
        self.btn4[6]['command'] = lambda: self.colour4(6)
        self.btn4[7]['command'] = lambda: self.colour4(7)
        self.btn4[8]['command'] = lambda: self.colour4(8)
        self.btn4[9]['command'] = lambda: self.colour4(9)

        for i in range(10):
            self.btn5.append(Button(self.frame, width=3, text="x", bg="red", fg="white", font=("Arial", 20)))
        self.x = 0
        for j in self.btn5:
            j.grid(row=6, column=self.x)
            self.x = self.x+1
            j['text'] = str(self.z)
            self.z += 1
        self.z = 0
        self.btn5[0]['command'] = lambda: self.colour5(0)
        self.btn5[1]['command'] = lambda: self.colour5(1)
        self.btn5[2]['command'] = lambda: self.colour5(2)
        self.btn5[3]['command'] = lambda: self.colour5(3)
        self.btn5[4]['command'] = lambda: self.colour5(4)
        self.btn5[5]['command'] = lambda: self.colour5(5)
        self.btn5[6]['command'] = lambda: self.colour5(6)
        self.btn5[7]['command'] = lambda: self.colour5(7)
        self.btn5[8]['command'] = lambda: self.colour5(8)
        self.btn5[9]['command'] = lambda: self.colour5(9)


if __name__ == "__main__":
    root = Tk()
    root.title("Login")
    root.geometry("650x400")
    root.resizable(width=False, height=False)
    t = TakeAttendance(root)
    alt = Attendance(root)
    t.attend_gui()
    root.mainloop()
