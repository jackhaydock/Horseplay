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
            total_score += pair.odds_score
        for pair in self.racers:
            pair.odds = total_score / pair.odds_score

    def start_race(self):

        # Define initial score at begining of race
        positions = self.racers[:]
        for pair in positions:
             pair.race_score = (pair.horse.s1 * 10) + (pair.rider.s1 * 10)

        # Define each lap of track
        lap_design = []
        for i in range(self.track.legs_per_lap):
            lap_design.append(0)
        for i in range(self.track.jumps_per_lap):
            lap_design.append(1)
        shuffle(lap_design)

        positions.sort(key=lambda x: x.race_score, reverse=True)
        race_summary =[[""],[""]]
        for x,y in enumerate(positions):
            race_summary[0].append(x)
            race_summary[1].append("#{} ({})".format(y.number, y.race_score))

        # Begin Race
        for i, lap in enumerate(range(self.track.laps)):
            race_summary.append(['Lap {}'.format(i+1)])
            for part in lap_design:

                if part == 0: # Leg
                    part_summary = ["Leg"]
                    for pair in positions:
                        pair.race_score -= randint(200,400) # Loss of speed from leg
                        pair.race_score += pair.horse.s2 + pair.rider.s2 # Counter to above

                        part_summary.append("#{} ({})".format(pair.number, pair.race_score))

                elif part == 1: # Jump
                    part_summary = ["Jump"]
                    for pair in positions:
                        pair.race_score -= randint(200,400) # Loss of speed from jump
                        pair.race_score += pair.horse.s3 + pair.rider.s3 # Counter to above
                        part_summary.append("#{} ({})".format(pair.number, pair.race_score))

                positions.sort(key=lambda x: x.race_score, reverse=True)
                race_summary += [part_summary]

        print(tabulate(race_summary))
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
