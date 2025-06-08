from customtkinter import *

window = CTk()
window.geometry("400x300")
window.title("")
window.configure(fg_color = "black", )
#window.iconbitmap()
textbox = CTkTextbox(window, width = 1000, height = 800)
textbox.pack(pady=20)


window.mainloop()
