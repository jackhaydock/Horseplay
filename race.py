from random import randint
import textwrap

from horse import Horse
from rider import Rider
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
            racers.append((Rider(), Horse()))
            i += 1
        return racers

    def calculate_odds(self):
        scores = []
        for rider,horse in self.racers:
            score = 0

            score += rider.s1 * 5 # Control of Rider
            score += rider.s2 * 5
            score += rider.s3 * 5

            score += rider.career[0] * 5 # Rider's 1st place wins
            score += rider.career[1] * 4 # Rider's 2nd place wins
            score += rider.career[2] * 3 # Rider's 3rd place wins
            score -= rider.career[3] * 2 # Rider's Loses


            score += horse.s1 * 5 # Speed of Horse
            score += horse.s2 * (self.track.legs_per_lap * self.track.laps) # Stamina of Horse
            score += horse.s3 * (self.track.jumps_per_lap * self.track.laps) # Jumping ability of Horse

            score += horse.career[0] * 5 # Horse's 1st place wins
            score += horse.career[1] * 4 # Horse's 2nd place wins
            score += horse.career[2] * 3 # Horse's 3rd place wins
            score -= horse.career[3] * 2 # Horse's Loses

            score += randint(-100, 100) # Bookie error
            scores.append(score)

        odds = []
        for score in scores:
            odds.append((sum(scores)/score))
        self.odds = odds

    def print_details(self):
        str = self.track.print_details()
        str += ("Racing Pairs: %d\n" % self.num_racers)
        for i, pair in enumerate(self.racers):
            str += ("\n---#%d---(%d/1)" % (int(i) + 1, self.odds[i]))
            for racer in pair:
                str += "\n"
                str += (racer.print_details())
        return str

if __name__ == "__main__":
    r = Race()
    print(r.print_details())
    r.calculate_odds()
