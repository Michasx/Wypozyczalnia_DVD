from tkinter import *
class Regulamin:

    #def __init__(self, parent=Tk()):
        #self.parent = parent


#Ustawienia Okna

    def a(self):
        self.parent.title("Regulamin")
        self.parent.config(bg = "#1B1324")
        self.parent.resizable(width=False, height=False)
        self.parent.geometry('500x700')

#Tekst na stronie
    def b(self):

        self.Label_Number_1 = Label(self.parent, text="Regulamin", fg="#8E7719", bg="#1B1324")
        self.Label_Number_1.config(font=("Courier", 20, "bold"))
        self.Label_Number_1.place(relx=0.3, rely=0)

        self.text1 = "Tu będzie regulamin"
        self.Label_Number_2 = Label(self.parent, text=self.text1, fg="#8E7719", bg="#1B1324")
        self.Label_Number_2.config(font=("Courier", 10, "bold"))
        self.Label_Number_2.place(relx=0.06, rely=0.1)

    def c(self):
        self.parent.mainloop()



