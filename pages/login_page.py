import tkinter as tk

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
        
        # Back button
        back_button = tk.Button(
            self,
            text="Back",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            padx=10,
            pady=10,
            command=lambda: controller.show_frame("HomePage")
        )
        back_button.pack(pady=10)
