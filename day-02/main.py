# Data Type, Data Conversion
print("hello"[4])

# Excercise 1 - Day - 02

input_number = input("Type a two digit number: ")  # 39

first_num = input_number[0]
second_num = input_number[1]

print(int(first_num) + int(second_num))


print(3 * (3 + 3) / 3 - 3)

# Body mass Index

height = float(input("enter your height in m: ")) 
weight = float(input("enter your weight in kg: "))

bmi = (weight/height**2)

print(int(bmi))

# Rround Function
print(round(2.666666, 5))

age = int(input("What is your current age? "))

new_age = 90 - age

days = new_age * 365

weeks = new_age * 52

months = new_age * 12

print(f"You have {days} days, {weeks} weeks, {months} months")

