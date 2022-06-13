# Author: Jeremiah Hawthorne
# Started: Fri September 17th
# Finished: not yet
import datetime

import requests as r
from datetime import *
import smtplib
global users
users = [ ]
with open("users.txt", "r") as File:
    users = File.readlines()
GRAPH_ID = "graph1"
TOKEN = "fghdhdhdhdhdhdhswu"
HEADERS = {
}
global USER_NAME
USER_NAME = ""
global PIXELA_ENDPOINT
PIXELA_ENDPOINT = "https://pixe.la/v1/"
global graph_endpoint
graph_endpoint = f"{PIXELA_ENDPOINT}/users/"
global graph_link
graph_link = ""


def no_nums(val):
    for character in val:
        if character.isdigit():
            return False
    return True


def how_works():
    print("Hello my name is Guru")
    print(", I am a habit tracker", end="")
    print("I use the Pixela API to help people track their habits")
    print("The Pixela API is extremely simple and easy to use, it allows you to record and track your habits in a "
          "visual manner that shows your progress")
    print("Please check out the following their website for a more deeoper look on how it works by clicking on the "
          "link below\n")
    print("https://pixe.la")


def create_user():
    user_name = str(input("Please enter the username that you want\n"))
    global USER_NAME
    USER_NAME = user_name
    token = str(input("Please enter the token that you want to authenticate you\n"))
    agree_service = str(input("Please type yes or no if you agree with Pixela's terms of service?\n")).lower()
    not_agree = ""
    while (agree_service == "no" and not_agree == ""):
        not_agree = input("Do you really not agree with the terms of service? If you say no then you are not allowed "
                          "to use this service, so choose carefully please type yes or no with regards to whetehr or "
                          "not you agree with Pixela's terms of service below?\n")
        if not_agree == "no":
            print("Since you decided not to agree with the terms of service, you cannot use my service.")
            exit()

    not_a_minor = str(input("Please type yes or no if you are a minor?\n")).lower()
    while (no_nums(not_a_minor) == False):
        print("Please only type yes or no, do not type any numbers")
        not_a_minor = str(input("Please type yes or no if you are a minor?\n")).lower()

    if (not_a_minor == "no"):
        print("Since you are a minor you cannot use this service goodbye now.").lower()
    USER_PARAMS = {
        "token": token,
        "username": user_name,
        "agreeTermsOfService": agree_service,
        "notMinor": not_a_minor,
    }
    email = input("Please type your full email\n")
    with open("users.txt", "a") as File:
        File.write(f"\n{user_name}:{email}")
    with open(f"{user_name}.txt", "a") as File:
        File.write("user_information\n")
        File.write(f"{token}\n")
        File.write(f"{user_name}\n")
    global graph_endpoint
    response = r.post(url="https://pixe.la/v1/users", json=USER_PARAMS)
    print(response.status_code)
    print(response.text)


# Create our graph:
""" graph_params = {
    "id": GRAPH_ID,
    "name": "Running Tracker",
    "unit": "km",
    "type": "int",
    "color": "sora",
}"""


def create_graph():
    user_name = str(input("What is your username?\n"))
    if (user_name not in users):
        print("The username that you entered is not valid, please try again")
        menu()
    id = str(input("Enter your graph id\n"))
    name = str(input("Enter your graph name\n"))
    unit = str(input("Enter your graph unit\n"))
    type = str(input("Enter your graph type(type int or float)\n")).lower()
    color = str(input("Enter your graph's color\n"))
    graph_params = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
    }
    global HEADERS
    with open(f"{user_name}.txt","r") as File:
         lines  = File.readlines()
         print(lines)
         HEADERS["X-USER-TOKEN"] = lines[1][0:len(lines[1])-1]
         print(HEADERS)
    with open(f"{user_name}.txt", "a") as File:
        File.write(f"\nid:{id}")
        File.write(f"\nname:{name}")
        File.write(f"\nunit:{unit}")
        File.write(f"\ntype:{type}")
        File.write(f"\ncolor:{color}")
    response = r.post(url=f"https://pixe.la/v1/users/{user_name}/graphs", json=graph_params, headers=HEADERS)

    HEADERS.clear()
    print(response.text)
    print(response.status_code)







def post_on_graph():
    '''
    This method adds a new pixel to your graph signifying that you completed
    you habit for whatever time interval you set. So for example if you wanted to run everyday
    you would add a new pixel everyday to show that you ran that day.
    :return:
    '''
    user_name = str(input("Please enter your username?\n"))
    global HEADERS
    with open(f"{user_name}.txt", "r") as File:
        lines = File.readlines()
        print(lines[1])
        HEADERS["X-USER-TOKEN"] = lines[1][0:len(lines[1])-1]

    today = str(datetime.today())
    today = today[0:10]
    today = today.replace("-", "")
    quantity = ""
    global GRAPH_ID
    GRAPH_ID = input("Plz enter your graph id\n")
    try:
        quantity = str(input("How many miles did you run today?\n"))
    except ValueError:
        print("Please only enter a number")
    pixel_params = {
        "date": today,
        "quantity": quantity,
    }
    response = r.post(url=f"{graph_endpoint}/{user_name}/graphs/{GRAPH_ID}", json=pixel_params,headers = HEADERS)
    print(response.status_code)
    print(f"https://pixe.la/v1/users/{user_name}/graphs/{GRAPH_ID}")





def profile():
    USER_NAME = input("please enter your username\n")
    endpoint = f"https://pixe.la/@{USER_NAME}"
    print(f"Go to this link to view your profile, {USER_NAME}\n")
    print(endpoint)


def menu():
    print("Here are your options type the number of what you want to do?")
    print("1.Create an account")
    print("2.Create a graph")
    print("3.Record a pixel on the graph")
    print("4.View your profile")
    option = int(input("What would you like to do? Type the number\n"))
    if option == 1:
        create_user()
    if option == 2:
        create_graph()
    if option == 3:
        post_on_graph()
    if option == 4:
        profile()
my_email = "jeremiah.bot@yahoo.com"
my_pass = "hiyhkysgjdgzicrl()"
with open("users.txt", "r") as File:
    lines = File.readlines()
    for x in range(len(lines)):
        if datetime.hour == 18:
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password = my_pass )
                connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com",
                msg=f"Subject: Time to record your habits"
            f"It is time to record your habits {lines[x]}, plz head over to repl in order to record them")

menu()
