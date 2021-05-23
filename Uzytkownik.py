from tkinter import *
from Regulamin import Regulamin
import mysql.connector
from Lista import Lista
import tkinter.font as font

t = mysql.connector.connect(
  host="127.0.0.1",
  user="Michasx",
  password="abcabc123",
  database="Plyty"
)

mycursor = t.cursor()

class Uzytkownik:

    #def __init__(self, val=Tk()):
        #self.val = val

#Ustawienia Okna

    def k(self):
        self.val.title("Panel Uzytkownika")
        self.val.config(bg = "#1B1324")
        self.val.resizable(width=False, height=False)
        self.val.geometry('500x700')

#Tekst na stronie
    def l(self):

        self.Label_Number_1 = Label(self.val, text="Panel Uzytkownika", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.225, rely=0)

        self.text1 = "Tu będą się pojawiać informacje o nowych filmach :) "
        self.Label_Number_2 = Label(self.val, text=self.text1, fg="#8E7719", bg="#1B1324")
        self.Label_Number_2.config(font=("Courier", 10, "bold"))
        self.Label_Number_2.place(relx=0.09, rely=0.1)

        self.Button_Number_1 = Button(self.val, text="Wypożyczanie Płyt", padx=10, pady=10, fg="#8E7719", bg="#1B1324")
        self.Button_Number_1.place(relx=0.351, rely=0.2)

        self.Button_Number_2 = Button(self.val, text="Zwrot Płyt", padx=10, pady=10, fg="#8E7719", bg="#1B1324")
        self.Button_Number_2.place(relx=0.385, rely=0.3)

        self.Button_Number_3 = Button(self.val, text="Lista Płyt", padx=10, pady=10, fg="#8E7719", bg="#1B1324", command = self.List)
        self.Button_Number_3.place(relx=0.39, rely=0.4)


        self.Button_Number_4 = Button(self.val, text="Regulamin", padx=10, pady=10, fg="#8E7719", bg="#1B1324", command= self.WebPageRegulamin)
        self.Button_Number_4.place(relx=0.383, rely=0.9)

    def WebPageRegulamin(self):
        self.val.destroy()
        monitor2 = Regulamin()
        monitor2.parent = Tk()
        monitor2.a()
        monitor2.b()
        monitor2.c()

    def m(self):
        self.val.mainloop()

    def List(self):
        self.val.destroy()
        monitor6 = Lista()
        monitor6.zol = Tk()
        monitor6.v()
        monitor6.Enter()
        monitor6.z()
