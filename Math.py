import math


class mat():
    def __init__(self):
        self.options = """1.Add 
                          2.Subtract 
                          3.Multiply 
                          4.Divide
                          5.Square Root 
                          6.Square a number"""
        self.ops = {"plus": "+", "add": "+", "divided": "/", "multiply": "*", "times": "*", "divide": "/",
                    "subtract": "-", "minus": "-", "square root": "√", "squared": "**", "root": "√",
                    "mod": "%", "modulus": "%"}
        self.nums = []

    """ def order(self):
        final = []
        for x in range(len(self.nums)):
            if self.nums[x] == "/":
                final.append(self.nums[x - 1])
                final.append(self.nums[x])
                final.append(self.nums[x + 1])
            if self.nums[x] == "+":
                final.append(self.nums[x - 1])
                final.append(self.nums[x])
                final.append(self.nums[x + 1])
            if self.nums[x] == "-":
                final.append(self.nums[x - 1])
                final.append(self.nums[x])
                final.append(self.nums[x + 1])
        self.nums = final
        """

    def calculate(self):
        sum = float(0)
        current_num = 0
        prev_op = ""
        found_divs = False

        for x in range(len(self.nums)):
            if found_divs == False and "/" in self.nums:
                for x1 in range(len(self.nums)):
                    if self.nums[x1] == "/":
                        current_num = float(self.nums[x1 - 1])
                        temp = current_num / float(self.nums[x1 + 1])
                        sum = temp
                        self.nums[x1 + 1] = None
                        self.nums[x1 + 1] = None
            found_divs = True
            if self.nums[x] == "+":
                prev_op = "+"
                vals = self.nums[x - 1:x + 2]
                for x1 in range(len(vals)):
                    if vals[x1] != "+":
                        sum += float(vals[x1])
                if x >= len(self.nums):
                    break
            if self.nums[x] == "*":
                prev_op = "*"
                vals = self.nums[x - 1:x + 1]
                for x1 in range(len(vals)):
                    if vals[x1] != "*":
                        sum = float(vals[x1])
                        sum *= float(vals[x1])
                if x >= len(self.nums):
                    break
            if self.nums[x] == "%":
                prev_op = "%"
                prev_num = 0
                vals = self.nums[x - 1:x + 1]
                for x1 in range(len(vals)):
                    if vals[x1] != "%":
                        prev_num = vals[x1]
                    if vals[x1] != "%" and vals[x1] != prev_num and prev_num != 0:
                        sum = prev_num % vals[x1]

            if self.nums[x] == "-":
                prev_op = "-"
                vals = self.nums[x - 1:x + 2]
                prev_num = 0
                for x1 in range(len(vals)):
                    if vals[x1] != "-" and prev_num == 0:
                        prev_num = float(vals[x1])
                    if vals[x1] != "-" and prev_num != 0 and float(vals[x1]) != prev_num:
                        prev_num -= float(vals[x1])
                        sum = prev_num

                if x >= len(self.nums):
                    break
            if self.nums[
                x] == "√" and "/" not in self.nums and "+" not in self.nums and "-" not in self.nums and "*" not in self.nums and "%" not in self.nums:
                prev_op = "√"
                sum = math.sqrt(float(self.nums[x + 1]))

        return sum

    def m_d(self):
        sum = 0
        print("nums " + f"{ self.nums}")
        while "/" in self.nums or "*" in self.nums:
            for x in range(0, len(self.nums)):
                if self.nums[x] == "*":
                    vals = self.nums[x - 1:x + 1]
                    val1 = self.nums[x]
                    val2 = self.nums[x+1]
                    val3 = self.nums[x-1]
                    sum = float(val3)
                    sum*= float(val2)
                    print( sum)
                    self.nums.remove(val1)
                    self.nums.remove(val2)
                    self.nums.remove(val3)
                    self.nums.insert(x-1, sum)
                    break
                if self.nums[x] == "/":
                        vals = self.nums[x - 1:x + 1]
                        val1 = self.nums[x]
                        val2 = self.nums[x + 1]
                        val3 = self.nums[x - 1]
                        sum = float(val3)
                        sum /= float(val2)
                        print(sum)
                        self.nums.remove(val1)
                        self.nums.remove(val2)
                        self.nums.remove(val3)
                        self.nums.insert(x-1, sum)
                        print("after" + f"{ self.nums}")
                        break
                print("first " + f"{self.nums}")




        print(self.nums)




    def get_nums(self, txt):

        txt = txt.split(" ")
        print(txt)
        for x in range(len(txt)):
            try:
                current_num = int(txt[x])
                self.nums.append(str(float(current_num)))
            except ValueError:
                if txt[x].isdigit() == False and txt[x] != " " and txt[x] != "by" and txt[x] in self.ops:
                    self.nums.append(self.ops[txt[x]])
                continue
