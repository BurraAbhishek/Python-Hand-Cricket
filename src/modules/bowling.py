import random

# Player is bowling


def bowl(bowler, is_bowler_human):
    # Get a number from 0 to 6, from the player.
    if(is_bowler_human):
        print("Bowling: Type your choice in {0, 1, 2, 3, 4, 5, 6}")
        print("Any other input means free sixer for opponent.")
        user_bowl_attempt = input("Bowl any number from 0 to 6: ")
    else:
        user_bowl_attempt = random.randint(0, 6)
    # p_run: Player's attempted score
    try:
        p_run = int(user_bowl_attempt)
    except:
        p_run = 7
    # Punish the bowler for overflow case
    if p_run < 0 or p_run > 6:
        returned_ball = '7'
    else:
        returned_ball = str(p_run)
    return returned_ball
