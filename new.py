from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os

def play_game():
    root.destroy()
    import game

root = tk.Tk()
root.title("Typing Master")      
root.geometry("600x400+400-200")
root.configure(bg="#001D3D")

# Get the current working directory
current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, "typing.ico")

# Check if the icon file exists
if os.path.exists(icon_path):
    root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file=icon_path))
else:
    print("Icon file not found.")

root.maxsize(600, 400)
root.minsize(600, 400)

label1 = Label(root, text="Welcome To Typing Master", font="comicsansms 25 bold", fg="#FFC300", bg="#001D3D", anchor="center")
label1.pack(pady=7)    #welcome text

label2 = Label(root, text="Instructions: Enter the given words in limited time and find your typing speed at the end of the game. Enjoy!!", font="comicsansms 15 italic", fg="grey", bg="#001D3D", anchor="center", wraplength=500)
label2.pack(pady=20)      #instructions to play game

play = Image.open("play.png")                  #play button  
resize_image = play.resize((224, 87))
play = ImageTk.PhotoImage(resize_image)
play_button = Button(root, image=play, borderwidth=0, bg="#001D3D", command=play_game, bd=0, anchor="center")
play_button.pack(pady=70)

root.mainloop()
