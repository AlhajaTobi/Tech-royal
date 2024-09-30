"""
collect scores of student from user.

store each scores as scores_of_students

get the total number of students

store as total_number_of_student

then divide scores with total_number_of_student.

display result as average of the score.
"""
total = 0
score_counter = 0
scores = [20,30,35,25.40,45,50,60,55,60]

for score in scores:
    total += score
    score_counter += 1

average = total/score_counter
print(f'class average is {average}')
    

