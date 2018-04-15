from tkinter import *
from tkinter import scrolledtext
 
top = Tk()
top.title("Welcome to GUI sas")
top.geometry('350x200')

#membuat text area 
txt = scrolledtext.ScrolledText(top,width=40,height=10)
txt.grid(column=0,row=0)
 
top.mainloop()
