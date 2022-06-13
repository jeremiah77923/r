import json
import tkinter
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

data_dict = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    global password_list
    for char in range(randint(8, 10)):
        password_list.append(choice(letters))

    for char in range(randint(2, 4)):
        password_list += choice(symbols)

    for char in range(randint(2, 4)):
        password_list += choice(numbers)

    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
websites = []
emails = []
pas = []


def add():
    is_ok = None
    websites = web_entry.get()
    emails= email_entry.get()
    pas = pass_entry.get()
    if len(websites) == 0 or len(emails) == 0 or len(pas) == 0:
        websites = web_entry.get()
        emails = email_entry.get()
        pas = pass_entry.get()
        not_enough = messagebox.showwarning(title="Warning", message="Please enter in all fields!!")
    if  not len(websites) == 0 and not len(emails) == 0 and not len(pas) == 0:

        is_ok = messagebox.askokcancel(title="Is it okay to save?",
                                       message=f"These are the details entered: \nWebsite: {websites}\nEmail"
                                               f"/Username: {emails} \n Password: {pas}\n Is it Okay?")
    if is_ok and len(websites) > 0 and len(emails) > 0 and len(pas) > 0:
        data_dict["Website"] = websites
        data_dict["Email/Username"] = emails
        data_dict["Password"] = pas
        new_data = {websites: {
            "Email/Username": emails,
            "Password": pas
        },
        }
        try:
            with open("passwords.JSON", "r") as File:
                data = json.load(File)
        except FileNotFoundError:
            with open("passwords.JSON","w") as File:
                json.dump(new_data, File, indent=4)
        else:
            data.update(new_data)
            with open("passwords.JSON", "w") as File:
                json.dump(data, File, indent =4)
        finally:
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- Search for a password -----------------
def search():
   web = web_entry.get()
   with open("passwords.JSON","r") as File:
    data = json.load(fp=File)
    if web in data:
        passw = data[web]['Password']
        email = "Email/Username"
        messagebox.showinfo(title=web, message = f"Email: {data[web][email]}\nPassword: {passw}" )
# ---------------------------- UI SETUP -----------------
window = Tk()
window.title("Password Manager")
canvas = Canvas(width=300, height=200)
window.config(padx=50, pady=50)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=1)
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)



web_entry = Entry(width=29)
web_entry.grid(column=1, row=2, sticky=W)
web_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3, sticky=W)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=3, sticky=W)

search = Button(text="Search", command = search)
search.grid(column=1, row = 2,  sticky=E)


pass_label = Label(text="Password")
pass_label.grid(column=0, row=4)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=4, sticky=W)

gen_pass = Button(text="Generate Password", command=generate)
gen_pass.grid(column=1, row=4, sticky=E)

add = Button(text="Add", command=add, width=35)
add.grid(column=1, row=5)
window.mainloop()
