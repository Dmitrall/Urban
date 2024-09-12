grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
grades_students = list(map(lambda grades: sum(grades) / len(grades), grades))
students_evaluations = dict(zip(sorted_students, grades_students))
print(students_evaluations)