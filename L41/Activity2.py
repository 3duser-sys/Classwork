from tkinter import *
from tkinter import messagebox
import time
progress_count = 0
window = Tk()
window.title('Tkinter Security')
window.geometry('4096x2160')

def msg():
    progress_count = 0
    i=1
    for i in range(100):
        i = i+1
        progress_count = f"{i}" + "%"
        progress.config(text=f"{progress_count}")
        time.sleep(0.1)
    messagebox.showwarning("Scan", "VIRUS DETECTED")
    label.config(text="TAKE ACTION.")

label = Label(window, text="No virus detected.")
label.place(x=600, y=40)
button = Button(window, text="Scan your pc.", command=msg)
button.place(x=600, y=80)
progress = Label(window, text=f"{progress_count}")
progress.place(x=600, y=120)


window.mainloop()