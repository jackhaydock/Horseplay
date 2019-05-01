from random import randint
from tabulate import tabulate

from rider import Rider
from horse import Horse

class Racing_Pair(object):
    def __init__(
        self,
        number,
        rider=None,
        horse=None
    ):
        self.number = number
        self.rider = rider if rider else Rider()
        self.horse = horse if horse else Horse()
        # self.calculate_score()

    def calculate_score(self, track):
        score = 0

        score += self.rider.s1 * 5 # Control of Rider
        score += self.rider.s2 * 5
        score += self.rider.s3 * 5

        score += self.rider.career[0] * 10 # Rider's 1st place wins
        score += self.rider.career[1] * 5 # Rider's 2nd place wins
        score += self.rider.career[2] * 1 # Rider's 3rd place wins
        score -= self.rider.career[3] * 5 # Rider's Loses

        score += self.horse.s1 * 5 # Speed of Horse
        score += self.horse.s2 * (track.legs_per_lap * track.laps) # Stamina of Horse
        score += self.horse.s3 * (track.jumps_per_lap * track.laps) # Jumping ability of Horse

        score += self.horse.career[0] * 10 # Horse's 1st place wins
        score += self.horse.career[1] * 5 # Horse's 2nd place wins
        score += self.horse.career[2] * 1 # Horse's 3rd place wins
        score -= self.horse.career[3] * 5 # Horse's Loses

        score += randint(-200, 200) # Bookie error
        self.score = score

    def print_details(self):
        table = [
            [
            self.number,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "{}/1".format(self.odds),
            ],
            [
            "Rider",
            self.rider.name,
            self.rider.age,
            self.rider.sex_str.title(),
            self.rider.s1,
            self.rider.s2,
            self.rider.s3,
            self.rider.career[0],
            self.rider.career[1],
            self.rider.career[2],
            self.rider.career[3],
            ],
            [
            "Horse",
            self.horse.name,
            self.horse.age,
            self.horse.sex_str.title(),
            self.horse.s1,
            self.horse.s2,
            self.horse.s3,
            self.horse.career[0],
            self.horse.career[1],
            self.horse.career[2],
            self.horse.career[3],
            ],
        ]
        return table
