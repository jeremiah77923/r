import pandas

gray_count = 0
red_count = 0
black_count = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data.PrimaryFurColor
for color in colors:
    if color == "Gray":
        gray_count+=1
    elif color == "Red":
        red_count+=1
    elif color == "Black":
        black_count+=1
print(gray_count)
print(red_count)
print(black_count)
data_dict = {"fur color":["gray", "red", "black"], "number":[gray_count, red_count, black_count]}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel.csv")