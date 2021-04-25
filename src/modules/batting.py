import random

# Player is batting


def bat(batter, is_declare_permitted, is_batter_human):
    # Get the player scoring attempt as an input
    if(is_batter_human):
        print("Batting: Type your scoring choice in {0, 1, 2, 3, 4, 5, 6}")
        print("Any other input means NO RUN")
        if is_declare_permitted:
            print("Type 'Declare' to declare this innings closed.")
        user_bat_attempted = input("Bat any number from 0 to 6: ")
    else:
        user_bat_attempted = random.randint(0, 6)
    # p_run: Player's score
    try:
        p_run = int(user_bat_attempted)
    except:
        p_run = 0
    # Overflow case
    if p_run < 0 or p_run > 6:
        returned_runs = '-2'
    else:
        returned_runs = str(p_run)
    # Declare the innings closed, if opted
    if is_declare_permitted:
        if user_bat_attempted == "Declare":
            returned_runs = -1
    return returned_runs
