import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

print("welcome to teh PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password? \n"))

nr_symbols = int(input("How many symbols would you like in your password? \n"))

nr_number = int(input("How many number would you like in your password? \n"))

password = []

for i in range(0, nr_letters):
    password += random.choice(letters)
    
for j in range(0, nr_symbols):
    password += random.choice(symbols)
    
for k in range(0, nr_symbols):
    password += random.choice(number)
    

# Shuffle the list of characters
random.shuffle(password)

suffled = ''

for i in password:
    suffled += i
    

# Join the shuffled characters to form a new password

print("Original Password:", password)
print("Shuffled Password:", suffled) 
    
    
    






