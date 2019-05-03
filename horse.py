import names
from random import randint

from racer import Racer
from adjectives import adjectives
from adverbs import adverbs
from nouns import nouns

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
        self.stat1_long, self.stat1_short = "Speed", "SPD" # Increase initial speed
        self.stat2_long, self.stat2_short = "Stamina", "STM" # Reduce loss of speed from legs
        self.stat3_long, self.stat3_short = "Jumping", "JMP" # Reduce loss of speed from jumps

    def generate_age(self):
        return randint(2,11)

    def generate_name(self):
        full_name = ""

        # Adverb
        if randint(0,10) == 0:
            full_name += "%s " % adverbs[randint(0,len(adverbs)-1)].strip().title()

        # Adjective
        full_name += "%s " % adjectives[randint(0,len(adjectives)-1)].title()

        # Name/Noun
        if randint(0,1) == 0:
            full_name += names.get_first_name(gender=self.sex_str)
        else:
            full_name += "%s " % nouns[randint(0,len(nouns))].title()

        return full_name

if __name__ == "__main__":
    h = Horse()
    print(h.print_details())
