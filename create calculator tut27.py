from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x800")
root.title("Calculator")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1 = Frame(root,bg="blue")
f1.pack()
b = Button(f1,text="9",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="8",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="7",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
f1 = Frame(root,bg="blue")
f1.pack()
b = Button(f1,text="6",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="5",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="4",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
f1 = Frame(root,bg="blue")
f1.pack()
b = Button(f1,text="3",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="2",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="1",padx=28,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
f1 = Frame(root,bg="blue")
f1.pack()
b = Button(f1,text="0",padx=30,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="-",padx=30,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="+",padx=30,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
f1 = Frame(root,bg="blue")
f1.pack()
b = Button(f1,text="/",padx=31,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="=",padx=31,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)
b = Button(f1,text="*",padx=31,pady=18,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=18,pady=5)

root.mainloop()