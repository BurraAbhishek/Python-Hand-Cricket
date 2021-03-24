import random

# Player is bowling
def playOut(fd,bt):
    print("This is hand cricket batting. Bowler:", fd, ". Batter on strike:", bt)
    print("Any other input means free sixer for opponent.")
    # Get a number from 0 to 6, from the player.
    user_bowl_attempt=input("Bowl any number from 0 to 6: ")
    try:
        p_run=int(user_bowl_attempt)
    except:
        p_run=6
    # Get the batter's attempted score
    o_run=random.randint(0, 6)
    # Punish the bowler for overflow case
    if p_run<0 or p_run>6:
        rr='6'
    else:
        # Wicket, if the numbers match
        if p_run==o_run:
            rr='W'
        else:
            rr=str(orun)
    return rr
