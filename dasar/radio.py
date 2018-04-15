from tkinter import * 
from tkinter.ttk import *
 
top = Tk()
 
top.title("Welcome to GUI sas")
top.geometry('350x200')
 
rad1 = Radiobutton(top,text='First', value=1)
rad2 = Radiobutton(top,text='Second', value=2)
rad3 = Radiobutton(top,text='Third', value=3)
 
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
 
top.mainloop()
