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

def play_game():
    root.destroy()
    import game

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

def show_tips():
    messagebox.showinfo("Tips", "1. Practice regularly.\n2. Focus on accuracy over speed.\n3. Take breaks to rest your hands and eyes.\n4. Use all your fingers while typing.\n5. Use online typing tools for practice.")

def save_score():
    with open("scores.txt", "a") as file:
        file.write(f"Score: {matched}\n")

def exit_game():
    root.quit()

def show_previous_scores():
    top = Toplevel(root)
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
    scores = [int(score.split(":")[1].strip()) for score in scores if score.strip().startswith("Score")]
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(scores)), scores, color='#e9c46a')
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

def open_online():
    webbrowser.open_new("ztyper.html")

def install_python():
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the relative path to the installer
    installer_path = os.path.join(current_directory, "Python_Install", "python-3.12.3-amd64.exe")

    # Check if the installer exists
    if os.path.exists(installer_path):
        subprocess.Popen(installer_path)
    else:
        print("Installer not found:", installer_path)

root = tk.Tk()
root.title("ZTyper")      
root.geometry("800x600+200+100")
root.configure(bg="#264653")
root.attributes("-fullscreen", False)

# Load the icon using PIL and convert it to a PhotoImage object
icon_image = Image.open("./typing.ico")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

