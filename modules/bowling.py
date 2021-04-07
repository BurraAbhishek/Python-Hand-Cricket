import random

# Player is bowling
def playOut(bowler,batter):
    print("This is hand cricket batting. Bowler:", bowler, ". Batter on strike:", batter)
    print("Any other input means free sixer for opponent.")
    # Get a number from 0 to 6, from the player.
    user_bowl_attempt=input("Bowl any number from 0 to 6: ")
    # p_run: Player's attempted score
    try:
        p_run=int(user_bowl_attempt)
    except:
        p_run=6
    # Get the batter's attempted score
    # o_run: Opponent's score
    o_run=random.randint(0, 6)
    # Punish the bowler for overflow case
    if p_run<0 or p_run>6:
        returned_runs='6'
    else:
        # Wicket, if the numbers match
        if p_run==o_run:
            returned_runs='W'
        else:
            returned_runs=str(o_run)
    return returned_runs
