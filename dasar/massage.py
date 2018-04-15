from tkinter import *
from tkinter import messagebox
 
top = Tk()
 
top.title("Welcome to GUI sas") 
top.geometry('350x200')
 
def clicked():
    messagebox.showinfo('Message title', 'pesan berhasil')
 
btn = Button(top,text='Click', command=clicked)
btn.grid(column=0,row=0)
 
top.mainloop()
