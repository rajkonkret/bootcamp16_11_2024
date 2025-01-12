import tkinter


# tkinter - biblioteka do działania z okienkami

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()  # tworzenie okienka

        self.label1 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label2 = tkinter.Label(self.main_window, text="Python")
        self.label3 = tkinter.Label(self.main_window, text="góra")
        self.label4 = tkinter.Label(self.main_window, text="dół")

        self.label1.pack(side='left')
        self.label2.pack(side='right')
        self.label3.pack(side='top')
        self.label4.pack(side=tkinter.BOTTOM)

        tkinter.mainloop()
        # right, top, bottom


my_gui = MyGui()
# pyinstaller.exe --onefile --noconsole .\okno1.py
