from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import random
import pygame
import webbrowser
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import subprocess
import os

class ZTyper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZTyper")      
        self.root.geometry("800x600")
        self.root.configure(bg="#264653")
        self.root.attributes("-fullscreen", False)

        # Load resources
        self.load_icon()
        self.load_words()
        self.load_sounds()

        # Game state variables
        self.timeleft = 60
        self.matched = 0
        self.not_matched = 0

        # Create widgets
        self.create_widgets()
        self.root.bind('<F11>', self.toggle_fullscreen)
        self.root.bind('<Return>', self.start_game)

        # Start main loop
        self.root.mainloop()

    def load_icon(self):
        icon_image = Image.open("./typing.ico")
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(True, icon_photo)

    def load_words(self):
        self.words = [
            'red car', 'blue sky', 'green grass', 'yellow duck', 'black night', 'white cloud', 'silver coin',
            'purple flower', 'orange sun', 'pink candy', 'brown dog', 'grey cat', 'beige sand', 'gold ring',
            'turquoise sea', 'maroon hat', 'navy ship', 'cream cake', 'mint leaf', 'teal ocean', 'coral reef',
            'violet butterfly', 'indigo jeans', 'ruby gem', 'amber necklace', 'ivory tower', 'jade stone', 'lavender scent',
            'magenta lipstick', 'olive oil', 'peach fruit', 'plum jam', 'salmon fish', 'tan skin', 'taupe color',
            'bronze medal', 'copper wire', 'banana fruit', 'happy child', 'big tree', 'small book', 'round ball',
            'soft pillow', 'hard rock', 'fast car', 'slow turtle', 'loud music', 'quiet room', 'tasty cake',
            'sour lemon', 'sweet cookie', 'spicy chili', 'bitter medicine', 'hot sun', 'cold ice', 'fresh air',
            'wet rain', 'dry desert', 'smooth silk', 'rough stone', 'sharp knife', 'dull pencil', 'clear water',
            'cloudy sky', 'sunny day', 'windy weather', 'stormy night', 'calm sea', 'angry bee', 'happy smile',
            'sad tear', 'fierce lion', 'gentle lamb', 'brave hero', 'cowardly mouse', 'loud thunder', 'quiet whisper',
            'busy street', 'empty room', 'colorful rainbow', 'dull gray', 'shiny gold', 'soft fur', 'hard shell'
        ]

    def load_sounds(self):
        pygame.mixer.init()

    def create_widgets(self):
        self.create_title()
        self.create_word_entry()
        self.create_timer()
        self.create_progress_bar()
        self.create_instructions()
        self.create_score_widgets()
        self.create_menu()

    def create_title(self):
        title_label = Label(self.root, text="ZTyper", bg="#264653", fg="#FFC300", font="Arial 36 bold")
        title_label.pack(pady=(20, 10))

    def create_word_entry(self):
        self.word_label = Label(self.root, text=random.choice(self.words), font="Arial 24 bold", fg="#FFD60A", bg="#264653")
        self.word_label.pack(pady=20)

        self.word_entry = Entry(self.root, font="Arial 18 bold", fg="grey", bg="#264653", justify="center", bd=4)
        self.word_entry.pack(pady=10)

    def create_timer(self):
        timer_frame = Frame(self.root, bg="#264653")
        timer_frame.pack()

        self.timer_label = Label(timer_frame, text="Time Left:", fg="green", bg="#264653", font="Arial 18 bold")
        self.timer_label.pack(side=LEFT, padx=(50, 10))

        self.timer_count = Label(timer_frame, text=self.timeleft, fg="green", bg="#264653", font="Arial 18 bold")
        self.timer_count.pack(side=LEFT)

    def create_progress_bar(self):
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate", maximum=self.timeleft)
        self.progress_bar.pack(pady=10)
        self.progress_bar['value'] = self.timeleft

    def create_instructions(self):
        instructions_label = Label(self.root, text="Type the phrase and press Enter to start the game", bg="#264653", fg="grey", font="Arial 14 italic")
        instructions_label.pack(pady=10)

    def create_score_widgets(self):
        score_frame = Frame(self.root, bg="#264653")
        score_frame.pack(pady=10)

        self.score_label = Label(score_frame, text="Your typing speed: ", bg="#264653", fg="#FFC300", font="Arial 20 bold")
        self.score_label.pack(side=LEFT, padx=(50, 10))

        self.score_count = Label(score_frame, text="", bg="#264653", fg="#FFC300", font="Arial 20 bold")
        self.score_count.pack(side=LEFT)

        self.feedback_label = Label(self.root, text="", bg="#264653", fg="#FFC300", font="Arial 16 bold")
        self.feedback_label.pack(pady=(10, 20))

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Score", command=self.save_score)
        file_menu.add_command(label="View Previous Scores", command=self.show_previous_scores)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_game)

        tips_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tips", menu=tips_menu)
        tips_menu.add_command(label="Show Tips", command=self.show_tips)

        online_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Online", menu=online_menu)
        online_menu.add_command(label="Start Online Test", command=self.open_online)

        python_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Update", menu=python_menu)
        python_menu.add_command(label="Install Python", command=self.install_python)

    def toggle_fullscreen(self, event=None):
        fullscreen = not self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", fullscreen)

    def show_tips(self):
        messagebox.showinfo("Tips", "1. Practice regularly.\n2. Focus on accuracy over speed.\n3. Take breaks to rest your hands and eyes.\n4. Use all your fingers while typing.\n5. Use online typing tools for practice.")

    def save_score(self):
        with open("scores.txt", "a") as file:
            file.write(f"Score: {self.matched}\n")

    def exit_game(self):
        self.root.quit()

    def show_previous_scores(self):
        top = Toplevel(self.root)
        top.title("Previous Scores")
        top.geometry("800x600")
        top.configure(bg="#2a9d8f")

        with open("scores.txt", "r") as file:
            scores = file.readlines()

        label = Label(top, text="Previous Scores", font=("Arial", 20), bg="#2a9d8f", fg="white")
        label.pack(pady=10)

        frame = Frame(top, bg="#2a9d8f")
        frame.pack(pady=10)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        scores_list = Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 12), bg="#264653", fg="white")
        for score in scores:
            scores_list.insert(END, score.strip())
        scores_list.pack(side=LEFT, fill=BOTH)

        scrollbar.config(command=scores_list.yview)

        # Plotting graph
        score_values = [int(score.split(":")[1].strip()) for score in scores if score.strip().startswith("Score")]
        plt.figure(figsize=(8, 6))
        plt.bar(range(len(score_values)), score_values, color='#e9c46a')
        plt.xlabel('Game', fontsize=14)
        plt.ylabel('Score', fontsize=14)
        plt.title('ZTyper - Previous Scores', fontsize=16)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.savefig('scores_graph.png')

        image = Image.open('scores_graph.png')
        graph_photo = ImageTk.PhotoImage(image)
        graph_label = Label(top, image=graph_photo, bg="#2a9d8f")
        graph_label.image = graph_photo
        graph_label.pack(pady=10)

    def open_online(self):
        webbrowser.open_new("ztyper.html")

    def install_python(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        installer_path = os.path.join(current_directory, "Python_Install", "python-3.12.3-amd64.exe")

        if os.path.exists(installer_path):
            subprocess.Popen(installer_path)
        else:
            print("Installer not found:", installer_path)

    def time(self):
        if self.timeleft > 0:
            self.timeleft -= 1
            self.timer_count.configure(text=self.timeleft)
            self.progress_bar['value'] = self.timeleft
            self.timer_count.after(1000, self.time)
            if self.timeleft < 11:
                self.timer_count.configure(fg="red")
                self.timer_label.configure(fg="red")
            if self.timeleft == 10:
                pygame.mixer.music.load("countdown1.mp3")
                pygame.mixer.music.play(loops=0)
        else:
            self.end_game()

    def start_game(self, event):
        if self.timeleft == 60:
            self.time()

        if self.word_entry.get().strip() == self.word_label["text"]:
            self.matched += 1
            self.word_label.configure(fg="green")
        else:
            self.not_matched += 1
            self.word_label.configure(fg="red")
            pygame.mixer.music.load("buzzer1.mp3")
            pygame.mixer.music.play(loops=0)

        self.word_label.after(500, self.next_word)
        self.word_entry.delete(0, END)

    def next_word(self):
        self.word_label.configure(text=random.choice(self.words), fg="#FFD60A")

    def end_game(self):
        self.score_count.configure(text=self.matched)
        if 35 <= self.matched <= 40:
            self.feedback_label.configure(text="Average")
        elif self.matched >= 65:
            self.feedback_label.configure(text="Above Average")
        else:
            self.feedback_label.configure(text="Below Average")

        retry = messagebox.askretrycancel('Notification', 'Do you want to retry?')
        if retry:
            self.reset_game()

    def reset_game(self):
        self.timeleft = 60
        self.matched = 0
        self.not_matched = 0
        self.feedback_label.configure(text='')
        self.score_count.configure(text='')
        self.score_label.configure(text='')
        self.timer_count.configure(text=self.timeleft, fg="green")
        self.timer_label.configure(fg="green")
        self.word_entry.delete(0, END)
        self.word_label.configure(text=random.choice(self.words), fg="#FFD60A")

if __name__ == "__main__":
    ZTyper()
