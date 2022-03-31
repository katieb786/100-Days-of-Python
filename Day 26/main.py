import random

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

range_list = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
capital_names = [name.upper() for name in names if len(name) > 4]


students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 70}
