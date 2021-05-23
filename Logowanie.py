from tkinter import *
from Admin import Admin
password = 'abc'

class Logowanie:

    #def __init__(self, root=Tk()):
        #self.parent = root

#Ustawienia Okna

    def d(self):
        self.stec.title("Logowanie")
        self.stec.config(bg = "#1B1324")
        self.stec.resizable(width=False, height=False)
        self.stec.geometry('200x200')

        self.text1 = Label(self.stec, text="Wpisz Hasło: ", fg="#8E7719", bg="#1B1324")
        self.text1.config(font=("Courier", 10, "bold"))
        self.text1.place(relx=0.230,rely=0)
        self.get_password = Entry(self.stec, bg="white")
        self.get_password.place(relx=0.230, rely=0.13)
        self.button_accept1 = Button(self.stec, text="Zaakceptuj", fg="black", padx=80, pady=5, command=self.g)
        self.button_accept1.place(relx=0, rely=0.25)

#Tekst na stronie
    def e(self):

        self.Label_Number_1 = Label(self.stec, text="Logowanie", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0, rely=2)

        self.text1 = "Zaloguj się"
        self.Label_Number_2 = Label(self.stec, text=self.text1, fg="#8E7719", bg="#1B1324")
        self.Label_Number_2.config(font=("Courier", 10, "bold"))
        self.Label_Number_2.place(relx=0, rely=2)

    def f(self):
        self.stec.mainloop()

    def g(self):
        if self.get_password.get() == password:
            self.button_accept1['text'] = "Poprawne!"
            self.stec.destroy()
            monitor4 = Admin()
            monitor4.mati = Tk()
            monitor4.h()
            monitor4.i()
            monitor4.j()
        else:
            self.button_accept1['text'] = "Niepoprawne!"
