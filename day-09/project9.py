
def find_the_highest(bid):
    winner = 0
    winner_person = ""
    for item in bid:
        if bidders[item] > winner:
            winner = bidders[item]
            winner_person = item
            
    print(f"The winner is {winner_person} with a bid of ${winner}")

true = True

bidders = {}  
while true:
    bid_user = input("What is your name please? ")
    bid =  int(input("What is your bid? $"))
    bidders[bid_user] = bid
    user = input("Is there any other? Type 'yes' or 'no'. ").lower()
    
    if user == "no":        
        true = False
        find_the_highest(bidders)
        
        

                

            


            
            
        
    
    
    
    
    
    
    
    
    
    
    





