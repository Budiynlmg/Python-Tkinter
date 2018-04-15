from tkinter import *
from tkinter.ttk import *

top = Tk() 
top.title("Welcome to GUI sas")

#---menambah geometri windows-------
top.geometry('350x200')

combo = Combobox(top)
combo['values'] = (1,2,3,4,5, "Text")
combo.current(1)
combo.grid(column=0, row=0)

top.mainloop()
