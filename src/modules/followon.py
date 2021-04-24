import random

# This module is used only in test cricket, NOT in limited overs cricket


def checkFollowOn(team1_name, team2_name, is_team1_human):
    is_human = True
    if not is_team1_human:
        # The computer batted first.
        is_human = False
    if is_human:
        print('You are permitted to enforce follow-on')
        followon_confirm = input("Do you want to enforce follow-on? \
Type 'Y' for yes and 'N' for no. (Y/N)")
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
