# def format_name(f_name, l_name):
#     name = f_name + " " + l_name
#     return name.title()  



# f_name = input("Plese input the first name: ")
# l_name = input("Plese input the last name: ")

# name = format_name(f_name, l_name)

# print(name)


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if is_leap(year):
      month_days[1] = 29
      return month_days[month - 1] 
  else:
      return month_days[month - 1]

      
    
       
   
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)















    