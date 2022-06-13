from Art import logo

print(logo)
print(f"Welcome to the secret auction!!!")
more_people = ""

people = {}

clear = '''
-------------------------------
-----------------------------
------------------------------------------------------------
-----------------------------
------------------------------------------------------------
-----------------------------
------------------------------------------------------------
-----------------------------
------------------------------------------------------------
-----------------------------
-----------------------------
'''


def addPerson(name, bid):
    people[name] = bid


def lines():
    for i in range(500000):
        print(clear)


count = 0
while True:
    user_name = input("What is your name?\n")
    bid = int(input("What is your bid in $\n$"))
    addPerson(name=user_name, bid=bid)
    more_people = input("Type \"yes\" if there is another person who wishes to bid, "
                        "or type \"no\" if there is no one else.\n")
    count += 1
    if more_people.lower() == "yes":
        lines()
        print("Ok plz hand the device off to the next bidder")
    if count == 1 and more_people.lower() == "no":
        print(f"You were so the only one who placed a bid, so your bid of{people[user_name]} won congrats!!")
        break
    if count > 1 and more_people.lower() == "no":
        break
winner = " "
bid = 0

for key in people:
    if len(people) > 1:
        if people[key] > bid:
            winner = key
            bid = people[key]
if len(people) > 1:
    print(f"The winner was {winner}, with a bid of {bid}$ congrats{winner}!!!")
