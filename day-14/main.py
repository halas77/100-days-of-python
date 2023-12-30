#  import random module, art, data
import random
from art import logo, vs
from data import data

# a funtion which compare two items and return the answer

print(logo)


def Comparator(guess, item1, item2):
    if item1["follower_count"] > item2["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"
    
    
# choose random objects from data

def Chooser(sample_data):
    object = random.choice(sample_data)
    return object


def game_starter(object1, object2):
        
    print(f"Compare A: {object1["name"]}, a {object1["description"]},  from {object1["country"]}")
    
    print(vs)
    
    print(f"Against B: {object2["name"]}, a {object2["description"]},  from {object2["country"]}")
    

game_over = False

object1 = Chooser(data)
object2 = Chooser(data)

score = 0

while not game_over:
   
    if score > 0:
        print(f"Your score is {score}")

    game_starter(object1, object2)
        
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    correct_answer = Comparator(user_answer, object1, object2)

    if correct_answer:
        score += 1
        object1 = object2
        object2 = Chooser(data)
    else:
        print(f"Your Final score is {score}")
        game_over = True
    
    
