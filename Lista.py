from tkinter import *
import mysql.connector
import tkinter.font as font

t = mysql.connector.connect(
  host="127.0.0.1",
  user="Michasx",
  password="abcabc123",
  database="Plyty"
)

c = t.cursor()
c.execute("SELECT * FROM plyty")

class Lista:

    #def __init__(self, zol=Tk()):
        #self.zol = zol

    def v(self):
        self.zol.title("Lista Płyt")
        self.zol.config(bg="#1B1324")
        self.zol.resizable(width=False, height=False)

    def Enter(self):
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(self.zol, width=20, fg='black', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

    def z(self):
        self.zol.mainloop()

lst = []
templist = c.fetchall()
my_columns = 0
for row in templist:
    lst.append(row)
    my_columns += 1

total_rows = len(lst)
total_columns = len(lst[0])

