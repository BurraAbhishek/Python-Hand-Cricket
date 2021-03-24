import random

# Player is batting
def playIn(fd,bt):
    print("This is hand cricket batting. Bowler:", fd, ". Batter on strike:", bt)
    print("Any other input means NO RUN")
    # Get the player scoring attempt as an input
    user_bat_attempted=input("Bat any number from 0 to 6: ")
    try:
        p_run=int(user_bat_attempted)
    except:
        p_run=0
    # Get the bowler's score to determine the scoring
    o_run=random.randint(0, 6)
    # Overflow case
    if p_run<0 or p_run>6:
        rr='0'
    else:
        # Wicket, if the numbers match
        if p_run==o_run:
            rr='W'
        else:
            rr=str(p_run)
    return rr

