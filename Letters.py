# You can also update names.txt and letter.txt id you wish
# to send a different message to different people.
names = []
day_of_week = input("What is the day of the week of the birthday party?\n")
day = input("What is the calendar date of the day? The number of the day on a calendar?\n")
month = input("What is the month of the birthday party?(the name like January not the number of the month?\n")
time = input("When does the party start?\n")
day_time = input("Is it in the AM or PM?\n").upper()
location = input("Where is the party give the name of the place like \"chucky cheese\"?\n")
address = input("Give the address for the building where the party is?\n")
with open("input/names.txt", "r") as File:
    for line in File:
        line.strip()
        names.append(line)
print(names)
for x in range(len(names)):
    with open("input/letter.txt") as file:
        names[x] =  names[x].strip()
        letter_contents = file.read()
        letter_contents.strip()
        letter_contents = letter_contents.replace("[name]",  names[x])
        letter_contents = letter_contents.replace("[day_of_week]", day_of_week)
        letter_contents = letter_contents.replace("[month]", month)
        letter_contents = letter_contents.replace("[day]", day)
        letter_contents = letter_contents.replace("[time]", time)
        letter_contents = letter_contents.replace("[day_time]", day_time)
        letter_contents = letter_contents.replace("[description]", location)
        letter_contents = letter_contents.replace("[address]", address)
        filename = f"letter_{names[x]}.txt"
    with open(f"letters/{filename}", "w") as file:
        file.write(letter_contents)
