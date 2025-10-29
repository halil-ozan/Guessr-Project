import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#1E90FF')
        self.controller = controller
        
        # Title Label
        title_label = tk.Label(self, text="GeoGuessr Clone", font=("Helvetica", 24), bg='#1E90FF', fg='white')
        title_label.pack(pady=20)
        
        # Navigation Buttons
        login_button = tk.Button(self, text="Login", 
                               command=lambda: controller.show_frame("LoginPage"),
                               font=("Helvetica", 12))
        login_button.pack(pady=10)
        
        register_button = tk.Button(self, text="Register", 
                                  command=lambda: controller.show_frame("RegisterPage"),
                                  font=("Helvetica", 12))
        register_button.pack(pady=10)
        
        settings_button = tk.Button(self, text="Settings", 
                                  command=lambda: controller.show_frame("SettingsPage"),
                                  font=("Helvetica", 12))
        settings_button.pack(pady=10)
        
        # Exit button - directly created in the frame
        exit_button = tk.Button(
            self,
            text="Exit",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            padx=10,
            pady=10,
            command=controller.quit
        )
        exit_button.pack(pady=10)
