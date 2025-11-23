from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg = "#d0efff" )

labels1 = Label(frame, text = "Full name", bg = "#3895D3", fg = "white", width = 12)
labels2 = Label(frame, text = "Email", bg = "#3895D3", fg = "white", width = 12)
labels3 = Label(frame, text = "Password", bg = "#3895D3", fg = "white", width = 12)

name_ent = Entry(frame)
email_ent = Entry(frame)
pass_ent = Entry(frame, show ="*")

def display():
    name = name_ent.get()
    greet = "Hey "+name
    message = "\n Congrats for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    ndbtn.place(x=130,y=350)

def Yesa():
    message2 = "\n\n\n\n Lets head off to your information page!"
    textbox.insert(END, message2)
    

textbox = Text(bg = "#d0efff", fg = "black" )
btn = Button(text = "Create Account,", command=display, bg="red")
ndbtn = Button(text= "Lets proceed:", command=Yesa, bg="#3895D3")

frame.place(x=20,y=0)
labels1.place(x=20, y=20)
name_ent.place(x=150, y=20)
labels2.place(x=20, y=80)
email_ent.place(x=150, y=80)
labels3.place(x=20, y=140)
pass_ent.place(x=150, y=140)
textbox.place(y=250)
btn.place(x=130, y=210)

root.mainloop()