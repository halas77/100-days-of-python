
#  Functions

# def greet():
#     print("Hello Dawit Mellese.")
#     print("Hello python coder.")
#     print("Hello Digital Marketer.")

# greet()


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"Hello {location}")
    

# greet_with("Dawit", "Addis Ababa" ) 


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"Hello {location}")
    

# greet_with(name="Dawit", location="Addis Ababa" )  

# import math 


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
#     no_of_can = math.ceil((height * width) / cover)
#     print(f"You'll need {no_of_can} cans of paint.")  
    

# paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Number Checker


def prime_checker(number):
    
    if number == 2:
        print("The number is prime.")
    
    for i in range(2, number):
        if number % i == 0:
            print("The number is not prime.")
            break
            
        else:
            print("The number is prime.")
            break



n = int(input("Check this number: "))
prime_checker(number=n) 

    