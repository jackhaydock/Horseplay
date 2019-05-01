from random import randint
import textwrap
import tabulate

class Racer(object):

    def __init__(
        self,
        sex=None,
        name=None,
        age=None,
        stats=None,
        career=None
    ):
        self.sex = sex if sex else self.generate_sex()
        self.sex_str = 'male' if self.sex == 0 else 'female'
        self.name = name if name else self.generate_name()
        self.age = age if age else self.generate_age()
        self.s1, self.s2, self.s3 = stats if stats else self.generate_stats()
        self.career = career if career else self.generate_career()

    def generate_sex(self):
        sex = randint(0,1)
        return sex

    def generate_stats(self, points=100):
        s1 = randint(0, points)
        s2 = randint(0, points - s1)
        s3 = points - s1 - s2
        return [s1, s2, s3]

    def generate_career(self, races=randint(0,20)):
        skew = randint(0, races/2)
        first = randint(0, races - skew)
        second = randint(0, races - first)
        third = randint(0, races - first - second)
        lost = races - first - second - third
        return [first, second, third, lost]
