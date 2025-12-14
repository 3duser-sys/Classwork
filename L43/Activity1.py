import tkinter
from tkinter import *
counter=0

root = Tk()
root.geometry("400x300")
root.title("main")

def top_win():
    couter = counter
    couter=couter+1
    top = Toplevel()
    top.geometry("180x100")
    top.title("Im your " + couter +  "window!")
    lbl2 = Label(top, text = "This is toplevel window")
    lbl2.pack()

    top.mainloop()

l = Label(root, text="this is your first")
btn = Button(root, text ="click here to open anodda window.", command=top_win)
l.pack()
btn.pack()
root.mainloop()