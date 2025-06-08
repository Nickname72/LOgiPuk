from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")

        self.frame = CTkFrame(self, width=400, height = self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width = 0)

        self.frame.place(x = 0, y = 0)
        self.is_show_menu = False
        self.frame_width = 0

        self.label = CTkLabel(self.frame, text="Введіть налаштування")
        self.label.pack(pady=30)
        self.entry = CTkEntry(self.frame)
        self.entry.pack()

        

        self.btn = CTkButton(self, text="menu", command=self.togle_show_menu, width=30)
        self.btn.place(x=0, y=0)
        
    def togle_show_menu(self):
        if self.is_show_menu:
            self.frame.place_forget()
            self.is_show_menu = False
            self.speed_anim_menu *= -1
            self.btn.configure(text=">")
            self.show_menu()
        else:
            self.is_show_menu = True
            self.speed_anim_menu *= -1
            self.btn.configure(text="<")
            self.show_menu()

            self.label = CTkLabel(self.menu_frame, text="Ім'я:", font=("Arial", 20))
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack(pady=10)

    def show_menu(self):
        self.menu_frame.configure(width = self.menu_frame.winfo_width() + self.speed_anim_menu)
        if not self.menu_frame.winfo_width() >= 200 and  self.is_show:
            self.after(10, self.show_menu)
        elif self.menu_frame.winfo_width() >= 40 and not self.is_show:
            self.after(10, self.show_menu)
            if self.label and self.entry:
                self.lable.destroy()
                self.entry.destroy()

    def add_message(self, message):
        self.chat_field.configure(state="normal")
        self.chat_field.insert(END, " Я: " + message + "\n")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.add_message(f"{self.username}: {message}")
            data = f"TEXT@{self.username}@{message}\n"
            try:
                self.socket.sendall(data.encode())
            except:
                pass
        self.message_entry.delete(0, END)

    def recv_message(self):
        buffer = ""
        while True:
            try:
                chunk = self.socket.recv(4).decode()
                if not chunk:
                    break
                buffer += chunk
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    self.handle_line(line.strip())
            except:
                break
        self.socket.close()
    def handle_line(self, line):
        if not line:
            return
        parts = line.split("@",3)
        msg_type = parts[0]
        if msg_type == "TEXT":
            if len(parts) >= 3:
                author = parts[1]
                message = parts[2]
                self.add_message(f"{author}: {message}")
        elif msg_type == "IMAGE":
            if len(parts) >= 3:
                author = parts[1]
                filename = parts[2]
                self.add_massage(f"{author} надіслав зображення: {filename}")
        else:
            self.add_message(line)