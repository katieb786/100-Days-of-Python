# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].tolist()
# # print(temp_list)
# #
# # # average = sum(temp_list) / len(temp_list)
# # # rounded_average = round(average, 2)
# # # print(rounded_average)
# #
# # print(data["temp"].mean())
#
# # max_temp = data["temp"].max()
# #
# # # print(data.condition)
# #
# # # Get Data in Row
# #
# # # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# f = 9.0/5.0 * monday.temp + 32
# print(f)
#
# # Create DataFrame from Scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")

# Squirrel Data
import pandas
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = squirrel_data["Primary Fur Color"]
gray = 0
black = 0
cinnamon = 0
for color in squirrel_color:
    if color == "Gray":
        gray += 1
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1

print(gray, black, cinnamon)

color_dict = {
    "color": ["Gray", "Black", "Cinnamon"],
    "count": [gray, black, cinnamon]
}
color_data = pandas.DataFrame(color_dict)
color_data.to_csv("squirrel_count.csv")
