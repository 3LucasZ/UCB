class Object:
    height = 1
    def __repr__(self):
        return f'height:{self.height}'
class Human(Object):
    height = 2
    def __repr__(self):
        return super().__repr__
class Soldier(Human):
    height = 3

object = Object()
human = Human()
soldier = Soldier()

print(object, human, soldier)