# List of complete strings
words = ['red car', 'blue sky', 'green grass', 'yellow duck', 'black night', 'white cloud', 'silver coin',
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
                'busy street', 'empty room', 'colorful rainbow', 'dull gray', 'shiny gold', 'soft fur', 'hard shell',
                'sweet honey', 'bitter coffee', 'salty sea', 'sour apple', 'spicy curry', 'bland rice', 'tangy lemonade',
                'thick fog', 'thin thread', 'warm fire', 'cool breeze', 'hot tea', 'cold soda', 'fresh fruit', 'rotten egg',
                'clean room', 'dirty floor', 'tidy desk', 'messy drawer', 'organized closet', 'chaotic kitchen', 'busy bee',
                'lazy sloth', 'fast cheetah', 'slow snail', 'tall giraffe', 'short ant', 'long snake', 'short hair',
                'long beard', 'fast rabbit', 'slow turtle', 'small ant', 'big elephant', 'thin stick', 'thick book',
                'hot oven', 'cold freezer', 'hard wood', 'soft cotton', 'bitter taste', 'sweet smell', 'sour flavor',
                'salty snack', 'spicy food', 'tangy sauce', 'rough texture', 'smooth surface', 'sharp edge', 'dull blade',
                'bright light', 'dark night', 'loud noise', 'quiet whisper', 'happy laughter', 'sad tears', 'angry shout',
                'scary movie', 'funny joke', 'exciting adventure', 'boring lecture', 'interesting book', 'simple task',
                'complicated puzzle', 'easy answer', 'difficult question', 'correct answer', 'wrong answer', 'right choice',
                'wrong decision', 'fast runner', 'slow walker', 'tall building', 'short tree', 'long road', 'short distance',
                'tall mountain', 'short hill', 'long river', 'short stream', 'tall skyscraper', 'short house', 'big elephant',
                'small mouse', 'wide field', 'narrow path', 'deep ocean', 'shallow pond', 'wide smile', 'narrow eyes',
                'deep thought', 'shallow idea', 'strong wind', 'weak breeze', 'strong muscle', 'weak attempt', 'hard ground',
                'soft pillow', 'hard work', 'soft touch', 'rich flavor', 'poor condition', 'rich person', 'poor beggar',
                'beautiful flower', 'ugly duckling', 'beautiful sunset', 'ugly scar', 'beautiful melody', 'ugly noise',
                'beautiful painting', 'ugly stain', 'beautiful sight', 'ugly sight', 'beautiful day', 'ugly weather',
                'beautiful dream', 'ugly reality', 'beautiful smile', 'ugly frown', 'beautiful memory', 'ugly experience',
                'beautiful dress', 'ugly outfit', 'beautiful gesture', 'ugly behavior', 'beautiful soul', 'ugly attitude',
                'beautiful story', 'ugly truth', 'beautiful lie', 'ugly secret', 'beautiful creation', 'ugly destruction',
                'beautiful world', 'ugly reality', 'happy child', 'sad parent', 'angry teacher', 'scared student',
                'brave soldier', 'cowardly leader', 'bright idea', 'dark secret', 'fast car', 'slow train', 'tall building',
                'short fence', 'long river', 'short stream', 'wide road', 'narrow alley', 'deep ocean', 'shallow lake',
                'wide smile', 'narrow eyes', 'deep thought', 'shallow idea', 'strong wind', 'weak breeze', 'strong muscle',
                'weak attempt', 'hard ground', 'soft pillow', 'hard work', 'soft touch', 'rich flavor', 'poor condition',
                'rich person', 'poor beggar', 'beautiful flower', 'ugly duckling', 'beautiful sunset', 'ugly scar',
                'beautiful melody', 'ugly noise', 'beautiful painting', 'ugly stain', 'beautiful sight', 'ugly sight',
                'beautiful day', 'ugly weather', 'beautiful dream', 'ugly reality', 'beautiful smile', 'ugly frown',
                'beautiful memory', 'ugly experience', 'beautiful dress', 'ugly outfit', 'beautiful gesture', 'ugly behavior',
                'beautiful soul', 'ugly attitude', 'beautiful story', 'ugly truth', 'beautiful lie', 'ugly secret',
                'beautiful creation', 'ugly destruction', 'beautiful world', 'ugly reality', 'happy child', 'sad parent',
                'angry teacher', 'scared student', 'brave soldier', 'cowardly leader', 'bright idea', 'dark secret',
                'fast car', 'slow train', 'tall building', 'short fence', 'long river', 'short stream', 'wide road',
                'narrow alley', 'deep ocean', 'shallow lake', 'wide smile', 'narrow eyes', 'deep thought', 'shallow idea',
                'strong wind', 'weak breeze', 'strong muscle', 'weak attempt', 'hard ground', 'soft pillow', 'hard work',
                'soft touch', 'rich flavor', 'poor condition', 'rich person', 'poor beggar', 'beautiful flower',
                'ugly duckling', 'beautiful sunset', 'ugly scar', 'beautiful melody', 'ugly noise', 'beautiful painting',
                'ugly stain', 'beautiful sight', 'ugly sight', 'beautiful day', 'ugly weather', 'beautiful dream',
                'ugly reality', 'beautiful smile', 'ugly frown', 'beautiful memory', 'ugly experience', 'beautiful dress',
                'ugly outfit', 'beautiful gesture', 'ugly behavior', 'beautiful soul', 'ugly attitude', 'beautiful story',
                'ugly truth', 'beautiful lie', 'ugly secret', 'beautiful creation', 'ugly destruction', 'beautiful world',
                'ugly reality', 'happy child', 'sad parent', 'angry teacher', 'scared student', 'brave soldier',
                'cowardly leader', 'bright idea', 'dark secret', 'fast car', 'slow train', 'tall building', 'short fence',
                'long river', 'short stream', 'wide road', 'narrow alley', 'deep ocean', 'shallow lake', 'wide smile',
                'narrow eyes', 'deep thought', 'shallow idea', 'strong wind', 'weak breeze', 'strong muscle',
                'weak attempt', 'hard ground', 'soft pillow', 'hard work', 'soft touch', 'rich flavor', 'poor condition',
                'rich person', 'poor beggar', 'beautiful flower', 'ugly duckling', 'beautiful sunset', 'ugly scar',
                'beautiful melody', 'ugly noise', 'beautiful painting', 'ugly stain', 'beautiful sight', 'ugly sight',
                'beautiful day', 'ugly weather', 'beautiful dream', 'ugly reality', 'beautiful smile', 'ugly frown',
                'beautiful memory', 'ugly experience', 'beautiful dress', 'ugly outfit', 'beautiful gesture',
                'ugly behavior', 'beautiful soul', 'ugly attitude', 'beautiful story', 'ugly truth', 'beautiful lie',
                'ugly secret', 'beautiful creation', 'ugly destruction', 'beautiful world', 'ugly reality']


