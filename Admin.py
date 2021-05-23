from tkinter import *
from Dodawanie import Dodawanie
from Lista import Lista
import tkinter.font as font

class Admin:

    #test
    #def __init__(self, val=Tk()):
        #self.val = val

#Ustawienia Okna

    def h(self):
        self.mati.title("Panel Administratora")
        self.mati.config(bg = "#1B1324")
        self.mati.resizable(width=False, height=False)
        self.mati.geometry('500x700')

#Tekst na stronie
    def i(self):

        self.Label_Number_1 = Label(self.mati, text="Panel Administratora", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.178, rely=0)

        self.Button_Number_1 = Button(self.mati, text="Dodawanie Płyt", padx=10, pady=10, fg="#8E7719", bg="#1B1324", command = self.NewPageWypozycz)
        self.Button_Number_1.place(relx=0.351, rely=0.2)

        self.Button_Number_2 = Button(self.mati, text="Usuwanie Płyt", padx=10, pady=10, fg="#8E7719", bg="#1B1324", command = self.Delete)
        self.Button_Number_2.place(relx=0.356, rely=0.3)

        self.Button_Number_3 = Button(self.mati, text="Lista Płyt", padx=10, pady=10, fg="#8E7719", bg="#1B1324", command = self.List)
        self.Button_Number_3.place(relx=0.38, rely=0.4)

    def j(self):
        self.mati.mainloop()

    def NewPageWypozycz(self):
        self.mati.destroy()
        monitor2 = Dodawanie()
        monitor2.va = Tk()
        monitor2.p()
        monitor2.o()
        monitor2.y()

    def Add(self):
        pass

    def List(self):
        self.mati.destroy()
        monitor6 = Lista()
        monitor6.zol = Tk()
        monitor6.v()
        monitor6.Enter()
        monitor6.z()

    def Delete(self):
        pass