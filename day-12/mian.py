# Welcome page, intro to the game, choose difficulty
import random

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

EASY = 10
HARD = 5



def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY
    else:
        return HARD


def game():
    answer = random.randint(0, 100)
    life = set_difficulty() 
    while life > 0:
        if life !=5 and life != 10:
            print("Guess Again!")          
        print(f"You have {life} attempts remaining to guess the number")        
        guess = int(input("Make a guess: "))
           
        if guess == answer:
            print("You got it.")
            life = -1
        elif guess >= answer:
            life -=1
            print("Too high.")
        elif guess <= answer:
            life -=1
            print("Too Low")
    if life == 0:      
        print("You've run out of guesses, you lose.")      

game()







