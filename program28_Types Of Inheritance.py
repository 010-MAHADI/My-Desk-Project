# 3 types of Inheritance

# 2.Multi-Level Inheritance
class A:
    def display1(self):
        print("I am in a class")
class B(A):
    def display2(self):
        print("I am in b class")
class C(B):
    def display3(self):
        print("I am in c class")

du = C()
du.display1()
du.display2()
du.display3()


# 3.Multiple Inheritance

class A:
    def display(self):
        print("I am in a class")
class B:
    def display(self):
        print("I am in b class")
class C(A,B):
    def display(self):
        print("I am in c class")

du = C()
du.display()