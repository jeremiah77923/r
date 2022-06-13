import random
user_name = input("What is your name?\n")
print("Welcome to the Password Generator, " + user_name)
letters = int(input("How many letters would like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))
password = []
pas = ""
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
Password = []
for i in range(0, letters):
    random1 = random.randint(0, len(Letters) - 1)
    password.append(Letters[random1])
for i in range(0, symbols):
    random2 = random.randint(0, len(Symbols) - 1)
    password.append(Symbols[random2])
for i in range(0, numbers):
    random3 = random.randint(0, len(Numbers) - 1)
    password.append(Numbers[random3])
random.shuffle(password)
p = ""
for ele in password:
    p+=ele
print("Your password is: " + p)
