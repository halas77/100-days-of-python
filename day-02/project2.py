print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

new_total_bill = float(total_bill)

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

percentage = float(percentage)

split =  input("How many people to split the bill? ")

split = float(split)

new_percentage = percentage / 100 + 1

result = (new_total_bill / split) * new_percentage

rounded_result = round(result, 2)

print(f"Each person should pay: ${rounded_result}") 

