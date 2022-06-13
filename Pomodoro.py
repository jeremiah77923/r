import math
from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CURRENT_TIME = 0
Continue = True
COUNT_SEC = 25 * 60
reps = 0
breaks = 0
dict_time = {0: SHORT_BREAK_MIN, 1: SHORT_BREAK_MIN, 2: SHORT_BREAK_MIN, 3: LONG_BREAK_MIN}
dict1 = {0: WORK_MIN, 1: dict_time[reps]}
string_dict = {0: "5:00", 1: "5:00", 2: "5:00", 3: "5:00", 4: "20:00"}
og_time = CURRENT_TIME
reset = False

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def Stop():
    global Continue
    Continue = False
    global COUNT_SEC
    COUNT_SEC += 60


def count_down():
    global reps
    if reps > 3:
        reps = 0
    global Continue
    global breaks
    global og_time
    Continue = True
    global CURRENT_TIME
    global WORK_MIN
    global reset
    time = 0
    if reset:
        if breaks == 0:
            time = 25
        if breaks == 1 and reps < 3:
            time = 5
        if breaks == 1 and reps == 3:
            time = 20
        CURRENT_TIME = time * 60
        og_time = CURRENT_TIME
    if reset == False:
        CURRENT_TIME = WORK_MIN * 60
        og_time = CURRENT_TIME
    reset = False
    if breaks == 0:
        title_label.config(text="Work")
    if breaks == 1:
        title_label.config(text="Break", fg=PINK)
    start_timer(CURRENT_TIME)


def Reset():
    global Continue
    Continue = False
    global WORK_MIN
    global CURRENT_TIME
    global breaks
    global reset
    time = 0
    reset = True
    if breaks == 0:
        time = 1500
    if breaks == 1 and reps < 3:
        time = 300
    if breaks == 1 and reps == 3:
        time = 1200
    CURRENT_TIME = time
    CURRENT_TIME *= 60
    text = ""
    if breaks == 0:
        text = "25:00"
    if breaks == 1 and reps == 3:
        text = string_dict[reps]
    canvas.itemconfig(timer_text, text=text)


def Break():
    global breaks
    global CURRENT_TIME
    global COUNT_SEC
    global WORK_MIN
    WORK_MIN = dict_time[reps]
    CURRENT_TIME = WORK_MIN * 60
    canvas.itemconfig(timer_text, text=string_dict[reps])


def start_timer(count):
    global CURRENT_TIME
    global WORK_MIN
    global breaks
    global reps
    if count >= 0 and Continue:
        global COUNT_SEC
        CURRENT_TIME = math.floor(count / 60)
        COUNT_SEC = int(count % 60)
        WORK_MIN = CURRENT_TIME + COUNT_SEC / 60
        if COUNT_SEC == 0:
            COUNT_SEC = "00"
        canvas.itemconfig(timer_text, text=f"{CURRENT_TIME}:{COUNT_SEC}")
        window.after(1000, start_timer, count - 1)
    if count == 0:
        reps += 1
        if og_time >= 1400:
            breaks += 1
            Break()
            file = "ding-sound-effect_2.mp3"
            os.system("afplay " + file)
        if og_time < 1400:
            title_label.config(text="Work")
            Reset()
            breaks = 0
            file = "ding-sound-effect_2.mp3"
            os.system("afplay " + file)


# ---------------------------- UI SETUP -----------------
window = Tk()

# for playing wav file

window.title("Pomodoro")

window.config(padx=125, pady=75, bg=YELLOW)

title_label = Label(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=count_down)
start.grid(row=2, column=1, sticky=W)

stop = Button(text="Stop", command=Stop)
stop.grid(row=2, column=0)
stop.grid(row=2, column=0, sticky=E)

reset = Button(text="Reset", command=Reset)
reset.grid(row=2, column=2)

window.mainloop()
