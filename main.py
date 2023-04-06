# -*- coding: utf-8 -*-

BACKGROUND_COLOR = "#B1DDC6"
import random 

from tkinter import *
import pandas as pd

current_card ={}
dict_data = {}

try:
        data =pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
        data = pd.read_csv("./data/turkish_to_english.csv").decode("utf-8")
        dict_data = data.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")

def next():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    canvas.itemconfig(card_word , text=current_card["Turkish"], fill="black")
    canvas.itemconfig(card_title , text="Turkish",fill="black")
    canvas.itemconfig(front_card , image=card)
    flip_timer = window.after(3000,func=flip_card)


def is_known():

    dict_data.remove(current_card)
    data = pd.DataFrame(dict_data)
    data.to_csv("./data/words_to_learn.csv",index=False)
    next()

def flip_card():
    global current_card
    canvas.itemconfig(card_title , text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(front_card , image=card2)


window = Tk()
window.title("Flash Cards To Learn Turkish")
# window.minsize(width=800 , height = 526)
window.config(padx=50 , pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

card = PhotoImage(file="./images/card_front.png")
card2 = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800 , height=526, background=BACKGROUND_COLOR,highlightthickness=0)
front_card = canvas.create_image(400,213, image=card )
card_title = canvas.create_text(400,150,text="title", font=("Arial", 30,"italic"))
card_word = canvas.create_text(400,250, text="word" ,font=("Arial",45,"bold"))
canvas.grid(column=0 , row=0, columnspan=2)




right_answer_icon = PhotoImage(file="./images/right.png")
right_answer = Button(image=right_answer_icon,highlightthickness=0,command=is_known)
right_answer.grid(column=0,row=1)

wrong_answer_icon= PhotoImage(file="./images/wrong.png")
wrong_answer = Button(image=wrong_answer_icon,highlightthickness=0,command=next)
wrong_answer.grid(column=1,row=1)

next()

# ---------------------- pandas formart ----------------------

window.mainloop()

