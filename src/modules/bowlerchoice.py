import random

# Select the bowlers


def fieldChoice(bowlers_array: list, is_bowler_human: bool) -> str:
    if not is_bowler_human:
        bowler_selected = random.choice(bowlers_array)
    else:
        # Select the bowler from the list of available bowlers
        print("Bowlers:", bowlers_array)
        bowlchoice = input("Choose your bowler: ")
        bowler_team_valid = 0
        for i in bowlers_array:
            if bowlchoice == i:
                bowler_team_valid += 1
                bowler_shortlisted = bowlchoice
        if bowler_team_valid != 0:
            bowler_selected = bowler_shortlisted
        else:
            bowler_selected = random.choice(bowlers_array)
    return bowler_selected
