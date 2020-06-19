from tkinter import *
import random
import string

app = Tk()


def check():
    c1 = CheckVar1.get()
    c2 = CheckVar2.get()
    c3 = CheckVar3.get()
    return c1, c2, c3


def num():
    li = []
    nu = random.randint(1, 10)
    for i in range(nu):
        nu = random.randint(1, 10)
        li.append(str(nu))
    return li


def special_characters(pc):
    li = []
    nu = random.randint(1, 10)
    for i in range(nu):
        nu = pc[i]
        li.append(str(nu))
    return li


def both(pc, no):
    li = []
    a1 = random.randint(1, 10)
    a2 = random.randint(1, 10)
    a3 = random.choices(pc, k=a1)
    a4 = random.choices(no, k=a2)
    li.extend(a3)
    li.extend(a4)
    return li


def generate():
    punctuation = list(string.punctuation)
    c1, c2, c3 = check()
    if c1:
        li = num()
    elif c2:
        li = special_characters(punctuation)
    elif c3 == True:
        li = both(punctuation, num())

    p = e1.get()
    p = p.replace(" ", "")
    p = list(p)
    p.extend(li)
    random.shuffle(p)
    p = "".join(p)
    print(p)


def clear():
    e1.delete(0, END)
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()


def clear2():
    cb1.config(state=DISABLED)
    cb2.config(state=DISABLED)
    cb1.deselect()
    cb2.deselect()


def selected():
    c1, c2, c3 = check()
    if c1 == True and c2 == True:
        cb3.select()
        clear2()


def refresh():
    cb1.config(state=NORMAL)
    cb2.config(state=NORMAL)
    cb3.deselect()
    e1.delete(0, END)


l1 = Label(app, text='Random Password Generator').grid(row=0, column=0)
e1 = Entry(app)
l2 = Label(app, text="Number")
b1 = Button(app, text="Submit", command=generate)
b2 = Button(app, text="Clear All", command=clear)
b3 = Button(app, text='RESET', command=refresh)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
cb1 = Checkbutton(app, text="Include Numbers", variable=CheckVar1, command=selected)
cb2 = Checkbutton(app, text="Include Special Characters", variable=CheckVar2, command=selected)
cb3 = Checkbutton(app, text="Include Both", variable=CheckVar3, command=clear2)
e1.grid(row=1, column=0)
cb1.grid(row=2, column=0)
cb2.grid(row=3, column=0)
cb3.grid(row=4, column=0)
b1.grid(row=5, column=0, sticky=N)
b3.grid(row=5, column=1, sticky=W)
b2.grid(row=5, column=2, sticky=E)

app.mainloop()
