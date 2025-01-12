import tkinter as tk
import tkinter.messagebox
import tkinter.font


class MyGui:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Okno wyboru")
        self.main_window.geometry("400x400")
        self.canvas = tk.Canvas(self.main_window, width=200, height=200)
        myFont = tk.font.Font(family='Helvetica', size=18, weight='bold')
        self.canvas.create_text(100, 100, text="Testowy", anchor=tkinter.SW, font=myFont)

        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.cb_var = tk.IntVar()
        self.cb_var.set(0)

        self.rb1 = tk.Radiobutton(self.top_frame, text="Opcja 1", variable=self.radio_var, value=1)
        self.rb2 = tk.Radiobutton(self.top_frame, text="Opcja 2", variable=self.radio_var, value=2)
        self.rb3 = tk.Radiobutton(self.top_frame, text="Opcja 3", variable=self.radio_var, value=3)
        self.rb4 = tk.Checkbutton(self.top_frame, text="Opcja 4", variable=self.cb_var)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()

        self.ok_button = tk.Button(self.bottom_frame, text="OK", command=self.show_choice)

        self.ok_button.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.canvas.pack()

        tk.mainloop()

    def show_choice(self):
        tk.messagebox.showinfo("Wybór", "wybrałeś opcję: " + str(self.radio_var.get()))
        if self.cb_var.get() == 1:
            tk.messagebox.showinfo("Wybór", "Zaznaczyleś kwadracik")


gui = MyGui()
