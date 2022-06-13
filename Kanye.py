import requests
import smtplib

my_email = "jeremiah.bot@yahoo.com"
my_pass = "hiyhkysgjdgzicrl()"
response = requests.get(url="https://api.kanye.rest")
if response.status_code != 200:
    response.raise_for_status()
quote = "quote"
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="jeremiahhawthorne828@gmail.com", msg=f"Subject: Daily Kayne "
                                                                                               f"Quote\n\n \""
                                                                                               f"{response.json()[quote]}"
                                                                                               f"\""
                                                                                               f" - Kayne West")
