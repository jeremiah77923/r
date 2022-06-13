import smtplib
from random import *
from datetime import *
import pandas
Months = {1: "January", 2: "February", 3: "March", "April": 4, "May": 5, 6: "June", 7: "July", 8: "August",
          9: "September", 10: "October", 11: "November", 12: "December"}
my_email = "jeremiah.bot@yahoo.com"
my_pass = "hiyhkysgjdgzicrl()"
data = pandas.read_csv("birthdays.csv")
now = datetime.now()

global name
name = "name"
data_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
day = str(now.day)
def check():
    global name
    global data
    global now
    if (Months[now.month], day) in data_dict:
        return True
    return False



weekdays  = {0:"Monday",1:"Tuesday",2:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}


if check():
    name = "name"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com",
                            msg=f"Subject: {data_dict[(Months[now.month], day)][name]}Birthday Reminder\n\n{data_dict[(Months[now.month], day)][name]}'s "
                                f"birthday is in one week on {weekdays[now.weekday()]}, {Months[now.month]}, {day}")
