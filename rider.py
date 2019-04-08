from random import randint
import textwrap

from racer import Racer
from names import rider_names


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
        return randint(20,60)

    def generate_name(self):
        forename, surname = self.generate_names(rider_names)
        return "%s %s" % (forename, surname)

if __name__ == "__main__":
    r1 = Rider()
    print(r1.print_stats())
