# Created by Jeremiah Hawthorne
# Python Tip Calculator:
# Began on Thursday June 10th
# Finished on Thursday June 10th
# Day 2 of 100 days of Python coding

# Ask the user for their name
userName = input("What is your first name?\n")
# Greet the user
print("Hello and welcome to the tip calculator, " + userName)

# Ask the user the total bill in a good looking format
total = float(input("What was the total bill today?(type the dollar amount below):\n$"))
# Ask the user whether or not they want to do a percent tip or a dollar amount
typeOfTip = input("Do you want to do a tip as a percentage(type \"%\" if so) or dollar amount(type \"$\" if so)?\n")
# Ask the user what percent tip they want to do
if typeOfTip == "%":
    percentTip = int(input("What percentage tip would you like to give?(type the number like \"8\" for 8%) \n%"))
# Ask the user what dollar amount they want to give
elif typeOfTip == "$":
    dollarTip = float(input("What amount do you want to give for your tip? \n$"))
# Ask the user how many people are splitting the bill
isSplitting = input("Type \"yes\" if you are splitting the bill, or \"no\" if you are not splitting the bill.\n")
# Initialize the tip variable so we can reassign it to the actual tip value
tip = 0
# Runs if and only if the user choose percent as their tip type
if typeOfTip == "%":
    # Calculate the tip percent
    tip = percentTip / 100

    # Calculate the tip amount
    amountTip = total * tip

    # Add the tip to the total bill
    totalWithTip = total + amountTip

    if isSplitting.upper() == "YES":
        numOfPeople = int(input("How many people are splitting the bill?(type below the total number of people who "
                                "wish to split the bill):\n"))
        print("The total bill is $" + str(round(totalWithTip, 2)))
        print("Each person should pay " + str(round(totalWithTip / numOfPeople, 2)) + "$")

    # Output the total bill in a nice format rounded to decimal places if the user does not want to split it
    elif isSplitting.upper() == "NO":
        print("Your total bill is $" + str(round(totalWithTip, 2)))
if typeOfTip == "$":
    # Set the tip equal to the dollar amount the user gave
    tip = dollarTip
    # Add the tip to the bill so we can calculate the final bill for the user.
    total += tip
# Runs if and only if the user said that the bill as being split
    if isSplitting.upper() == "YES":
        # Asks the user how many people are splitting the bill.
        numOfPeople = int(input("How many people are splitting the bill?\n"))
        # Outputs the total bill
        print("The total bill is: $" + str(round(total, 2)))
        # Outputs what each person should pay
        print("Each person who is splitting the bill should pay: " + str(round(total / numOfPeople, 2)) + "$")
# Runs if the user did not say that they will splitting the bill,
# and if the user said that they are not splitting the bill.
elif isSplitting.upper() == "NO":
    # Outputs the total bill for the user.
    print("Your total bill is: $" + str(total))

# Created by Jeremiah Hawthorne
# Python Tip Calculator:
# Began on Thursday June 10th
# Finished on Thursday June 10th
# Day 2 of 100 days of Python coding bootcamp
