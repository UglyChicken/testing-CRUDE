from tkinter import *
from tkinter import messagebox

def display_name():
    name = "Succesfull  " + e1.get () + " " + e2.get () + "!"
    messagebox.showinfo("Dialog Box", name)

pota = Tk()
Label (pota, text='Employee Name').grid(row=0, padx=20, pady=10)
Label (pota, text='Department').grid(row=1, padx=20, pady=10)
Label (pota, text='Position').grid (row=2, padx=20, pady=10)
Label (pota, text='Employee Rate').grid (row=3, padx=20, pady=10)
e1 = Entry (pota)
e2 = Entry (pota)
e3 = Entry (pota)
e4 = Entry (pota)
e1.grid (row=0, column=1, padx=20, pady=10)
e2.grid (row=1, column=1, padx=20, pady=10)
e3.grid (row=2, column=1, padx=20, pady=10)
e4.grid (row=3, column=1, padx=20, pady=10)

b1 = Button (pota, text="Enter", command=display_name)
b1.grid (row=5, column=2, padx=20, pady=10)
mainloop () 