pygame.mixer.init()

def time():
    global timeleft, matched
    if timeleft > 0:
        timeleft -= 1
        timercount.configure(text=timeleft)
        timercount.after(1000, time)
        if timeleft < 11:
            timercount.configure(fg="red")
            timer.configure(fg="red")
        if timeleft == 10:
            pygame.mixer.music.load("countdown1.mp3")
            pygame.mixer.music.play(loops=0)
    else:
        scorecount.configure(text=matched)
        scorelabel.configure(text="Your typing speed: ")
        if 35 <= matched <= 40:
            feedback.configure(text="Average")
        elif matched >= 65:
            feedback.configure(text="Above Average")
        else:
            feedback.configure(text="Below Average")

        retry = messagebox.askretrycancel('Notification', 'Do you want to retry?')

        if retry:
            timeleft = 60
            matched = 0
            feedback.configure(text='')
            scorecount.configure(text='')
            scorelabel.configure(text='')
            timercount.configure(text=timeleft, fg="yellow")
            timer.configure(fg="yellow")
            wordentry.delete(0, END)

def startGame(event):
    global matched, not_matched

    if timeleft == 60:
        time()

    # Comparing complete strings
    if wordentry.get() == word["text"]:
        matched += 1
    elif wordentry.get() != word["text"]:
        not_matched += 1
        pygame.mixer.music.load("buzzer1.mp3")
        pygame.mixer.music.play(loops=0)

    random.shuffle(words)
    word.configure(text=words[0])
    wordentry.delete(0, END)
    label.configure(text="")


h1 = Label(root, text="ZTyper", bg="#264653", fg="#FFC300", font="Arial 24 bold", anchor="center")
h1.pack(pady=10)

word = Label(root, text=words[0], font="Arial 20 bold", fg="#FFD60A", bg="#264653", width=20, anchor="center")
word.place(y=200, x=100)

wordentry = Entry(root, font="Arial 18 bold", fg="grey", bg="#264653", justify="center", bd=4)
wordentry.place(x=100, y=300)

timer = Label(root, text="Timer:", fg="green", bg="#264653", font="Arial 18 bold")
timer.place(x=650, y=100)

timeleft = 60

timercount = Label(root, text="60", fg="green", bg="#264653", font="Arial 16 bold")
timercount.place(x=675, y=140)

label = Label(root, text="Type phrase and hit Enter to start the game", bg="#264653", fg="grey", font="Arial 10 italic")
label.place(x=200, y=400)

matched = 0
not_matched = 0

scorelabel = Label(root, text="", bg="#264653", fg="#FFC300", font="Arial 17 bold")
scorelabel.place(x=50, y=500)

scorecount = Label(root, text="", bg="#264653", fg="#FFC300", font="Arial 17 bold")
scorecount.place(x=250, y=500)

feedback = Label(root, text="", bg="#264653", fg="#FFC300", font="Arial 12 bold")
feedback.place(x=400, y=500)

fullscreen = False
root.bind('<F11>', toggle_fullscreen)

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Score", command=save_score)
file_menu.add_command(label="View Previous Scores", command=show_previous_scores)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_game)

tips_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tips", menu=tips_menu)
tips_menu.add_command(label="Show Tips", command=show_tips)

online_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Online", menu=online_menu)
online_menu.add_command(label="Start Online Test", command=open_online)

# New menu for Python installation
python_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Update", menu=python_menu)
python_menu.add_command(label="Install Python", command=install_python)

root.bind('<Return>', startGame)
root.mainloop()
