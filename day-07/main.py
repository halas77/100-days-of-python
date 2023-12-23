import random
import constants


chosen_word = random.choice(constants.word_lists)
display = []

for i in range(0, len(chosen_word)):
    display += "_"
    
print(f"The word is {chosen_word}")    
print(display)


end_of_game = False
the_guy = 6

while not end_of_game:
    guessed_letter = input("Please choose a letter? ")
    for i in range(0, len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            display[i] = guessed_letter
            print("Congragulations! You have got a letter.")
            print(display)
              
    if guessed_letter not in chosen_word:
        print("You have chose wrong letter!")
        print(constants.stages[the_guy])
        the_guy -= 1
        
        if the_guy == 0:
            print(constants.stages[0])
            end_of_game = True
            print("Game Over. You lose!")         
    
    if "_" not in display:
        end_of_game = True
        print("You win")
        
     
    


    
        





