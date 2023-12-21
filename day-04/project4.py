import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"


combined = [rock, paper, scissors]

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")

user_input_as_int = int(user_input)

random_number = random.randint(0, 2)

computer = combined[random_number]





if user_input_as_int == random_number:
    print("Same Choices. No win No lose.")  
         
if user_input_as_int == 0 and random_number == 1:
    print("You lose.")
       
if user_input_as_int == 1 and random_number == 2:
    print("You lose.")
       
if user_input_as_int == 1 and random_number == 0:
    print("You Won.")
       
if user_input_as_int == 2 and random_number == 1:
    print("You Won.")
      
if user_input_as_int == 0 and random_number == 2:
    print("You won.") 
    
if user_input_as_int == 2 and random_number == 0:
    print("You lose.")

print(f"{random_number} and {user_input}")