import tkinter
top = tkinter.Tk() 
top.title("Welcome to GUI sas")

#---menambah geometri windows-------
top.geometry('350x200')

#membuat label
lbl = tkinter.Label(top, text = "ini label")
lbl.grid(column=0, row=0)

#membuat text box
txt = tkinter.Entry(top, width=10)
txt.grid(column=1, row=0)

def clicked():
    tes = "welcome to " + txt.get()
    lbl.configure(text=tes)

#membuat button
btn = tkinter.Button(top, text="Click", command=clicked)
#--memberi warna pada button---
#btn = tkinter.Button(top, text="Click", bg="orange", fg="red")
btn.grid(column=2, row=0)

top.mainloop()
