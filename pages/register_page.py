import tkinter as tk
from tkinter import messagebox
from database.db_manager import DatabaseManager

db = DatabaseManager()

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#1E90FF')
        
        # Title
        title = tk.Label(self, 
                        text="Register",
                        font=('Helvetica', 24, 'bold'),
                        bg='#1E90FF',
                        fg='white')
        title.pack(pady=50)
        
        # Username
        tk.Label(self, text="Username:", bg='#1E90FF', fg='white').pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        
        # Email
        tk.Label(self, text="Email:", bg='#1E90FF', fg='white').pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        
        # Password
        tk.Label(self, text="Password:", bg='#1E90FF', fg='white').pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        # Register Button
        register_button = tk.Button(
            self,
            text="Register",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            command=self.handle_register
        )
        register_button.pack(pady=10)
        
        # Back to Login Button
        back_button = tk.Button(
            self,
            text="Back to Login",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            command=lambda: controller.show_frame("LoginPage")
        )
        back_button.pack(pady=10)

    def handle_register(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not email or not password:
            messagebox.showerror("Registration Failed", "Please fill in all fields.")
            return
        
        if db.add_user(username, password, email):
            messagebox.showinfo("Registration Successful", "You can now log in.")
            self.controller.show_frame("LoginPage")
        else:
            messagebox.showerror("Registration Failed", "Username or email already exists.")
