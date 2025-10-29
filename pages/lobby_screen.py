import tkinter as tk
from tkinter import messagebox

class LobbyScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#1E90FF')
        self.controller = controller

        # Başlık
        title_label = tk.Label(self, text="Lobby", font=("Helvetica", 24, "bold"), bg='#1E90FF', fg='white')
        title_label.pack(pady=30)

        # Bilgi / durum etiketi
        info_label = tk.Label(self, text="Ready to start the game.", font=("Helvetica", 12), bg='#1E90FF', fg='white')
        info_label.pack(pady=10)

        # Start Game butonu
        start_game_btn = tk.Button(
            self,
            text="Start Game",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 14, 'bold'),
            padx=20,
            pady=10,
            command=self.start_game
        )
        start_game_btn.pack(pady=20)

        # Geri butonu (lobi'den ana sayfaya dön)
        back_button = tk.Button(
            self,
            text="Back",
            bg='#FFD700',
            fg='#000000',
            activebackground='#FFA500',
            font=('Helvetica', 12, 'bold'),
            padx=10,
            pady=8,
            command=lambda: controller.show_frame("HomePage")
        )
        back_button.pack(pady=10)

    def start_game(self):
        # Oyun başlatma mantığı burada eklenecek. Şimdilik placeholder.
        messagebox.showinfo("Start Game", "Game start logic not implemented yet.")
