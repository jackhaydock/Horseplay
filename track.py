from random import randint
import textwrap

from track_names import track_names

class Track():
    def __init__(
        self,
        name=None,
        legs_per_lap=None,
        jumps_per_lap=None,
        laps=None,
    ):
        self.name = name if name else self.generate_name(track_names)
        self.laps = laps if laps else self.generate_laps()
        self.legs_per_lap = legs_per_lap if legs_per_lap else self.generate_legs_per_lap()
        self.jumps_per_lap = jumps_per_lap if jumps_per_lap else self.generate_jumps_per_lap()

    def generate_name(self, names):
        desc = names['desc'][randint(0, len(names['desc']) - 1)]
        type = names['type'][randint(0, len(names['type']) - 1)]
        return "The %s %s" % (desc, type)

    def generate_laps(self):
        return randint(1, 4)

    def generate_legs_per_lap(self):
        return randint(2, 12)

    def generate_jumps_per_lap(self):
        return randint(0, self.legs_per_lap)

    def print_details(self):
        table = [
            [
            "",
            "Laps",
            "Legs/Lap",
            "Jumps/Lap",
            "Total Legs",
            "Total Jumps"
            ],
            [
            self.name,
            self.laps,
            self.legs_per_lap,
            self.jumps_per_lap,
            self.legs_per_lap * self.laps,
            self.jumps_per_lap * self.laps,
            ]
        ]
        return table

if __name__ == "__main__":
    t = Track()
    print(t.print_details())
