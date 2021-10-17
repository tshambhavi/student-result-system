from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import random
import sqlite3
import score
conn = sqlite3.connect('Marksheet1db.db')
cur = conn.cursor()

def main():
    root = Tk()
    app = Window_1(root)
    root.mainloop()
    conn.commit()


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("GBU- Student Login")
        self.master.geometry('1200x680')
        self.master.config(bg = 'Navajo white')
        self.Frame = Frame(self.master, bg = 'Navajo white')
        self.Frame.pack()


        self.Username = StringVar()
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = 'Student Login', font = ('arial',35,'bold'), bg = 'Navajo white', fg = 'Black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)

        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1100, height = 580, relief ='ridge', bg = 'Navajo white', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 2, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief = 'ridge',bg = 'Navajo white', bd = 15,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 3, column = 0)



        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('arial',20,'bold'), bg = 'Navajo white', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), textvariable = self.Username)
        self.text_Username.grid(row = 0, column = 1, padx = 50)

        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('arial',20,'bold'), bg = 'Navajo white', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'bold'), show = '*', textvariable = self.Password)
        self.text_Password.grid(row = 1, column = 1)


        self.btnLogin = Button(self.Login_Frame_2, text = 'Login', width = 10, font = ('airia',15,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnregister = Button(self.Login_Frame_2, text = 'Register', width= 10, font = ('airia',15,'bold'), command = self.register_student)
        self.btnregister.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2, text = 'Reset', width = 10, font = ('airia',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 2, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2, text = 'Exit', width = 10, font = ('airia',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 3, padx = 8, pady = 20)


    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if u"" or p=="":
            messagebox.showerror("Error","Fill all the required fields",parent=self.master)

        else:

            cur.execute('SELECT * FROM STUDENT WHERE un = ? and password = ?',[u,p])
            row=cur.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Username or Password",parent=self.master)


            else:
                r1=float(row[10])
                r2=float(row[11])
                r3=float(row[12])
                r4=str(row[13])
                r5=str(row[14])
                r6=str(row[15])
                score.final_result(r1,r2,r3,r4,r5,r6)

                self.master.destroy()


    def Reset(self):
         self.Username.set("")
         self.Password.set("")
         self.text_Username.focus()



    def Exit(self):
        self.Exit = messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def register_student(self):
        self.master.destroy()
        score.marksheet()





if __name__ == '__main__':
    main()