from race import Race

def start_betting(purse):
    race = Race()
    print("")
    print(race.print_details())

    # Get Player's Pair
    racer_num = None
    while racer_num == None:
        try:
            x = int(input("Please choose your racing pair by entering their number: "))
            if x >= 1 and x <= len(race.racers):
                racer_num = x
                break
        except NameError:
            pass
        print("Please enter a valid number")

    # Get Player's Bet
    player_bet = None
    while player_bet == None:
        try:
            x = int(input("How much would you like to bet? (You have {}): ".format(purse)))
            if x >= 0 and x <= purse:
                player_bet = x
                purse -= player_bet
                break
        except NameError:
            pass
        print("Please enter a valid number")

    # Begin Race
    print("You have bet %d on #%d (%s riden by %s)" % (player_bet, racer_num, race.racers[racer_num -1].horse.name, race.racers[racer_num -1].rider.name))
    pot = int(race.racers[racer_num -1].odds * player_bet)
    print("Your potential winnings are: {}".format(pot))

    # Begin Race
    raw_input("Press enter to start race")
    winners = race.start_race()
    positions = [r.number for r in winners]

    print(positions)

    # Calculate Player's Winnings
    if racer_num == positions[0]:
        winnings = pot
        print("Congratulations You Win!")
        print("You earned: {}".format(winnings))
    elif racer_num == positions[1]:
        winnings = pot / 2
        print("You came second!")
        print("You earned half your potential winnings: {}".format(winnings))
    elif racer_num == positions[2]:
        winnings = player_bet
        print("You Came Third!")
        print("You earned your money back: {}".format(winnings))
    else:
        winnings = 0
        print("You Lost!")

    purse += winnings
    print("Current Purse: {}".format(purse))
    return purse

# Loop until player runs out of money
purse = 1000
while purse > 0:
    raw_input("Press enter to find next race")
    x = start_betting(purse)
    purse = x
else:
    print("You have lost all your money!")
