from race import Race

def start_betting():
    race = Race()
    print(race.print_details())

    racer_num = int(input("Please choose your racing pair by entering their number: "))
    player_bet = input("How much would you like to bet?: ")
    print("You have bet %d on #%d (%s riden by %s)" % (player_bet, racer_num, race.racers[racer_num -1].horse.name, race.racers[racer_num -1].rider.name))

    winners = race.start_race()
    positions = [r.number for r in winners]

    print(positions)

    if racer_num == positions[0]:
        print("Congratulations You Win!")
        print("You earned %d times your bet: %d" % (race.racers[racer_num -1].odds, race.racers[racer_num -1].odds * player_bet))
    elif racer_num == positions[1]:
        print("You came second!")
        print("You earned your money back: %d" % (player_bet))
    elif racer_num == positions[2]:
        print("You Came Third!")
        print("You earned half your money back: %d" % (player_bet / 2))
    else:
        print("You Lost!")

start_betting()
