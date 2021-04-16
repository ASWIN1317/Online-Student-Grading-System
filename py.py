from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox


class Grade(object):

    def __init__(self):
        self.textin = ''
        self.textinn = ''
        self.conn = sqlite3.connect('C:/Users/Aswini/Desktop/new.db', timeout=10)
        self.cursor = self.conn.cursor()
        self.e_name = ''
        self.e_password = ''
        self.sem=''
        self.dept=''
        self.a=[]
        self.gr={}
        self.subs={}
        self.window=''
        self.v=''
        self.sub_name=None
        self.credits=None
        self.dept=None
        self.sem_no=None
        self.l1=None
        self.l2=None
        self.l3=None
        self.l4=None
        self.but=None

    def helpp(self):
        help(sqlite3)

    def login(self, root):
        root.title("GRADING")
        root.geometry("1000x1000")
        menu = Menu(root)
        root.config(menu=menu)
        menu = Menu(root)
        root.config(menu=menu)
        subm = Menu(menu)
        self.textin = StringVar()
        self.textinn = StringVar()
        menu.add_cascade(label="Help", menu=subm)
        subm.add_command(label="Sqlite3 Docs", command=self.helpp)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, phone TEXT)")
        self.conn.commit()
        c = Canvas(root, bg="black", height=2000, width=1000)
        img = ImageTk.PhotoImage(Image.open("C:/Users/Aswini/Desktop/art1.jpg"))  # PIL solution
        c.create_image(0, 0, anchor=NW, image=img)
        c.pack()
        title=tk.Label(root, text="STUDENT GRADING SYSTEM", fg="black", bg="white",
                 font=("times new roman", 30, "italic"))
        title.place(x=200,y=100)
        username = tk.Label(root, text='USERNAME :', fg="black", bg="white", font=('none 13 bold'))
        username.place(x=300, y=200)
        password = tk.Label(root, text='PASSWORD :', fg="black", bg="white", font=('none 13 bold'))
        password.place(x=300, y=250)
        self.e_name = Entry(root, width=20, font=('none 13 bold'), textvar=self.textin)
        self.e_name.place(x=500, y=200)
        self.e_password = Entry(root, width=20, font=('none 13 bold'), textvar=self.textinn)
        self.e_password.place(x=500, y=250)
        but = tk.Button(root, padx=2, pady=2, text='Login as Student', fg="black", bg="white", command=self.student,
                        font=('none 13 bold'))
        but.place(x=300, y=300)
        but = tk.Button(root, padx=2, pady=2, text='Login as Admin', fg="black", bg="white", command=self.admin,
                        font=('none 13 bold'))
        but.place(x=500, y=300)


        but1 = tk.Button(root, padx=2, pady=2, text='Register', fg="black", bg="white", command=self.register,
                         font=('none 13 bold'))
        but1.place(x=400, y=400)

    def register(self):
        ename = self.e_name.get()
        epass = self.e_password.get()
        self.cursor.execute('INSERT INTO users(name,phone) VALUES (?,?)',(ename,epass))
        self.conn.commit()
        messagebox.showinfo("Information", "Registration successful")
        
    def admin(self):
        admin_name = "admin"
        admin_pass = "123"
        ename = self.e_name.get()
        epass = self.e_password.get()
        if ename == admin_name and epass == admin_pass:
            messagebox.showinfo("Information", "Login successful")
            but = tk.Button(root, padx=2, pady=2, text='Next', fg="black", bg="white", command=self.adminpage,
                            font=('none 13 bold'))
            but.place(x=500, y=400)
        else:
            messagebox.showinfo("Information", "Login failed")
        #self.root.destroy()

    def adminpage(self):
        self.v = tk.IntVar()

        self.window = Toplevel(root)
        self.window.title("ADMIN WEBPAGE")
        self.window.geometry('1000x1000')
        ttk.Label(self.window, text="Choose your operation",
                  font=("Times New Roman", 20)).grid(column=1,
                                                     row=10, padx=10, pady=25)
        options = [("Add new course", 1),
                     ("Delete course", 2),
                     ("Change course credits", 3)]
        r=30

        for opt, val in options:
            tk.Radiobutton(self.window,
                           text=opt,
                           padx=20,
                           variable=self.v,
                           command=self.operation,
                           value=val).grid(column=1,
                                        row=r, padx=10, pady=25)
            r+=20

    def clear(self):
        if self.sub_name:
            self.sub_name.grid_forget()
        if self.credits:
            self.credits.grid_forget()
        if self.dept:
            self.dept.grid_forget()
        if self.sem_no:
            self.sem_no.grid_forget()
        if self.l1:
            self.l1.grid_forget()
        if self.l2:
            self.l2.grid_forget()
        if self.l3:
            self.l3.grid_forget()
        if self.l4:
            self.l4.grid_forget()
        if self.but:
            self.but.grid_forget()

    def operation(self):
        value=self.v.get()
        if value==1:
            self.clear()
            self.l1=ttk.Label(self.window, text="Enter course name",
                      font=("Times New Roman", 20))
            self.l1.grid(column=1,row=100, padx=10, pady=25)
            self.sub_name = Entry(self.window, width=20)
            self.sub_name.grid(column=2, row=100, padx=10, pady=25)
            self.l2=ttk.Label(self.window, text="Enter credits",
                      font=("Times New Roman", 20))
            self.l2.grid(column=1, row=110, padx=10, pady=25)
            self.credits = Entry(self.window, width=20)
            self.credits.grid(column=2, row=110, padx=10, pady=25)
            self.l3=ttk.Label(self.window, text="Enter department",
                      font=("Times New Roman", 20))
            self.l3.grid(column=1, row=120, padx=10, pady=25)
            self.dept = Entry(self.window, width=20)
            self.dept.grid(column=2, row=120, padx=10, pady=25)
            self.l4=ttk.Label(self.window, text="Enter semester",
                      font=("Times New Roman", 20))
            self.l4.grid(column=1, row=130, padx=10, pady=25)
            self.sem_no = Entry(self.window, width=20)
            self.sem_no.grid(column=2, row=130, padx=10, pady=25)
            self.but = tk.Button(self.window, padx=2, pady=2, text='Submit', fg="black", bg="white", command=self.add,
                            font=('none 13 bold'))
            self.but.grid(column=1, row=140, padx=10, pady=25)
        elif value==2:
            self.clear()
            self.l1=ttk.Label(self.window, text="Enter course name",
                      font=("Times New Roman", 20))
            self.l1.grid(column=1,row=100, padx=10, pady=25)
            self.sub_name = Entry(self.window, width=20)
            self.sub_name.grid(column=2, row=100, padx=10, pady=25)
            self.but = tk.Button(self.window, padx=2, pady=2, text='Submit', fg="black", bg="white", command=self.delete,
                            font=('none 13 bold'))
            self.but.grid(column=1, row=120, padx=10, pady=25)
        elif value==3:
            self.clear()
            self.l1=ttk.Label(self.window, text="Enter course name",
                      font=("Times New Roman", 20))
            self.l1.grid(column=1,row=100, padx=10, pady=25)
            self.sub_name = Entry(self.window, width=20)
            self.sub_name.grid(column=2, row=100, padx=10, pady=25)
            self.l2=ttk.Label(self.window, text="Enter credits",
                      font=("Times New Roman", 20))
            self.l2.grid(column=1,row=110, padx=10, pady=25)
            self.credits = Entry(self.window, width=20)
            self.credits.grid(column=2, row=110, padx=10, pady=25)
            self.but = tk.Button(self.window, padx=2, pady=2, text='Submit', fg="black", bg="white", command=self.update,
                            font=('none 13 bold'))
            self.but.grid(column=1, row=130, padx=10, pady=25)

    def add(self):
        self.cursor.execute('INSERT INTO sub_list(sub_name,credits,sem_no,dept) VALUES (?,?,?,?)',
                            (self.sub_name.get(),self.credits.get(),self.sem_no.get(),self.dept.get()))
        self.conn.commit()

    def delete(self):
        print(self.sub_name.get())
        self.cursor.execute('DELETE FROM sub_list WHERE sub_name=?',(self.sub_name.get(),))
        self.conn.commit()

    def update(self):
        self.cursor.execute('UPDATE sub_list SET credits=? WHERE sub_name=?',(self.credits.get(),self.sub_name.get()))
        self.conn.commit()

    def student(self):
        name1 = self.textin.get()
        pass1 = self.textinn.get()
        with self.conn:
            self.cursor.execute('SELECT * FROM users WHERE name = ? AND phone = ?', (name1, pass1))
            entry = self.cursor.fetchall()
            if not entry:
                messagebox.showinfo("Information", "Login failed")
            else:
                messagebox.showinfo("Information", "Login successful")
                but = tk.Button(root, padx=2, pady=2, text='Next', fg="black", bg="white", command=self.grades, font=('none 13 bold'))
                but.place(x=500, y=400)
        #self.root.destroy()

    def grades(self):
        self.window = Toplevel(root)
        self.window.title("GRADE")
        self.window.geometry('1000x1000')
        # label text for title
        ttk.Label(self.window, text="Semester Grading",
                  font=("Times New Roman", 30)).grid(row=0, column=1)

        ttk.Label(self.window, text="Enter your details",
                  font=("Times New Roman", 20)).grid(row=7, column=1)

        # label
        ttk.Label(self.window, text="Select the department :",
                  font=("Times New Roman", 20)).grid(column=0,
                                                     row=20, padx=10, pady=25)
        ttk.Label(self.window, text="Select the semester :",
                  font=("Times New Roman", 20)).grid(column=0,
                                                     row=40, padx=10, pady=25)

        n = tk.StringVar()
        self.dept = ttk.Combobox(self.window, width=27,
                                   textvariable=n)

        # Adding combobox drop down list
        self.dept['values'] = ('CSE',
                                 'ECE',
                                 'CHEM',
                                 'EEE',
                                 'MECH',
                                 'CIVIL',
                                 'IT',
                                 'EIE')

        self.dept.grid(column=1, row=20)
        self.dept.current(0)

        n1 = tk.StringVar()
        self.sem = ttk.Combobox(self.window, width=27,
                                  textvariable=n1)
        self.sem['values'] = ('1',
                                '2',
                                '3',
                                '4',
                                '5',
                                '6',
                                '7',
                                '8')

        self.sem.grid(column=1, row=40)
        self.sem.current(0)
        but = tk.Button(self.window, padx=2, pady=2, text='Submit', fg="black", bg="white", command=self.calculate,
                        font=('none 13 bold'))
        but.place(x=400, y=300)

    def calculate(self):
        sem = self.sem.get()
        dept = self.dept.get()
        self.window = Toplevel(root)
        self.window.title("GRADE")
        self.window.geometry('1000x1000')
        ttk.Label(self.window, text="Enter your grades",
                  font=("Times New Roman", 20)).grid(column=1,
                                                     row=10, padx=10, pady=25)
        try:
            self.cursor.execute("SELECT sub_name, credits from sub_list WHERE sem_no= ? AND dept = ?", (sem, dept))
            records = self.cursor.fetchall()
            rows = 20
            for i in records:
                key = i[0]
                self.subs[key] = int(i[1])
                self.gr[key] = ''
            for i in records:
                ttk.Label(self.window, text=i[0],
                          font=("Times New Roman", 20)).grid(column=0,
                                                             row=rows, padx=10, pady=25)
                aa = Entry(self.window, width=20)
                aa.grid(column=1, row=rows, padx=10, pady=25)
                rows += 20
                self.a.append(aa)
            but = tk.Button(self.window, padx=2, pady=2, text='Calculate CGPA', fg="black", bg="white", command=self.c,
                            font=('none 13 bold')).grid(column=2,row=80, padx=10, pady=25)
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

    def c(self):
        gp={'S':10, 'A':9, 'B':8, 'C':7, 'D':6, 'E':5}
        keys=list(self.gr.keys())
        for i in range(len(self.a)):
            k=keys[i]
            s=self.a[i].get()
            self.gr[k]=gp[s]
        sum1=0
        for i in keys:
            sum1+=self.subs[i]*self.gr[i]
        b = list(self.subs.values())
        total = sum(b)
        cgpa = sum1/total
        cgpa = round(cgpa,2)
        ttk.Label(self.window, text="CGPA: "+str(cgpa),
                  font=("Times New Roman", 20)).grid(column=2,
                                                     row=100, padx=10, pady=25)
        








root = tk.Tk()
app = Grade()
app.login(root)
root.mainloop()
