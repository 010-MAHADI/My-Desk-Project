# Magic methods
class Bike:
    # Magic methods
    def __init__(self,name,color):
        self.name = name
        self.color = color

    # Magic methods
    def __str__(self):
        return(f"Name  ={self.name} \nColor ={self.color}")

    # Magic methods
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def display(self):
        print(f"Name  ={self.name} \nColor ={self.color}")

bike1 = Bike("Fz29", "Black")

bike2 = Bike("Fz26", "Blue")

print(bike1==bike2)

print(bike1)