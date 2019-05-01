from random import randint
import names

from racer import Racer

class Rider(Racer):
    def __init__(
        self,
        sex=None,
        name=None,
        age=None,
        stats=None,
        career=None
    ):
        super(Rider, self).__init__(
            sex=sex,
            name=name,
            age=age,
            stats=stats,
            career=career
        )
        self.stat1_long, self.stat1_short = "Control", "CTL"
        self.stat2_long, self.stat2_short = "", ""
        self.stat3_long, self.stat3_short = "", ""

    def generate_age(self):
        return randint(18,55)

    def generate_name(self):
        name = names.get_full_name(gender=self.sex_str)
        if randint(0,20) == 0:
            name += " Jr."
        return name

if __name__ == "__main__":
    r = Rider()
    print(r.print_details())
