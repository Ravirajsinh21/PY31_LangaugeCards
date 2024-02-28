from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}


try:
    data = pd.read_csv("data/new")
    print("using new")
except FileNotFoundError:
    data=pd.read_csv("data/french_words.csv")
    print("using old")

to_learn=data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill ="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=front)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back)


def is_known():
    to_learn.remove(current_card)
    new=pd.DataFrame(to_learn)
    new.to_csv("data/new", index=False)
    next_card()

window = Tk()
window.title("Language Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=700, height= 426)
front = PhotoImage(file="images\card_front.png")
back = PhotoImage(file="images\card_back.png")
card=canvas.create_image(350,213, image=front)
canvas.grid(row = 0, column = 0, columnspan=2)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
title=canvas.create_text(350,150,text = "Title", font =("Ariel",40,"italic"))
word=canvas.create_text(350,213,text = "word", font =("Ariel",40,"bold"))

cross= PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross, highlightthickness=0, command= next_card)
unknown_button.grid(row=1, column = 0)

check= PhotoImage(file="images/right.png")
known_button = Button(image=check, highlightthickness=0, command=is_known)
known_button.grid(row=1, column = 1)

next_card()

window.mainloop()