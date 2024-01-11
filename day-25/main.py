# with open("weather-data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)
# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []   
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temprature.append(int(row[1]))
# print(temprature)
# import pandas
# data = pandas.read_csv("weather-data.csv")   
# # temp_list = data["temp"].to_list()
# # avg = sum(temp_list)/len(temp_list)
# # max = data["temp"].max()
# # print(max)  

# max_row = data[data["temp"] == data["temp"].max()]
# to_F = 9/5 * max_row.temp + 32
# print(to_F)
# 9/5 * C + 32 

import pandas

data = pandas.read_csv("./227 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

my_data = {
    "color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}


df = pandas.DataFrame(my_data)

data_csv = df.to_csv("new_df.csv")



