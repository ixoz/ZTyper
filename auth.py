import tkinter as tk
from tkinter import messagebox
from database import Database
from ztyper import ZTyper
from dashboard import Dashboard

class AuthWindow:
    def __init__(self):
        self.db = Database()
        self.root = tk.Tk()
        self.root.title("Login/Register")
        self.root.geometry("400x300")
        self.root.configure(bg="#264653")

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        tk.Label(self.root, text="ZTyper", font="Arial 24 bold", bg="#264653", fg="#FFC300").pack(pady=20)

        tk.Label(self.root, text="Username", bg="#264653", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password", bg="#264653", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(self.root, text="Register", command=self.register)
        self.register_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.db.get_user(username, password)
        if user:
            self.root.destroy()
            Dashboard(user_id=user[0])
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.db.create_user(username, password)
        messagebox.showinfo("Success", "User registered successfully")

if __name__ == "__main__":
    AuthWindow()
