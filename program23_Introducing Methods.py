class Student:
    roll = ""
    gpa = ""
    def ontry(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"ROLL = {self.roll},GPA = {self.gpa}")

rahim = Student()
rahim.ontry(101,2.34)
rahim.display()

hasan = Student()
hasan.ontry(102,3.95)
hasan.display()