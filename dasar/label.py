import tkinter
top = tkinter.Tk() 
top.title("Welcome to GUI sas")

#membuat label
lbl = tkinter.Label(top, text = "ini label")

#----merubah font----
#lbl = tkinter.Label(top, text="ini label", font=("Arial Bold", 50))

#---menambah geometri windows-------
#top.geometry('350x200')

lbl.grid(column=10, row=1)
top.mainloop()

