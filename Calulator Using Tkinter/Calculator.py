from tkinter import *


window = Tk()
window.geometry('500x500')

math = None     # Initialize global variables
i = 0

e = Entry(window, width=56,borderwidth=5)
e.place(x=0,y=0)

def click(num):     #funtion for display numbers  when click button
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

buttons = [
    ('1',10,60), ('2',80,60), ('3',170,60),
    ('4',10,120), ('5',80,120), ('6',170,120),
    ('7',10,180), ('8',80,180), ('9',170,180),
    ('0',10,240)
]

for (text, x, y) in buttons:
    Button(window, text=text, width=12,command=lambda t=text: click(t)).place(x=x, y=y)

# OPERATORS
def add():
    n1 = e.get()
    if n1 == "":
        return
    global math
    math ="addition"
    global i
    i =float(n1)
    e.delete(0,END)

b = Button(window,text='+',width=12,command= add)
b.place(x=80,y=240)

def sub():
    n1 = e.get()
    if n1 == "":
        return
    global math
    math = "substraction"
    global i
    i =float(n1)
    e.delete(0,END)

b = Button(window,text='-',width=12,command= sub)
b.place(x=170,y=240)

def mult():
    n1 = e.get()
    if n1 == "":
        return
    global math
    math = "multiplication"
    global i
    i =float(n1)
    e.delete(0,END)

b = Button(window,text='*',width=12,command= mult)
b.place(x=10,y=300)

def div():
    n1 = e.get()
    if n1 == "":
        return
    global math
    math = "division"
    global i
    i =float(n1)
    e.delete(0,END)

b = Button(window,text='/',width=12,command= div)
b.place(x=80,y=300)

def equal():
    n2 = e.get()
    if n2 =="" or math == None:
        return

    e.delete(0,END)
    if math == "addition":
        e.insert(0, i + float(n2))
    elif math == "substraction":
        e.insert(0, i - float(n2))
    elif math == "multiplication":
        e.insert(0, i * float(n2))
    elif math == "division":
        if float(n2) == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, i / float(n2))
    
b = Button(window,text='=',width=12,command=equal)
b.place(x=170,y=300)

def clear():
    e.delete(0, END)

b = Button(window,text='Clear',width=12,command= clear)
b.place(x=10,y=350)

mainloop()