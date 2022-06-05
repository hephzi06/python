# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("Draw")
#
#
# point = Point(10, 10)
# print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("Hephzi")
john.talk()

bob = Person("Bob")
bob.talk()