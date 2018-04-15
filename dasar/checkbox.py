from tkinter import *
from tkinter.ttk import *

top = Tk() 
top.title("Welcome to GUI sas")

#---menambah geometri windows-------
top.geometry('350x200')

chk_state = BooleanVar()
chk_state.set(True) #set check state

chk = Checkbutton(top, text = 'TI.17.B3', var=chk_state)

chk.grid(column=0, row=0)

top.mainloop()
