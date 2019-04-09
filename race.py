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

    def generate_num_racers(self):
        return randint(2,8)

    def generate_racers(self, num_racers):
        racers = []
        i = 0
        while i < num_racers:
            racers.append((Rider(), Horse()))
            i += 1
        return racers
        
    def print_details(self):
        str = self.track.print_details()
        str += ("Racing Pairs: %d\n" % self.num_racers)
        for i, pair in enumerate(self.racers):
            str += ("\n---#%d---" % (int(i) + 1))
            for racer in pair:
                str += "\n"
                str += (racer.print_details())
        return str

if __name__ == "__main__":
    r = Race()
    print(r.print_details())
