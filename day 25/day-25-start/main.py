# with open("weather_data.csv", mode = "r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas 

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# total = 0

# for i in temp_list:
#     total += i

# average = total / len(temp_list)
# print(average)

# print(data["temp"].max())

# print(data[data.day == "Monday"])

# lowest_degree = data["temp"].min()
# print(data[data.temp == lowest_degree])

# monday = data[data.day == "Monday"]
# print(monday.condition)

#Monday'in temp'i fahrenheit şeklinde istiyo

# temp = monday.temp
# f_temp = (temp * 1.8) + 32
# print(temp)
# print(f_temp)

#Creating dataframe from stratch 

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [34, 45, 66]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_NYC_Squirrel_Data.csv")
Gray = len(data[(data["Primary Fur Color"] == "Gray")])
Cinnamon = len(data[(data["Primary Fur Color"] == "Cinnamon")])
Black = len(data[(data["Primary Fur Color"] == "Black")])
Empty = len(data[(data["Primary Fur Color"].isna())])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray, Cinnamon, Black]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)

new_data.to_csv("Squirrel_Count.csv")

