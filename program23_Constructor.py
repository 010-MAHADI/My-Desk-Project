"""class student:
    roll = ""
    gpa = ""
    def display(self,gpa,roll):
        self.roll=roll
        self.gpa=gpa
        print(f"Roll :{self.roll}\ngpa  :{self.gpa}")

rahaim = student()
rahaim.display(34.45,454)
"""

class Student:
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"ROLL = {self.roll},GPA = {self.gpa}")

rahim = Student(101,2.34)
rahim.display()

hasan = Student(102,3.95)
hasan.display()