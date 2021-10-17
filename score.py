from tkinter import *
import sqlite3
import tkinter
import random
from tkinter import messagebox
from tkinter import ttk
from functools import partial
import Log_in

conn = sqlite3.connect('Marksheet1db.db')
cur = conn.cursor()

cur.executescript('''

CREATE TABLE IF NOT EXISTS STUDENT(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Name TEXT UNIQUE,
    un TEXT UNIQUE,
    password VARCHAR(15),
    confpassword VARCHAR(15),
    m1 INTEGER,
    m2 INTERGER,
    m3 INTEGER,
    m4 INTEGER,
    m5 INTEGER,
    gt INTEGER,
    per INTEGER,
    cgpa INTEGER,
    grade VARCHAR(15),
    div VARCHAR(15),
    result VARCHAR(15)


);
''')


def marksheet():
    root=Tk()
    root.title("GBU-Student Registration")
    root.resizable(0,0)
    root.geometry("1000x800")
    root.config(bg = 'Navajo white')


    Name=StringVar()
    un=StringVar()
    password1=StringVar()
    confpassword=StringVar()
    m1=DoubleVar()
    m2=DoubleVar()
    m3=DoubleVar()
    m4=DoubleVar()
    m5=DoubleVar()
    gt=DoubleVar()
    per=DoubleVar()
    cgpa=DoubleVar()
    grade=StringVar()
    div=StringVar()
    result=StringVar()



    def Add():



            conn = sqlite3.connect('Marksheet1db.db')
            cur = conn.cursor()

            v1=Name.get()
            v2=un.get()
            v3=password1.get()
            v4=confpassword.get()
            v5=m1.get()
            v6=m2.get()
            v7=m3.get()
            v8=m4.get()
            v9=m5.get()
            v10=gt.get()
            v11=per.get()
            v12=cgpa.get()
            v13=grade.get()
            v14=div.get()
            v15=result.get()
            if(v3==v4 and len(v2)!=0):


                cur.execute('''INSERT INTO STUDENT(Name,un,password,confpassword,m1,m2,m3,m4,m5,gt,per,cgpa,grade,div,result) VALUES (?,?,?,\
                                                       ?,?,?,?,?,?,?,?,?,?,?,?)''',(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15))

                messagebox.showinfo("Registered","Registration Successfull")

            else:
                messagebox.showinfo("Error","Password or Username Entry Error")

            conn.commit()
            conn.close()

    def Update():


            conn = sqlite3.connect('Marksheet1db.db')
            cur = conn.cursor()

            v1=Name.get()
            v2=un.get()
            v3=password1.get()
            v4=confpassword.get()
            v5=m1.get()
            v6=m2.get()
            v7=m3.get()
            v8=m4.get()
            v9=m5.get()
            v10=gt.get()
            v11=per.get()
            v12=cgpa.get()
            v13=grade.get()
            v14=div.get()
            v15=result.get()

            if(v3==v4 and len(v2)!=0):
                con = sqlite3.connect('Marksheet1db.db')
                cur = con.cursor()

                cur.execute('''INSERT OR REPLACE INTO STUDENT(Name,un,password,confpassword,m1,m2,m3,m4,m5,gt,per,cgpa,grade,div,result) VALUES (?,\
                             ?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15))
                messagebox.showinfo("Success","Record Updated Successfully")
                reset()

                con.commit()
                con.close()


            else:
                messagebox.showinfo("Error","Password or Username Entry Error")

            conn.commit()
            conn.close()


    def Exit():
        Exit = tkinter.messagebox.askyesno('Marksheet','Confirm if you want to Exit')
        if Exit > 0:
            root.destroy()
            Log_in.main()
            return


    def reset():
        Name.set(' ')
        un.set(' ')
        password1.set('')
        confpassword.set('')
        m1.set(' ')
        m2.set(' ')
        m3.set(' ')
        m4.set(' ')
        m5.set(' ')
        gt.set(' ')
        per.set(' ')
        cgpa.set(' ')
        grade.set(' ')
        div.set(' ')
        result.set(' ')



    def Compute():
        x1 = (m1.get());      x2 = (m2.get());    x3 = (m3.get());      x4 = (m4.get());    x5 = (m5.get())

        if x1 > 100:
            tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
            return
        if x2 > 100:
            tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
            return
        if x3 > 100:
            tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
            return
        if x4 > 100:
            tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
            return
        if x5 > 100:
            tkinter.messagebox.askokcancel('Attention','Please enter Correct Marks')
            return


        tot = x1+x2+x3+x4+x5
        gt.set(tot)

        Per = ((x1+x2+x3+x4+x5) * 100)/500
        per.set(Per)


        cg = (((x1+x2+x3+x4+x5) * 100)/500) / 9.5
        cgpa.set(round(cg,1))

        if cg > 10:
            cgpa.set(10)


        if (((x1+x2+x3+x4+x5) * 100)/500) <= 40:
            grd = 'G'
        elif (((x1+x2+x3+x4+x5) * 100)/500) <= 50:
            grd = 'F'
        elif (((x1+x2+x3+x4+x5) * 100)/500) <= 60:
            grd = 'E'
        elif (((x1+x2+x3+x4+x5) * 100)/500) <= 70:
            grd = 'D'
        elif (((x1+x2+x3+x4+x5) * 100)/500) <= 80:
            grd = 'C'
        elif (((x1+x2+x3+x4+x5) * 100)/500) <= 90:
            grd = 'B'
        else:
            grd = 'A'

        grade.set(grd)

        count = 0
        if x1 < 33:
            count = count + 1
        if x2 < 33:
            count = count + 1
        if x3 < 33:
            count = count + 1
        if x4 < 33:
            count = count + 1
        if x5 < 33:
            count = count + 1

        if (count == 0):
            result.set('PASS')
        elif (count == 1 or count == 2 ):
            result.set('SUPPLY')
        else:
            result.set('FAIL')

        if Per <= 45 and result != "FAIL":
            div.set('THIRD')
        elif Per <= 60 and result != "FAIL":
            div.set('SECOND')
        elif Per <= 100:
            div.set('FIRST')

    f2 = LabelFrame(root, width= 900, height=700, font=("verdana",16),  relief='ridge',bd=13, bg = 'Navajo white').place(x=50,y=50)
    Details=Label(f2, text="Enter details of the student:", font=("verdana",18),bg = 'Navajo white').place(x=170, y= 80)
    name=Label(f2, text= "Name:", font=("verdana",16), bg = 'Navajo white').place(x=170, y= 140)
    entry1=Entry(f2, textvariable=Name, width=70).place(x=450, y=145, width= 200)
    uname=Label(f2, text="Username:", font=("verdana",16), bg = 'Navajo white').place(x=170, y=200)
    entry2=Entry(f2, textvariable=un, width=70).place(x=450, y=205, width= 200)
    pword=Label(f2, text="Password:", font=("verdana",16), bg = 'Navajo white').place(x=170, y=260)
    entry3=Entry(f2, show="*", textvariable=password1, width=70).place(x=450, y=265, width= 200)
    conf_pword=Label(f2, text="Confirm Password:", font=("verdana",16), bg='Navajo white').place(x=170, y=320)
    entry4=Entry(f2, show="*", textvariable=confpassword, width=70).place(x=450, y=325, width= 200)
    Dtl=Label(f2, text="Enter the marks of the student:", font=("verdana",18),bg = 'Navajo white').place(x=170,y=380)
    maths=Label(f2, text="Eng. Mathematics:", font=("verdana",16),bg = 'Navajo white').place(x=170,y=440)
    eone=Entry(f2, textvariable=m1, width=35).place(x= 450,y=445)
    physics=Label(f2, text="Eng. Physics:", font=("verdana",16),bg = 'Navajo white').place(x=170, y=500)
    etwo=Entry(f2, textvariable=m2, width=35).place(x= 450,y=505)
    elec=Label(f2, text="Basic Electrical Eng.:", font=("verdana",16),bg = 'Navajo white').place(x=170, y=560)
    ethree=Entry(f2, textvariable=m3, width=35).place(x= 450,y=565)
    mech=Label(f2, text="Engineering Mechanics:", font=("verdana",16),bg = 'Navajo white').place(x=170,y=620)
    efour=Entry(f2, textvariable=m4, width=35).place(x= 450,y=625)
    lang=Label(f2, text="Language Lab:", font=("verdana",16),bg = 'Navajo white').place(x=170, y=680)
    efive=Entry(f2, textvariable=m5, width=35).place(x= 450,y=685)


    Btn_Compute = Button(f2, text = 'COMPUTE', font = ('verdana',10,'bold'),width=10, command=Compute).place(x=750, y= 200)
    Btn_Save = Button(f2, text = 'SAVE', font = ('verdana',10,'bold'), width=10, command=Add).place(x=750, y= 300)
    Btn_Update = Button(f2, text = 'UPDATE', font = ('verdana',10,'bold'), width=10, command=Update).place(x=750, y= 400)
    Btn_Cancel = Button(f2, text = 'RESET', font = ('verdana',10,'bold'), width=10, command=reset).place(x=750, y= 500)
    Btn_Exit = Button(f2, text = 'EXIT', font = ('verdana',10,'bold'), width=10, command=Exit).place(x=750, y= 600)





    root.mainloop()

def final_result(r1,r2,r3,r4,r5,r6):
    wind=Tk()
    wind.title("GBU-Student Result")
    wind.resizable(0,0)
    wind.geometry("770x690")
    wind.configure(bg="Navajo white")


    def call_Login():
        wind.destroy()
        Log_in.main()

    f3 = LabelFrame(wind, width= 770, height=680, font=("verdana",22), bg = 'Navajo white')




    gt=DoubleVar(f3, r1)
    per=DoubleVar(f3, r2)
    cgpa=DoubleVar(f3, r3)
    grade=StringVar(f3, r4)
    div=StringVar(f3, r5)
    result=StringVar(f3, r6)



    res=Label(f3, text="Result", font=("verdana", 28), bg='Navajo white').place(x=280, y=50)
    l1=Label(f3, text="Grand Total:", font=("verdana", 22), bg='Navajo white').place(x=100, y=120)
    l2=Label(f3, text="Percentage:", font=("verdana", 22), bg='Navajo white').place(x=100, y=200)
    l3=Label(f3, text="cgpa:", font=("verdana", 22), bg='Navajo white').place(x=100, y=280)
    l4=Label(f3, text="grade:", font=("verdana", 22), bg='Navajo white').place(x=100,y=360)
    l5=Label(f3, text="Div.:", font=("verdana", 22), bg='Navajo white').place(x=100,y=440)
    l6=Label(f3, text="Result:", font=("verdana", 22), bg='Navajo white').place(x=100, y= 520)
    ent1=Entry(f3, textvariable=gt, state="readonly", width=35).place(x=300,y=130,height=28)
    ent2=Entry(f3, textvariable=per, state="readonly",width=35).place(x=300,y=210,height=28)
    ent3=Entry(f3, textvariable=cgpa, state="readonly",width=35).place(x=300,y=290,height=28)
    ent4=Entry(f3, textvariable=grade, state="readonly",width=35).place(x=300,y=370,height=28)
    ent5=Entry(f3, textvariable=div, state="readonly",width=35).place(x=300,y=450,height=28)
    ent6=Entry(f3, textvariable=result, state="readonly",width=35).place(x=300,y=530,height=28)



    Btn_signin = Button(f3 , text = 'LOGIN', font = ('verdana',10,'bold'), width = 10, command = call_Login).place(x=595,y=255)
    Btn_Exit = Button(f3, text = 'EXIT', font = ('verdana',10,'bold'), width = 10, command = wind.destroy).place(x=595,y=390)

    f3.pack()





conn.commit()





if __name__=="__main__":
    marksheet()