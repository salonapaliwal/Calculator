from tkinter import *
from tkinter import messagebox

root=Tk()

val=""
A=0
operator=""
def btn_1_isClicked():
    global val
    val=val+"1"
    data.set(val)
def btn_2_isClicked():
    global val
    val=val+"2"
    data.set(val)
def btn_3_isClicked():
    global val
    val=val+"3"
    data.set(val)
def btn_4_isClicked():
    global val
    val=val+"4"
    data.set(val)
def btn_5_isClicked():
    global val
    val=val+"5"
    data.set(val)
def btn_6_isClicked():
    global val
    val=val+"6"
    data.set(val)
def btn_7_isClicked():
    global val
    val=val+"7"
    data.set(val)
def btn_8_isClicked():
    global val
    val=val+"8"
    data.set(val)
def btn_9_isClicked():
    global val
    val=val+"9"
    data.set(val)
def btn_0_isClicked():
    global val
    val=val+"0"
    data.set(val)
def btn_plus_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="+"
    val=val + "+"
    data.set(val)
def btn_minus_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="-"
    val=val + "-"
    data.set(val)
def btn_mult_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="*"
    val=val + "*"
    data.set(val)
def btn_div_clicked():
    global A
    global operator
    global val
    A=float(val)
    operator="/"
    val=val + "/"
    data.set(val)
def c_clicked():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)
def result_isclicked():
    global A
    global operator
    global val
    val2=val
    if operator == "+":
        x=float((val2.split("+")[1]))
        C = A + x#bcoz A already contains int of val
        data.set(C)
        val=str(C)#to take cont inputs such as after doing 3+2=5 then 5-4
    elif operator=="-":
        x = float((val2.split('-')[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator=="*":
        x = float((val2.split('*')[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator=="/":
        x = float((val2.split('/')[1]))
        if x==0:
            messagebox.showerror("Error","Division by 0 not supported")
            A=""
            val=""
            data.set(val)
        else:
            C= float(A/x)
            data.set(C)
            val=str(C)







root.title("Calculator")#to give title to the GUI
#operator="" to hold on the input
root.geometry("250x400+300+300")
#root.resizable(0,0)#to resize the calculator (0,0) means not able to resize


data=StringVar()#where we will take the input


lbl=Label(root,text="Label",anchor=SE,font=("Verdana",20),textvariable=data,background="#ffffff",fg="#000000")# input part
lbl.pack(expand=True,fill="both")

btnrow1=Frame(root)                         #buttons
btnrow1.pack(expand=True,fill="both")

btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both")




btn1=Button(btnrow1,text="1",font=("Verdana",22),relief=GROOVE,border=0,command=btn_1_isClicked,)#relief=GROOVE-to remove the border lines and spaces,border=0#
btn1.pack(side=LEFT,expand=True,fill="both")

btn2=Button(btnrow1,text="2",font=("Verdana",22),relief=GROOVE,border=0,command=btn_2_isClicked,)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3=Button(btnrow1,text="3",font=("Verdana",22),relief=GROOVE,border=0,command=btn_3_isClicked,)
btn3.pack(side=LEFT,expand=True,fill="both")

btn4=Button(btnrow1,text="+",font=("Verdana",22),relief=GROOVE,border=0,command=btn_plus_clicked,)
btn4.pack(side=LEFT,expand=True,fill="both")




btn5=Button(btnrow2,text="4",font=("Verdana",22),relief=GROOVE,border=0,command=btn_4_isClicked,)
btn5.pack(side=LEFT,expand=True,fill="both")

btn6=Button(btnrow2,text="5",font=("Verdana",22),relief=GROOVE,border=0,command=btn_5_isClicked,)
btn6.pack(side=LEFT,expand=True,fill="both")

btn7=Button(btnrow2,text="6",font=("Verdana",22),relief=GROOVE,border=0,command=btn_6_isClicked,)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8=Button(btnrow2,text="-",font=("Verdana",22),relief=GROOVE,border=0,command=btn_minus_clicked,)
btn8.pack(side=LEFT,expand=True,fill="both")



btn9=Button(btnrow3,text="7",font=("Verdana",22),relief=GROOVE,border=0,command=btn_7_isClicked,)
btn9.pack(side=LEFT,expand=True,fill="both")

btn10=Button(btnrow3,text="8",font=("Verdana",22),relief=GROOVE,border=0,command=btn_8_isClicked,)
btn10.pack(side=LEFT,expand=True,fill="both")

btn11=Button(btnrow3,text="9",font=("Verdana",22),relief=GROOVE,border=0,command=btn_9_isClicked,)
btn11.pack(side=LEFT,expand=True,fill="both")

btn12=Button(btnrow3,text="*",font=("Verdana",22),relief=GROOVE,border=0,command=btn_mult_clicked,)
btn12.pack(side=LEFT,expand=True,fill="both")


btn9=Button(btnrow4,text="C",font=("Verdana",22),relief=GROOVE,border=0,command=c_clicked,)
btn9.pack(side=LEFT,expand=True,fill="both")

btn10=Button(btnrow4,text="0",font=("Verdana",22),relief=GROOVE,border=0,command=btn_0_isClicked,)
btn10.pack(side=LEFT,expand=True,fill="both")

btn11=Button(btnrow4,text="=",font=("Verdana",22),relief=GROOVE,border=0,command=result_isclicked,)
btn11.pack(side=LEFT,expand=True,fill="both")

btn12=Button(btnrow4,text="/",font=("Verdana",22),relief=GROOVE,border=0,command=btn_div_clicked)
btn12.pack(side=LEFT,expand=True,fill="both")


root.mainloop()