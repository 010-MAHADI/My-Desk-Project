class Student:
    roll = ""
    gpa = ""


rahim = Student()
print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.35
print(f"GPA = {rahim.gpa},ROLL = {rahim.roll}")



hasan = Student()
hasan.roll = 105
hasan.gpa = 4.00
print(f"GPA = {hasan.gpa},ROLL = {hasan.roll}")
