from tkinter import *



class Main:
    def __init__(self):
        self.pack = None



    pass


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#222", foreground="#FFF")
        self.lbl.place(x=11, y=50)

    btns = [
        "1", "2", "3", "/",
        "4", "5", "6", "*",
        "7", "8", "9", "+",
        " ", "0", "=", "-",
        "треугS=a*b","кругS=a*b/2",
        "квадS=a×a=a2","трапS=a+b/2*h",
        "пр.угл треугS=1/2(a×h)",
        "пр.углS=a×√(d2-а2)","ра.треуг S=a*b/2",
        "ра.трапS=a+b/2Vc2-(a+b)2/4",





    ]

    x = 10
    y = 140
    for bt in btns:
        com = lambda x=bt: self.logicalc(x)
        Button(text=bt, bg="#FFF",
               font=("Times New Roman", 15),
               command=com).place(x=x, y=y,
                                  width=115,
                                  height=79)
        x += 117
        if x > 400:
            x = 10
            y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "=":
            self.formula = str(eval(self.formula))

        else:
            if self.formula == "0":
                self.formula = ""
            self.formula = ""
        self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

    if __name__ == '__main__':
        root = Tk()
        root["bg"] = "#000"
        root.geometry("700x750+200+200")
        root.title("Калькулятор")
        root.resizable(False, False)
        app = Main()
        app.pack
        root.mainloop()
