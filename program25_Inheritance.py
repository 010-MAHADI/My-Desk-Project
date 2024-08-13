class phone:
    def call(self):
        print("you can call")
    def massage(self):
        print("you can massage")

class apple(phone):
    def photos(self):
        print("you can take photos")

T = apple()
T.call()
T.massage()
T.photos()
