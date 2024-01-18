import smtplib

my_email = "dawitmellese23@gmail.com"
password = "1234abcd()"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="dawitm777@gmail.com", msg="Subject:Hello\n\nThis is the body section"
)