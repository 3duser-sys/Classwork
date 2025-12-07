#Simple Text Editor.

from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfile, asksaveasfile, asksaveasfilename

window =Tk()
window.title("Doodle Docs - New TextDoc")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight = 1)
window.columnconfigure(1, minsize=800, weight = 1)

def open_a_file():
    #Open a file that user rlly wants to edit.
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    #file is opened, display da content o the file:
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Doodle Docs - {filepath}")

def save_a_file():
    filepath = asksaveasfilename(defaultextension = ".txt", filetypes = [("Text files", "*.txt"), 
    ("Python", "*.py"), ("C", "*.c"), ("C header", "*.h"), ("C++", "*.cpp"), ("Java", "*.Java"), ("Html", "*.html"), ("JSON", "*.JSON")], )

    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Doodle Docs - {filepath}")

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd = 2)
openbtn = Button(fr_buttons, text = "Open Doc",command=open_a_file)
savebtn = Button(fr_buttons, text = "Save as...",command=save_a_file)

openbtn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
savebtn.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0,column=1, sticky="nsew")

window.mainloop()