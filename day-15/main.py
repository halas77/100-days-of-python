from data import MENU, resources 

def print_report(water, milk, coffee, money):
    print(f"Water: {water} ")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")
    
      
def cost_calculator(quarters, dimes, nickles, pennies):
    price = quarters * 0.25 + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return price


money = 0
corrent_water = resources["water"]
corrent_milk = resources["milk"]
corrent_coffee = resources["coffee"]

turnoff = False

while not turnoff:
    users_preffered_drink = input("What would you like? (espresso/latte/cappuccino): ")
    
    if users_preffered_drink == "report":
        print_report(corrent_water, corrent_milk, corrent_coffee, money)
            
    elif users_preffered_drink == "latte" or users_preffered_drink == "cappuccino":
        water = MENU[users_preffered_drink]["ingredients"]["water"]
        milk = MENU[users_preffered_drink]["ingredients"]["milk"] 
        coffee = MENU[users_preffered_drink]["ingredients"]["coffee"] 
        if corrent_water > water and corrent_milk > milk and corrent_coffee > coffee:
            print("Please insert coins.")
            quarters = float(input("How many quarters: "))
            dimes = float(input("How many dimes: "))
            nickles = float(input("How many nickles: "))
            pennies = float(input("How many pennies: "))
            
            price =  cost_calculator(quarters, dimes, nickles, pennies)
            
            
            if price >= MENU[users_preffered_drink]["cost"]:
                print(f"You can get {users_preffered_drink}.")
                money += price
                corrent_water -= water
                corrent_milk -= milk
                corrent_coffee -= coffee

                
            else:
                print("Your price cann't buy {users_preffered_drink}")
                
        else:
            print("Sorry you don't have enough water")
            
    elif users_preffered_drink == "espresso":
        water = MENU[users_preffered_drink]["ingredients"]["water"]
        coffee = MENU[users_preffered_drink]["ingredients"]["coffee"]
        if corrent_water > water and corrent_coffee > coffee:
            print("Please insert coins.")
            quarters = float(input("How many quarters: "))
            dimes = float(input("How many dimes: "))
            nickles = float(input("How many nickles: "))
            pennies = float(input("How many pennies: "))
            
            price =  cost_calculator(quarters, dimes, nickles, pennies)
            
            
            if price >= MENU[users_preffered_drink]["cost"]:
                print(f"You can get {users_preffered_drink}.")
                money += price
                corrent_water -= water
                corrent_coffee -= coffee
                                
            else:
                print("Your price cann't buy {users_preffered_drink}")
                
        else:
            print("Sorry you don't have enough water")
        
            
    elif users_preffered_drink == "off":
        turnoff = True
            
        

    
    
    
    
    
    

    

    
     
    
    

    