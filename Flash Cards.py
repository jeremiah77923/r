import random
from tkinter import *
import pandas

# Create new Flash Cards:
from pandas import DataFrame

global back_card
global side
global title
side = "front"
global on_back
on_back = True
global word
global data
global language_learning
language_learning = ""
global first_language
first_language = ""


def create():
    global language_learning
    global first_language
    str = f"Files/{language_learning}_words.csv"
    with open(str, "w") as File:
        File.write("Word,Meaning\n")
        q = input(
            "Your words file has been made, Type \"a\" to start entering in words or \"q\" to return to the main menu.\n")
        while q != "q":
            q = input(
                f"Enter in an {first_language} word, then type space, then type its {language_learning} meaning\n")
            words = q.split(" ")

            if q.lower() != "q":
                if " " not in q or len(words) != 2:
                    print("You did not follow directions plz trying again")
                    q = input(
                        f"Enter in an {first_language} word, then type space, then type its "
                        f"{language_learning} meaning, or type \"q\" to quit\n")

            if q.lower() != "q":
                File.write(f"{words[0]},{words[1]}\n")


def options():
    global language_learning
    global first_language
    print("Type the number of the language that you want to study?")
    print("1.Spanish")
    print("2.English")
    print("3.Japanese")
    print("4.Russian")
    print("5.German")
    print("6.Korean")
    print("7.Mandarin")
    print("8.Portuguese")
    print("9.Latin")
    print("10.French")
    languages = {1: "Spanish", 2:
                 "English", 3: "Japanese", 4: "Russian",
                 5: "German", 6: "Korean", 7: "Mandarin",
                 8: "Portuguese", 9:
                     "Latin", 10: "French"}
    language_to_learn = int(input("Type the number of the language that you want to learn\n"))
    language_learning = languages[language_to_learn]
    first_language = input("What is your first language, the language that you grew up learning or the one that your "
                           "parents speak, if you grew up learning multiple languages just type the language that you"
                           " know best\n")
    print(f"Enjoy learning some {language_learning}")
    return ""
def add():
    global language_learning
    global first_language
    str = f"Files/{language_learning}_words.csv"
    with open(str, "a") as File:
        q = input("Type \"a\" to start entering in words or \"q\" to quit the app if you are done.\n")
        while q != "q":
            q = input(
                f"Enter in an {first_language} word, then type space, then type its {language_learning} meaning\n, or type \"q\" to quit")
            words = q.split(" ")

            if q.lower() != "q":
                if " " not in q or len(words) != 2:
                    print("You did not follow directions plz trying again")
                    q = input(
                        f"Enter in an {first_language} word, then type space, then type its {language_learning} meaning\n")
            if q.lower() != "q":
                File.write(f"{words[0]},{words[1]}\n")




option = ""
while option != "yes":
    option = input("What do you want to do? If you want to study a set of cards type \"yes\","
               " if you want to create a new set or add to an existing set type \"no\"\n")
    if option == "yes":
        options()
    if option == "no":
        languages = {1: "Spanish", 2:
        "English",
                     3: "Japanese", 4: "Russian",
                 5: "German", 6: "Korean", 7: "Mandarin",
                 8: "Portuguese", 9:
                     "Latin", 10: "French"}

        print("1.Spanish")
        print("2.English")
        print("3.Japanese")
        print("4.Russian")
        print("5.German")
        print("6.Korean")
        print("7.Mandarin")
        print("8.Portuguese")
        print("9.Latin")
        print("10.French")
        language_learn = int(input("Type the number of the language that you want to create a set for or add to an existing "
                            "set?\n"))
        language_learning = languages[language_learn]
        first_language = input("What is your first language, the language that you grew up learning or the one that your "
                           "parents speak, if you grew up learning multiple languages just type the language that you"
                           " know best\n")
        has_cards = input(f"Type \"yes\" to add to your {languages[language_learn]} set, or \"no\" to create a {languages[language_learn]} set if you have not created one yet.\n")
        if has_cards == "no":
            create()
        if has_cards == "yes":
            add()

str = f"Files/{language_learning}_words.csv"
data = pandas.read_csv(str)
word_list = data.Word
data_dict = DataFrame.to_dict(data)
global card_back_img
global card_front_img
global word1
current_card = {}
global create2
create2 = False
creatte = False


def create():
    side = "front"
    global word1
    global current_card
    global on_back
    global create2
    if creatte == False:
        print(current_card)
        word1 = word_list[random.randint(0, len(word_list) - 1)]
        Canvas.itemconfig(title, text=language_learning)
        Canvas.itemconfig(img, image=card_front_img)
        Canvas.itemconfig(word, text=current_card)
        return
    Canvas.itemconfig(title, text=language_learning)
    Canvas.itemconfig(img, image=card_front_img)
    if create2:
        current_card = random.choice(data_dict["Word"])
        Canvas.itemconfig(word, text=current_card)


def create1():
    global create2
    global creatte
    create2 = True
    creatte = True
    create()


def create2():
    global creatte
    global create2
    creatte = False
    create2 = False
    create()


def create4():
    global creatte
    global create2
    create2 = False
    creatte = False
    back()


def get_key(val):
    for key, value in data_dict["Word"].items():
        if val == value:
            return key

    return "key doesn't exist"


def back():
    global on_back
    global word1
    global data
    global back_card
    side = "back"
    Canvas.itemconfig(title, text=first_language)
    word2 = data[data.Word == word]
    key = get_key(current_card)
    back_card = data_dict["Meaning"][key]
    Canvas.itemconfig(word, text=back_card)
    Canvas.itemconfig(img, image=card_back_img)
    on_back = False


# --------------------Set up the UI-------------------------
window = Tk()
window.title(f"{language_learning} Words")
window.config(padx=50, pady=50, bg="#B1DDC6")

right_button_img = PhotoImage(file="Images/right.png")
right_button = Button(image=right_button_img, bg="#B1DDC6", command=create1, highlightthickness=0)
right_button.grid(row=3, column=1)

left_button_img = PhotoImage(file="Images/wrong.png")
left_button = Button(image=left_button_img, bg="#B1DDC6", command=create1, highlightthickness=0)
left_button.grid(row=3, column=0, sticky=S)

card_front_img = PhotoImage(file="Images/card_front.png")
card_back_img = PhotoImage(file="Images/card_back.png")
Canvas = Canvas(width=800, height=526, bg="white")
img = Canvas.create_image(400, 263, image=card_front_img)
Canvas.config(bg="#B1DDC6", highlightthickness=0)
title = Canvas.create_text(400, 150, text=language_learning, font=("Ariel", 40, "italic"))
current_card = random.choice(data_dict["Word"])
word = Canvas.create_text(400, 300, text=current_card, font=("Ariel", 60, "bold"))
Canvas.grid(row=0, column=0, columnspan=2)

button = Button(text="Front", command=create2)
button.grid(row=1, column=0, sticky=E)
button1 = Button(text="Back", command=create4)
button1.grid(row=1, column=1, sticky=W)
window.mainloop()
