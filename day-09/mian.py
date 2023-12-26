# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades= {}

# for student in student_score:
#     if student_score[student] > 90:
#         student_grades[student] = "Outstanding"
    
#     elif student_score[student] > 80:
#         student_grades[student] = "Exceeds Expectations"
        
#     elif student_score[student] > 70:
#         student_grades[student] = "Acceptable"
        
#     else:
#         student_grades[student] = "Fail"
        
# print(student_grades) 


# travel = {
#     "france": {"visited": "lille"},
#     "german":{"visited": ["berlin", "hamburg", "stuttgart"], "total_visit": 10}
    
# }


travel = [
    {
        "country" : "France",
        "visted" : 12,
        "cities" : ["Paris", "Lille", "Dijon"] 
    },
    {w
        "country" : "Germany",
        "visted" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"] 
    }
]

def add_new_country(country, visits, cities ):
    
    new_dic = {}
    
    new_dic["country"] = country
    new_dic["visited"] = visits
    new_dic["cities"] = cities
    
    travel.append(new_dic)
     
add_new_country("Russia", 2, ["Moscow", "Saint petersperg", "Test"])
print(travel)






