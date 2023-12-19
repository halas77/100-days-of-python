print("Welcome to Treasure Island.")

dir = input("Where do you go? Left or Right")


new_dir = dir.lower()

if new_dir == "left":
    lake = input("Wait or Swim? ")
    new_lake = lake.lower()
    
    if new_lake == "wait":
        color = input("Yellow, Blue or Red? ")
        new_color = color.lower()
        
        if new_color == "yellow":
            print("You Win!")
            
        else:
            print(f"You choose {new_color}, So You Faild!")
            
    else:
        
        print(f"You choose {new_lake}, So You Faild!")
        
else:
    print(f"You choose {new_dir}, So You Faild!")
    
        
        
        
        
        
        
        
    
    
    
    
    
    
    
