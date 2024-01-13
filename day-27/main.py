# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
        
#     return sum

# num_sum = add(1, 2, 6, 7, 45, 567, 43) 
# print(num_sum)

import tkinter

window = tkinter.Tk()
window.title("Python Graphics")
window.minsize(500, 300)

#  Label
text = tkinter.Label(text="Hello Dawit")
text.grid(column=0, row=0) 

   
# Input
button = tkinter.Button(text="Submit here")
button.grid(column=1, row=1)

# Button
def handle_button():
    getted = input.get() 
    text["text"] = getted

button = tkinter.Button(text="Click here", command=handle_button)
button.grid(column=2, row=0)

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()


