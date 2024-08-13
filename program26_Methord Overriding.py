
class phone:
    def __init__(self):
        print("i am in phone class")

class samsung(phone):
    def __init__(self):
        super().__init__()
        print("i am in sumsung class")

h = samsung()
