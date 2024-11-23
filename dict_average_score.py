grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_students = list(students)
average_score = {}
for name_of_student, grade_average in zip(sorted(list_of_students), grades):
    average_of_score = sum(grade_average)/len(grade_average)
    average_score[name_of_student] = average_of_score
print(average_score)
