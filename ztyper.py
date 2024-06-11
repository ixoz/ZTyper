import tkinter as tk
from tkinter import messagebox
from ztyper import ZTyper
from database import Database

class UpdateDetailsWindow:
    def __init__(self, user_id):
        self.user_id = user_id

        self.window = tk.Toplevel()
        self.window.title("Update Details")
        self.window.geometry("400x300")
        self.window.configure(bg="#264653")

        self.db = Database()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.window, text="Update Details", bg="#264653", fg="#FFC300", font="Arial 24 bold")
        title_label.pack(pady=(20, 10))

        self.new_username_entry = tk.Entry(self.window, font="Arial 14", bg="white", fg="black", bd=2)
        self.new_username_entry.insert(0, self.db.get_user_by_id(self.user_id)[1])  # Pre-fill with current username
        self.new_username_entry.pack(pady=10, padx=20, fill=tk.X)

        self.new_password_entry = tk.Entry(self.window, font="Arial 14", bg="white", fg="black", bd=2, show="*")
        self.new_password_entry.pack(pady=10, padx=20, fill=tk.X)

        update_button = tk.Button(self.window, text="Update", command=self.update_details, font="Arial 14 bold", bg="#2a9d8f", fg="white")
        update_button.pack(pady=20)

        cancel_button = tk.Button(self.window, text="Cancel", command=self.window.destroy, font="Arial 14 bold", bg="#e76f51", fg="white")
        cancel_button.pack(pady=10)

    def update_details(self):
        new_username = self.new_username_entry.get().strip()
        new_password = self.new_password_entry.get().strip()

        if new_username and new_password:
            self.db.update_user(self.user_id, new_username, new_password)
            messagebox.showinfo("Success", "Details updated successfully.")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Username and password cannot be empty.")

class Dashboard:
    def __init__(self, user_id):
        self.db = Database()
        self.user_id = user_id

        self.root = tk.Tk()
        self.root.title("Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg="#264653")

        # Create widgets
        self.create_widgets()

        # Start main loop
        self.root.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Dashboard", bg="#264653", fg="#FFC300", font="Arial 36 bold")
        title_label.pack(pady=(20, 10))

        start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test, font="Arial 18 bold", bg="#2a9d8f", fg="white")
        start_button.pack(pady=20)

        view_scores_button = tk.Button(self.root, text="View Scores", command=self.view_scores, font="Arial 18 bold", bg="#2a9d8f", fg="white")
        view_scores_button.pack(pady=20)

        update_details_button = tk.Button(self.root, text="Update Details", command=self.update_details_window, font="Arial 18 bold", bg="#2a9d8f", fg="white")
        update_details_button.pack(pady=20)

        delete_account_button = tk.Button(self.root, text="Delete Account", command=self.delete_account, font="Arial 18 bold", bg="#e76f51", fg="white")
        delete_account_button.pack(pady=20)

        logout_button = tk.Button(self.root, text="Logout", command=self.logout, font="Arial 18 bold", bg="#264653", fg="white")
        logout_button.pack(pady=20)

    def start_typing_test(self):
        self.root.destroy()
        ZTyper(self.user_id)

    def view_scores(self):
        scores = self.db.get_scores(self.user_id)
        top = tk.Toplevel(self.root)
        top.title("Your Scores")
        top.geometry("800x600")
        top.configure(bg="#2a9d8f")

        label = tk.Label(top, text="Your Scores", font=("Arial", 20), bg="#2a9d8f", fg="white")
        label.pack(pady=10)

        frame = tk.Frame(top, bg="#2a9d8f")
        frame.pack(pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scores_list = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 12), bg="#264653", fg="white")
        for score, created_at in scores:
            scores_list.insert(tk.END, f"Score: {score} - {created_at}")
        scores_list.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar.config(command=scores_list.yview)

    def update_details_window(self):
        UpdateDetailsWindow(self.user_id)

    def delete_account(self):
        confirmation = messagebox.askyesno("Delete Account", "Are you sure you want to delete your account?")
        if confirmation:
            self.db.delete_user(self.user_id)
            messagebox.showinfo("Account Deleted", "Your account has been deleted.")
            self.root.destroy()

    def logout(self):
        self.root.destroy()
        from auth import AuthWindow
        AuthWindow()

if __name__ == "__main__":
    from auth import AuthWindow
    AuthWindow()

