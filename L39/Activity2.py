from tkinter import *
from datetime import date
window = Tk()
darkblue = "#072F5F"
lightblue = "#3895D3"

window.title('Gettign started with widgets')
window.geometry('400x300')
dalabel = Label(text="Alright!", fg="white", bg=darkblue, height=1, width = 300)
name_lbl = Label(text="Enter your Full Name", bg=lightblue)
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the tkinter test demo! DA Date is:"
    greeting = "Hallo there "+name+"\n"
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#1261A0",fg = "white")

dalabel.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()
