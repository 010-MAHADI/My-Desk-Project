class Triangle():
    def __init__(self,hight,base):
        self.hight = hight
        self.base = base
    def area_calculate(self):
        area = 0.5 * self.base * self.hight
        print(f"Area = {area}")

T1 = Triangle(20,34)
T1.area_calculate()

t5 = Triangle(34,43)
t5.area_calculate()

