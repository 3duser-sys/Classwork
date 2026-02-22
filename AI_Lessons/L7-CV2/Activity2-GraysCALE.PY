import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Image Viewer")
img = cv2.imread('creator-pro.gif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray, (224, 224))
frame = tk.Frame(root)

def save():
    cv2.imwrite('saved_image.gif', resized)
    messagebox.showinfo("Saved", "Image saved as 'saved_image.jpg'")

def quit_app():
    root.destroy()


tk_img = ImageTk.PhotoImage(Image.fromarray(resized))
label = tk.Label(root, image=tk_img)
save_btn = tk.Button(frame, text="Save", command=save, bg="green", fg="white", width=10)
quit_btn = tk.Button(frame, text="Quit", command=quit_app, bg="red", fg="white", width=10)
label.pack()
frame.pack(pady=10)
save_btn.pack(side="left", padx=10)
quit_btn.pack(side="right", padx=10)



root.mainloop()

print(f"Image size: {resized.shape}")
