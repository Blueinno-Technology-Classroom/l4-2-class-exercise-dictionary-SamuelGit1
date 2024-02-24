##################################################
'''
Q1: 
'''

sample_dict = {
   "name": "Hermione",
   "marks": {
       "transfiguration": 90,
       "charms": 98,
       "potions": 98,
       "history of magic": 92,
   }
}
print(sample_dict["marks"]["history of magic"])

##################################################
'''
Q2:
'''

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict["emp3"]["salary"] = 8500

##################################################
'''
Q3:
'''

mystery_pokemon = {
     "height": 15,
     "weight": 405,
     "moves": [
         {
             "name": "lick",
             "level_learned_at": 0
         },
         {
             "name": "nightmare",
             "level_learned_at": 0
         },
         {
             "name": "curse",
             "level_learned_at": 16
         }
     ]
}
print(f'It can learn "curse" at level {mystery_pokemon["moves"][2]["level_learned_at"]}.')

##################################################
'''
Q4:
'''

student_scores = {
    "Harry": 81, 
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62
}

##################################################
'''
Q5a:
'''

for key, val in student_scores.items():
   print(f"key: {key}, value: {val}")

##################################################
'''
Q5b:
'''

minimum = 100
student = ""
for key, val in student_scores.items():
    if minimum > val:
        minimum = val
        student = key
print(f"The student with the lowest score is {student} and their score is {minimum}.")
    
##################################################
'''
Q6:
'''

student_grades = {}

for key, val in student_scores.items():
    if val > 90:
        student_grades[key] = "Outstanding"
    elif val > 80:
        student_grades[key] = "Exceeds Expectations"
    elif val > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

##################################################
'''
Q7:
'''

keys = ['Harry', 'Ron', 'Hermione']
values = ['B', 'C', 'A']

merge_dict = dict(zip(keys, values))

##################################################
