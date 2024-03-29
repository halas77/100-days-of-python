from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ------------------------- PASSWORD GENERATOR ---------------------------- #
def generate_password():
#Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0: 
        messagebox.showinfo(title="Oops.", message="Please don't insert empty field!")
         
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Here is the detail:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        
        if is_ok:
            with open("./day-29/data.txt", "a") as data:  
                data.write(f"{website} | {email} | {password} \n")   
                website_input.delete(0, END)
                password_input.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="./day-29/logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "dawit@gmail.com")

password_input = Entry(width=17)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
