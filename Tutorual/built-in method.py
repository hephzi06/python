import random


# for i in range(3):
#     print(random.randint(1000000000, 9999999999))


# members = ['John', 'Mary','Bob', 'Hephzi']
# print(random.choice(members))


# class Dice:
#
#     def roll(self, rolled):
#         self.rolled = rolled
#
#         print(rolled)
#
#
# dices = Dice()
# dices.roll(rolled=(random.randint(1, 6), random.randint(1, 6)))


"""Mosh exampes"""


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())
