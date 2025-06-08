from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Resizable Button Example")
        self.geometry("800x600")
        self.btn = CTkButton(self, text="Кнопка", width=30, height=30)
        self.btn.place(x=0, y=0)
        

def button_adaptive():
    window_width = win.winfo_width()
    btn.config(width=window_width // 10)
    self.after(50, button_adaptive)
    self.btn.place(x = self.winfo_width() - self.btn.winfo_wigth(), y = self.winfo_height() - self.btn.winfo_height())

    self.after(10, self.button_adaptive)


btn = CTkButton(win, text="Кнопка", width=300, height=100)
btn.place(x=50, y=40)

win = MainWindow()
win.after(50, button_adaptive)
win.mainloop()