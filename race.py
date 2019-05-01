from random import randint, shuffle
import textwrap
from tabulate import tabulate

from pair import Racing_Pair
from track import Track

class Race():
    def __init__(
        self,
        track=None,
        num_racers=None,
        racers=None,
    ):
        self.track = track if track else Track()
        self.num_racers = num_racers if num_racers else self.generate_num_racers()
        self.racers = racers if racers else self.generate_racers(self.num_racers)
        self.calculate_odds()

    def generate_num_racers(self):
        return randint(2,8)

    def generate_racers(self, num_racers):
        racers = []
        i = 0
        while i < num_racers:
            racers.append(Racing_Pair(i + 1))
            i += 1
        return racers

    def calculate_odds(self):
        total_score = 0
        for pair in self.racers:
            pair.calculate_score(self.track)
            total_score += pair.score
        for pair in self.racers:
            pair.odds = total_score / pair.score

    # TODO design properly
    def start_race(self):
        positions = self.racers[:]
        shuffle(positions)
        return positions

    def print_details(self):
        str = self.track.name
        str += "\n"
        str += tabulate(self.track.print_details(), tablefmt="plain")
        str += ("\nRacing Pairs: %d\n" % self.num_racers)

        table = [
            [
            # self.number,
            "",
            "Name",
            "Age",
            "Sex",
            "{}/{}".format(self.racers[0].rider.stat1_short, self.racers[0].horse.stat1_short),
            "{}/{}".format(self.racers[0].rider.stat2_short, self.racers[0].horse.stat2_short),
            "{}/{}".format(self.racers[0].rider.stat3_short, self.racers[0].horse.stat3_short),
            "1st",
            "2nd",
            "3rd",
            "Lost",
            "Odds",
            ]
        ]
        for pair in self.racers:
            table += pair.print_details()
        str += tabulate(table)
        return str

if __name__ == "__main__":
    r = Race()
    print(r.print_details())
    print(r.start_race())
