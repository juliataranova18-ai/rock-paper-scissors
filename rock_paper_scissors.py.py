import tkinter as tk
from tkinter import messagebox
import random
import time

class ModernRockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ROCK • PAPER • SCISSORS")
        self.window.geometry("500x700")
        self.window.configure(bg='#0f0f23')
        self.window.resizable(False, False)

        # Современная цветовая схема
        self.colors = {
            'bg': '#0f0f23',
            'card_bg': '#1a1a2e',
            'accent': '#ff2a6d',
            'accent2': '#05d9e8',
            'text': '#ffffff',
            'text_secondary': '#b8b8b8',
            'success': '#00ff9f',
            'warning': '#ffcc00'
        }

        # Шрифты
        self.fonts = {
            'title': ('Arial', 24, 'bold'),
            'subtitle': ('Arial', 14, 'bold'),
            'normal': ('Arial', 12),
            'score': ('Arial', 16, 'bold'),
            'choice': ('Arial', 18, 'bold')
        }

        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.round = 1

        self.create_modern_ui()

    def create_modern_ui(self):
        # Header с градиентным эффектом
        header_frame = tk.Frame(self.window, bg=self.colors['bg'], height=120)
        header_frame.pack(fill='x', padx=20, pady=(20, 10))

        title = tk.Label(
            header_frame,
            text="ROCK • PAPER • SCISSORS",
            font=self.fonts['title'],
            bg=self.colors['bg'],
            fg=self.colors['accent2']
        )
        title.pack(pady=(10, 5))

        subtitle = tk.Label(
            header_frame,
            text="Современная версия классической игры",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        )
        subtitle.pack()

        # Карточка с текущим раундом
        round_frame = tk.Frame(self.window, bg=self.colors['card_bg'], relief='flat', bd=0)
        round_frame.pack(fill='x', padx=20, pady=10)

        tk.Label(
            round_frame,
            text=f"РАУНД {self.round}",
            font=self.fonts['subtitle'],
            bg=self.colors['card_bg'],
            fg=self.colors['text']
        ).pack(pady=5)

        # Карточка счета
        score_frame = tk.Frame(self.window, bg=self.colors['card_bg'], relief='flat', bd=0)
        score_frame.pack(fill='x', padx=20, pady=10)

        self.score_label = tk.Label(
            score_frame,
            text=f"👤 {self.user_score}   |   🤖 {self.computer_score}   |   ⚖️ {self.ties}",
            font=self.fonts['score'],
            bg=self.colors['card_bg'],
            fg=self.colors['text']
        )
        self.score_label.pack(pady=10)

        # Область выбора компьютера с анимацией
        computer_frame = tk.Frame(self.window, bg=self.colors['bg'])
        computer_frame.pack(fill='x', padx=20, pady=20)

        tk.Label(
            computer_frame,
            text="ВЫБОР КОМПЬЮТЕРА",
            font=('Arial', 10, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        ).pack()

        self.computer_display = tk.Label(
            computer_frame,
            text="❓",
            font=('Arial', 48),
            bg=self.colors['bg'],
            fg=self.colors['accent2']
        )
        self.computer_display.pack(pady=10)

        # Область результата
        self.result_label = tk.Label(
            self.window,
            text="Сделайте ваш ход!",
            font=self.fonts['choice'],
            bg=self.colors['bg'],
            fg=self.colors['success']
        )
        self.result_label.pack(pady=10)

        # Кнопки выбора - современный дизайн
        choices_frame = tk.Frame(self.window, bg=self.colors['bg'])
        choices_frame.pack(pady=30)

        # Камень
        self.rock_btn = self.create_modern_button(
            choices_frame,
            "🪨 КАМЕНЬ",
            "#ff2a6d",
            lambda: self.play("камень")
        )
        self.rock_btn.grid(row=0, column=0, padx=10, pady=10)

        # Ножницы
        self.scissors_btn = self.create_modern_button(
            choices_frame,
            "✂️ НОЖНИЦЫ",
            "#05d9e8",
            lambda: self.play("ножницы")
        )
        self.scissors_btn.grid(row=0, column=1, padx=10, pady=10)

        # Бумага
        self.paper_btn = self.create_modern_button(
            choices_frame,
            "📄 БУМАГА",
            "#00ff9f",
            lambda: self.play("бумага")
        )
        self.paper_btn.grid(row=0, column=2, padx=10, pady=10)

        # Кнопка сброса
        reset_frame = tk.Frame(self.window, bg=self.colors['bg'])
        reset_frame.pack(pady=20)

        self.create_modern_button(
            reset_frame,
            "🔄 НАЧАТЬ ЗАНОВО",
            "#ffcc00",
            self.restart_game,
            width=20
        ).pack()

        # Статистика
        stats_frame = tk.Frame(self.window, bg=self.colors['card_bg'])
        stats_frame.pack(fill='x', padx=20, pady=20)

        self.stats_label = tk.Label(
            stats_frame,
            text=self.get_stats_text(),
            font=('Arial', 9),
            bg=self.colors['card_bg'],
            fg=self.colors['text_secondary'],
            justify='left'
        )
        self.stats_label.pack(pady=10)

    def create_modern_button(self, parent, text, color, command, width=12):
        btn = tk.Button(
            parent,
            text=text,
            font=self.fonts['normal'],
            width=width,
            height=2,
            bg=color,
            fg='white',
            relief='flat',
            bd=0,
            cursor='hand2',
            activebackground=self.adjust_color(color, 1.2),
            command=command
        )
        return btn

    def adjust_color(self, color, factor):
        # Простая функция для изменения яркости цвета
        return color

    def get_stats_text(self):
        total_games = self.user_score + self.computer_score + self.ties
        if total_games == 0:
            win_rate = 0
        else:
            win_rate = (self.user_score / total_games) * 100

        return f"📊 СТАТИСТИКА:\nВсего игр: {total_games} | Ваш винрейт: {win_rate:.1f}%"

    def animate_computer_choice(self, final_choice):
        choices = ["🪨", "✂️", "📄"]
        for i in range(8):
            current = random.choice(choices)
            self.computer_display.config(text=current)
            self.window.update()
            time.sleep(0.1)
        self.computer_display.config(text=self.get_emoji(final_choice))

    def play(self, user_choice):
        # Блокируем кнопки во время анимации
        self.rock_btn.config(state='disabled')
        self.scissors_btn.config(state='disabled')
        self.paper_btn.config(state='disabled')

        # Компьютер делает выбор
        choices = ["камень", "ножницы", "бумага"]
        computer_choice = random.choice(choices)

        # Анимация выбора компьютера
        self.animate_computer_choice(computer_choice)

        # Определяем победителя
        result = self.determine_winner(user_choice, computer_choice)

        # Обновляем счет
        if "ВЫ" in result:
            self.user_score += 1
            self.result_label.config(fg=self.colors['success'])
        elif "КОМПЬЮТЕР" in result:
            self.computer_score += 1
            self.result_label.config(fg=self.colors['accent'])
        else:
            self.ties += 1
            self.result_label.config(fg=self.colors['warning'])

        # Обновляем интерфейс
        self.result_label.config(text=result)
        self.score_label.config(
            text=f"👤 {self.user_score}   |   🤖 {self.computer_score}   |   ⚖️ {self.ties}"
        )
        self.round += 1

        # Обновляем статистику
        self.stats_label.config(text=self.get_stats_text())

        # Разблокируем кнопки
        self.rock_btn.config(state='normal')
        self.scissors_btn.config(state='normal')
        self.paper_btn.config(state='normal')

        # Проверяем условия победы
        self.check_achievements()

    def get_emoji(self, choice):
        emojis = {
            "камень": "🪨",
            "ножницы": "✂️",
            "бумага": "📄"
        }
        return emojis.get(choice, "❓")

    def determine_winner(self, user, computer):
        if user == computer:
            return "🤝 НИЧЬЯ!"

        winning_combinations = {
            "камень": "ножницы",
            "ножницы": "бумага",
            "бумага": "камень"
        }

        if winning_combinations[user] == computer:
            return "🎉 ВЫ ПОБЕДИЛИ!"
        else:
            return "💻 КОМПЬЮТЕР ПОБЕДИЛ!"

    def check_achievements(self):
        if self.user_score >= 10:
            messagebox.showinfo("🏆 ПОБЕДА!", "Вы достигли 10 побед! Вы мастер игры!")
            self.restart_game()
        elif self.computer_score >= 10:
            messagebox.showwarning("💀 ПОРАЖЕНИЕ", "Компьютер слишком силен! Попробуйте еще раз!")
            self.restart_game()

    def restart_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.round = 1
        self.computer_display.config(text="❓")
        self.result_label.config(text="Сделайте ваш ход!", fg=self.colors['success'])
        self.score_label.config(
            text=f"👤 {self.user_score}   |   🤖 {self.computer_score}   |   ⚖️ {self.ties}"
        )
        self.stats_label.config(text=self.get_stats_text())

# Запуск современной версии
if __name__ == "__main__":
    app = ModernRockPaperScissors()
    app.window.mainloop()
