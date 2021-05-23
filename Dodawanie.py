from tkinter import *
from Regulamin import Regulamin
import mysql.connector
import sqlite3
import tkinter.font as font

t = mysql.connector.connect(
  host="127.0.0.1",
  user="Michasx",
  password="abcabc123",
  database="Plyty"
)

mycursor = t.cursor()

class Dodawanie:

    def p(self):
        self.va.title("Panel Uzytkownika")
        self.va.config(bg = "#1B1324")
        self.va.resizable(width=False, height=False)
        self.va.geometry('500x700')

    def o(self):

        self.Label_Number_1 = Label(self.va, text="Dodaj Płytę", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.225, rely=0)

        self.text1 = Label(self.va, text="Podaj Nazwę Płyty:",fg="#8E7719", bg="#1B1324")
        self.text1.config(font=("Courier", 14, "bold"))
        self.text1.place(relx=0, rely=0.05)
        self.get_1 = Entry(self.va, bg="white")
        self.get_1.place(relx=0.5, rely = 0.066)
        self.text2 = Label(self.va, text="Podaj Czas Trwania:",fg="#8E7719", bg="#1B1324")
        self.text2.config(font=("Courier", 14, "bold"))
        self.text2.place(relx=0, rely=0.09)
        self.get_2 = Entry(self.va, bg="white")
        self.get_2.place(relx=0.5, rely = 0.095)
        self.text3 = Label(self.va, text="Podaj Nazwę Wytwórni:",fg="#8E7719", bg="#1B1324")
        self.text3.config(font=("Courier", 14, "bold"))
        self.text3.place(relx=0, rely=0.12)
        self.get_3 = Entry(self.va, bg="white")
        self.get_3.place(relx=0.5, rely = 0.125)
        self.button_accept1 = Button(self.va, text="Accept", fg="black", padx=80, pady=5, command=self.Add)
        self.button_accept1.place(relx=0.219, rely=0.17)

    def y(self):
        self.va.mainloop()

    def Add(self):
        sql = "INSERT INTO plyty (Nazwa, Czas, Wytwornia) VALUES (%s, %s, %s)"
        val = (str(self.get_1.get()), str(self.get_2.get()), str(self.get_3.get()))
        mycursor.execute(sql, val)
        t.commit()
        print(self.get_1,self.get_2,self.get_3)

    def List(self):
        print("UwU")

    def Delete(self):
        pass