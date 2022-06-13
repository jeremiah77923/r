import smtplib

import requests
import math
my_email = "jeremiah.bot@yahoo.com"
my_pass = "hiyhkysgjdgzicrl()"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# Response codes tell us if our requests succeeded or failed.
# print(response.status_code)
if response.status_code != 200:
    response.raise_for_status()
ISS_data = response.json()
latitude = float(ISS_data["iss_position"]["longitude"])
longitude= float(ISS_data["iss_position"]["latitude"])
ISS_location = (latitude, longitude)
my_lng = -97.547089
my_lat = 30.542959
while True:
    time.sleep(60)
    if abs(my_lng - longitude)<=15 and abs(my_lat - latitude)<=15:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password = my_pass)
            connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com", msg="Subject: ISS "
                                                                                               "Alert\n\nThe ISS is "
                                                                                               "currently over your "
                                                                                               "location, look up in "
                                                                                               "the sky!")

