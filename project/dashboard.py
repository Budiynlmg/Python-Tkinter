from tkinter import *
import tkinter

class dashboard:
    def __init__(self, induk, title):
        self.induk = induk
        self.aturWindow(title)         
        self.aturKomponen() 
        

    def aturWindow(self, title):
        lebar = 400
        tinggi = 150
        setTengahX = (self.induk.winfo_screenwidth()-lebar)/2
        setTengahY = (self.induk.winfo_screenheight()-tinggi)/2
        self.induk.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        self.induk.title(title)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)

    def aturKomponen(self):
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
         
        # atur frame data
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)
         
        # atur lABEL
        Label(frData, text='MENU PILIHAN',fg="blue", font=("Arial Bold", 30)).grid(row=0, column=1, sticky=W)
        
         
        # atur frame tombol
        frTombol = Frame(frameUtama, bd=6)
        frTombol.pack(fill=BOTH, expand=YES)
         
        # atur tombol login
        self.btnCal = Button(frTombol, text='Calculator', command=self.calculator)
        self.btnCal.pack(side=LEFT, fill=BOTH, expand=YES)
        
        self.btnStopwatch = Button(frTombol, text='Stopwatch', command=self.stwatch)
        self.btnStopwatch.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnCrud = Button(frTombol, text='CRUD', command=self.mhs)
        self.btnCrud.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnCrud = Button(frTombol, text='Media', command=self.med)
        self.btnCrud.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnClose = Button(frTombol, text='Close', command=self.Tutup)
        self.btnClose.pack(side=RIGHT, fill=BOTH, expand=YES)

    def Tutup(self, event=None):
        self.induk.destroy()

    def calculator(self, event=None):
        self.induk.destroy()
        if self.induk.destroy:
            import kalkulator
            

    def stwatch(self, event=None):
        self.induk.destroy()
        if self.induk.destroy:
            import stopwatch
            

    def mhs(self, event=None):
        self.induk.destroy()
        if self.induk.destroy:
            import mahasiswa

    def med(self, event=None):
        self.induk.destroy()
        if self.induk.destroy:
            import media
            
        
def main ():
    root = Tk()
    root.configure(bg="#526060")
    root.overrideredirect(True)
    app = dashboard(root, "Dashboard")
    root.mainloop()

main()
