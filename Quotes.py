import smtplib
import datetime as dt
from random import *

global adresses
# Email for sending messages from Python:
# Before the @ sign is your email identity so people
# know who sent messages, after the @ sign is your
# email service provider.
my_email = "jeremiah.bot@yahoo.com"
password = "hiyhkysgjdgzicrl()"
# Create a new smtp object:
# It is a way to connect to our email provider's smtp server.
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
quotes = []
import os

print(os.path.exists("Productivity/Motivational Quotes/quotes.txt"))

with open('quotes.txt', "r") as File:
    quotes = File.readlines()
    if now.weekday() == 1:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            # tls stands for transport layer security
            # and is a way for securing our connection to our email
            # server. If someone tries to intercept our email
            # they will not be able to read it because the email
            # will be highly encrypted and impossible to read  it's contents.
            # It will make our connection secure.
            connection.starttls()

            # Next thing we have to do is login
            # We have to provide a username and a password.
            # The username is the variable that holds your email
            # The password is the password for your email
            # contained in a variable.
            connection.login(user=my_email, password=password)

            # send the email you must specific the sender and the recipient, and must be case sensitive no typos!
            connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com",
                                msg=f"Subject:Monday Motivation\n\n{choice(quotes)}\nHave a great week, your stronger "
                                    f"than you know!")
            connection.close()
        # We have to close the connection when we send the email
