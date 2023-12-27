# To do

# - Do you wanna play a game of blackjack Type 'y' or 'n':

# - if y then, show your cards and score:, and computer's first card:

#  Type 'y' to get another card, type 'n' to pass:

#  if 'y' add another card and add in the prev, and show computers final hand, anf final score.

# - Back to the first line ...


import random

cards  = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]

def choose_cards():
    card1 = random.choice(cards)
    return card1

def add_cards(num1, num2):
    sum = num1 + num2   
    return sum

def greater(num1, num2):
    if num1 > num2 and num1 < 22:
         print("Congragulations! You Won!!!")        
    elif num1 == num2:
        print("Draw!!!")
    elif num1 > 21 or num2 > num1: 
        print("Oooops! You Lose!!!")
        
 
is_playing = True  
while is_playing:
    user_answer = input("Do you wanna play a game of blackjack Type 'y' or 'n': ")  
    if is_playing:    
        user_card1 = choose_cards()
        user_card2 = choose_cards()
        user_score = add_cards(user_card1, user_card2)
        
        print(f"Your card: [{user_card1}, {user_card2}], current score: {user_score}") 
        computer_card1 = choose_cards()
        computer_card2 = choose_cards()
        computer_score = add_cards(computer_card1, computer_card2)
        
        print(f"Computer's card: {computer_card1}")
        
        
        user_want = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if user_want == "y":
            user_card3 = choose_cards()
            user_score = add_cards(user_score, user_card3)
            print(f"Your card: [{user_card1}, {user_card2}, {user_card3}], current score: {user_score}")
            print(f"Computer's card: [{computer_card1}, {computer_card2}], final score: {computer_score}")
            greater(user_score, computer_score)
            
            
        else:
            print(f"Your card: [{user_card1}, {user_card2}] current score: {user_score}")
            print(f"Computer's card: [{computer_card1}, {computer_card2}], final score: {computer_score}")
            greater(user_score, computer_score)
        
    else:
        print("Thank You!! Have a nice day!")
        is_playing = False
            
        

        
         
        
        


        
    
     




