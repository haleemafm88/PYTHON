attendence=[18,20,19,15,21]
full_day=0
total_student=0
for students in attendence:
    if students >=20:
        print("full")
        full_day=full_day+1
    else:
        print("not full")
    total_student=total_student+students
print("number of fulldays:",full_day)
print("total attendence for 5 days:",total_student)