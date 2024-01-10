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



import pandas
data = pandas.read_csv("weather-data.csv")   
temp_list = data["temp"].to_list()
avg = sum(temp_list)/len(temp_list)
print(round(avg, 2))  