import smtplib
import datetime as dt
import random

my_email = "dawitmellese23@gmail.com"
password = "1234abcd()"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(my_email, password)

data_of_birth = dt.datetime(year=2000, month=1, day=12)

print(data_of_birth)


with open("./day-32/quotes.txt") as file:
    all_data = file.readlines()
    data = random.choice(all_data)
    

now = dt.datetime.now()

if now.weekday() == 0:

    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email, msg=f"Subject:Boom!\n\n {data}"
    )
    connection.close()
    
else:
    print("Not monday")


