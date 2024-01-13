# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = 'dawit'
# name_in_letter = [letter for letter in name]
# print(name_in_letter)

# double_list = [2 * num for num in range (1, 5)]
# print(double_list)

# names =['dawit', 'mellese', 'tsehay', 'beza', 'marta']

# long_names_uppercase = [name.upper() for name in names if len(name) > 5]

# print(long_names_uppercase)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
# result = [num for num in numbers if num % 2 == 0]
# print(result)


# with open("./day-26/file1.txt") as file1:
#     data1 = file1.readlines()
    
# with open("./day-26/file2.txt") as file2:
#     data2 = file1.readlines()
      
# result = [num for num in data1 if num in data2 ]    

 
# print(result)

# sentence = "What is the airspeed velocity of an unladen sawallow?"
# result = {word:len(word) for word in sentence.split()} 


# print(result)

weather_data = {
    "Monday": 12,
    "Tuesday": 14,
    "Wendsday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Subday": 24,   
}


result = {day:value * 9/5 + 32 for (day, value) in weather_data.items()}


print(result)







