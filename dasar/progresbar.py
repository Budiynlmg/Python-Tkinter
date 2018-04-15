from tkinter import *
from tkinter.ttk import Progressbar 
from tkinter import ttk
 
top = Tk() 
top.title("Welcome to GUI sas")
top.geometry('350x200')
 
style = ttk.Style() 
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='blue')
bar = Progressbar(top, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=0)
 
top.mainloop()
