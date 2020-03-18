from tkinter import *
from functions import say_hello
window = Tk()
window.title("BinaryLife")
window.geometry('800x1200')     
lbl = Label(window)
lbl.grid(column=1, row=0)
def clicked():
    lbl.configure(text=say_hello())
btn = Button(window, text="Start", command=clicked)
btn.grid(column=0, row=0)
window.mainloop()