from random import randint

from racer import Racer
from names import horse_names

class Horse(Racer):
    def __init__(
        self,
        sex=None,
        name=None,
        age=None,
        stats=None,
        career=None
    ):
        super(Horse, self).__init__(
            sex=sex,
            name=name,
            age=age,
            stats=stats,
            career=career
        )
        self.stat1_long, self.stat1_short = "Speed", "SPD"
        self.stat2_long, self.stat2_short = "Stamina", "STM"
        self.stat3_long, self.stat3_short = "Jumping", "JMP"

    def generate_age(self):
        return randint(2,11)

    def generate_name(self):
        surname, forename = self.generate_names(horse_names)
        return "%s %s" % (forename, surname)

if __name__ == "__main__":
    h = Horse()
    print(h.print_details())
