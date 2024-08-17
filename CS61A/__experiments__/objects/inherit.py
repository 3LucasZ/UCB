class Object:
    height = 1
    def __repr__(self):
        return f'height:{self.height}'
class Human(Object):
    def __init__(self):
        self.height += 1
    def __repr__(self):
        return super().__repr__()
class Soldier(Human):
    height = 3
    def __init__(self):
        Object.height = 4



print(Object.height, Human.height, Soldier.height)
object = Object()
object.height = 100
human = Human()
soldier = Soldier()
print(Object.height, Human.height, Soldier.height)
print(object, human, soldier)

