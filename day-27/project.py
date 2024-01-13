from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)


def km_converter():
    user_miles = int(input.get())
    km_result = round(1.6 * user_miles)
    result.config(text=km_result)
    

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

calculate = Button(text="Calculate", command=km_converter)
calculate.grid(column=1, row=2)

input = Entry(width=7)
input.grid(column=1, row=0)


window.mainloop()