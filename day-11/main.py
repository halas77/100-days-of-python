# To do

# - Do you wanna play a game of blackjack Type 'y' or 'n':

# - if y then, show your cards and score:, and computer's first card:

#  Type 'y' to get another card, type 'n' to pass:

#  if 'y' add another card and add in the prev, and show computers final hand, anf final score.

# - Back to the first line ...


import random


def choose_cards():
    cards  = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
    card1 = random.choice(cards)
    return card1

def add_cards(cards):
      return sum(cards)

def greater(num1, num2):
    if num1 > num2 and num1 < 22:
        print("Congragulations! You Won!!!")        
    elif num1 == num2:
        print("Draw!!!")
    elif num1 > 21 or num2 > num1: 
        print("Oooops! You Lose!!!")
   
   
def main_function():
    
    user = []
    computer = []

    for _ in range(2):
        user.append(choose_cards())
        computer.append(choose_cards())
    
    user_score = add_cards(user)
    computer_score = add_cards(computer)
    print(f"Your card: [{user[0]}, {user[1]}], current score: {user_score}") 
    print(f"Computer's card: {computer[0]}")
    
    
    user_want = input("Type 'y' to get another card, type 'n' to pass: ")
    
    if user_want == "y":
        user.append(choose_cards())
        user_score = add_cards(user)
        print(f"Your card: [{user[0]}, {user[1]}, {user[2]}], current score: {user_score}")
        print(f"Computer's card: [{computer[0]}, {computer[1]}], final score: {computer_score}")
        greater(user_score, computer_score)
        
        
    else:
        print(f"Your card: [{user[0]}, {user[1]}] current score: {user_score}")
        print(f"Computer's card: [{computer[0]}, {computer[1]}], final score: {computer_score}")
        greater(user_score, computer_score)
        
   
   
        
 
is_playing = True  
while is_playing:
    user_answer = input("Do you wanna play a game of blackjack Type 'y' or 'n': ")  
    if is_playing:
        main_function()    
    else:
        print("Thank You!! Have a nice day!")
        is_playing = False
            
        

        
         
        
        


        
    
     




