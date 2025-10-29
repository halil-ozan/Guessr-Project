import tkinter as tk
from tkinter import messagebox
from database.db_manager import DatabaseManager

db = DatabaseManager()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#1E90FF')
        
        # Title
        title = tk.Label(self, 
                        text="Login",
                        font=('Helvetica', 24, 'bold'),
                        bg='#1E90FF',
                        fg='white')
        title.pack(pady=50)
        
        # Username
        tk.Label(self, text="Username:", bg='#1E90FF', fg='white').pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        
        # Password
        tk.Label(self, text="Password:", bg='#1E90FF', fg='white').pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        # Login Button
        login_button = tk.Button(
            self,
            text="Login",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            command=self.handle_login
        )
        login_button.pack(pady=10)
        
        # Register Button
        register_button = tk.Button(
            self,
            text="Register",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            command=lambda: controller.show_frame("RegisterPage")
        )
        register_button.pack(pady=10)
        
        # Back Button
        back_button = tk.Button(
            self,
            text="Back",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            command=lambda: controller.show_frame("HomePage")
        )
        back_button.pack(pady=10)

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Login Failed", "Please fill in all fields.")
            return
        
        user = db.verify_user(username, password)
        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {user['username']}!")
            self.controller.show_frame("LobbyScreen")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
