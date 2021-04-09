import random

# This module is used only in test cricket, NOT in limited overs cricket.
# For human vs human or computer vs computer, p_name = '' (Empty string).

def checkFollowOn(team1_name, team2_name, p_name):
    is_human = True
    if(team2_name == p_name):
        # The computer batted first.
        is_human = False
    if is_human:
        print('You are permitted to enforce follow-on')
        followon_confirm = input("Do you want to enforce follow-on? Type 'Y' for yes and 'N' for no. (Y/N)")
        if followon_confirm == 'Y':
            followon_decision = True
        else:
            followon_decision = False
    else:
        followon_confirm = random.randint(0, 1)
        if followon_confirm == 1:
            followon_decision = True
        else:
            followon_decision = False
    return followon_decision
