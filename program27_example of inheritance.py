class shape:
    def __init__(self,width,hidth):
        self.hidth = hidth
        self.width = width
    def area(self):
        print("Shape class")

class tryangle(shape):
    def area(self):
        area = 0.5 * self.hidth * self.width
        print(f"area of tryangle:{area}")

class recttryangle(shape):
    def area(self):
        area = self.hidth * self.width
        print(f"area of recttryangle:{area}")



t1 = tryangle(32,43)
t1.area()

r1 = recttryangle(43,14)
r1.area()