def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}




def calculator():

    num1 = int(input("What is the first number? "))
    is_calculating = True
    while is_calculating:
        for i in operations:
            print(f"{i}")
        operations_symbol = input("Pick One symbol: ")
        num2 = int(input("What is the second number? "))
        function = operations[operations_symbol]
        answer = function(num1, num2)       
        print(f"{num1} {operations_symbol} {num2} = {answer}")        
        user_want = input("Do you wanna continue: 'y' or 'n': ")
        
        if user_want == "y":
            num1 = answer
        else:
            is_calculating = False
            calculator()
    
    
calculator()








