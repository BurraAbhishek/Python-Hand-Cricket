import random

# Player is batting


def playIn(bowler, batter, is_declare_permitted):
    print("This is hand cricket batting. \
Bowler:", bowler, ". Batter on strike:", batter)
    print("Any other input means NO RUN")
    if is_declare_permitted:
        print("Type 'Declare' to declare this innings closed.")
    # Get the player scoring attempt as an input
    user_bat_attempted = input("Bat any number from 0 to 6: ")
    # p_run: Player's score
    try:
        p_run = int(user_bat_attempted)
    except:
        p_run = 0
    # Get the bowler's score to determine the scoring
    # o_run: Opponent's choice
    o_run = random.randint(0, 6)
    # Overflow case
    if p_run < 0 or p_run > 6:
        returned_runs = '0'
    else:
        # Wicket, if the numbers match
        if p_run==o_run:
            returned_runs = 'W'
        else:
            returned_runs = str(p_run)
    # Declare the innings closed, if opted
    if is_declare_permitted:
        if user_bat_attempted == "Declare":
            returned_runs = -1
    return returned_runs
