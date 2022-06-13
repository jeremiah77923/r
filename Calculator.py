from Art import logo

print(logo)
user_name = input("What is your name?\n")
print(f"Welcome to the Calculator, {user_name}")


def cal(op, num, value):

    if op == "+":
        return value + num
    elif op == "-":
        return value - num
    elif op == "*":
        return value * num
    elif op == "/":
        return value / num
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Please enter one of the operations from above.")
def calc():
    q = ""
    output = ""
    value = 0
    count = 0
    while q != "q":
        if q == "c":
            output = ""
            print("+\n-\n*\n/")
            op = input(
                f"Pick an operation from above to continue with {value}"
                f" type \"+\", or \"-\", or \"*\" or \"/\".\n")
            num1 = float(input("Enter another number?\n"))
            output += str(value)
            output += " "
            output += op
            output += " "
            output += str(num1)
            output += " "
            output += "="
            output += " "
            count += 1
            ca = cal(op=op, num=num1, value=value)
            value = ca
            output += str(ca)
            print(output)
        if count == 0:
            num1 = float(input("What is the first number?\n"))
            output += str(num1)
            output += " "
            print("+\n-\n*\n/")
            op = input("Pick an operation from above type \"+\", or \"-\", or \"*\" or \"/\".\n")
            output += op
            output += " "
            num2 = float(input("What is the second number? or type \"1\" to quit\n"))
            output += str(num2)
            output += " "
            output += "="
            output += " "
            if op != "+" and op != "-" and op != "*" and op != "/":
                print("Please enter one of the operations from above.")
            if op == "+":
                value = num1 + num2
                output += str(value)
                print(output)
            elif op == "-":
                value = num1 - num2
                output += str(value)
                print(output)
            elif op == "*":
                value = num1 * num2
                output += str(value)
                print(output)
            elif op == "/":
                value = num1 / num2
                output += str(value)
                print(output)
        q = input(f"Type c to continue calculating with {value}, q to quit, or k to do another calculation\n")
        if q == "k":
            count = 0
            output = ""


calc()
