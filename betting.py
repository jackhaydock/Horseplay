from race import Race

def start_betting():
    race = Race()
    print(race.print_details())
    racer_num = int(input("Please choose your horse/rider by entering their number: "))
    player_bet = input("How much would you like to bet?: ")
    print("You have bet %d on %s riden by %s" % (player_bet, race.racers[racer_num -1][1].name, race.racers[racer_num -1][0].name))
    winner = race.start_race()
    if winner == racer_num:
        print("Congratulations You Win!")
        print("You earned: %d" % (race.odds[racer_num -1] * player_bet))
    else:
        print("You Lost!")

start_betting()
