import random

# Select the bowlers
def fieldChoice(bowlers_array,innings,user_choice_batfield):
    if innings==1:
        if user_choice_batfield == 'bat':
            bowler_selected=random.choice(bowlers_array)
        elif user_choice_batfield == 'field':
            # Select the bowler from the list of available bowlers
            print("Bowlers:",bowlers_array)
            bowlchoice=input("Choose your bowler: ")
            bowler_team_valid=0
            for i in range(0,11):
                if bowlchoice==bowlers_array[i]:
                    bowler_team_valid+=1
                    bowler_shortlisted=bowlchoice
            if bowler_team_valid!=0:
                bowler_selected=bowler_shortlisted
            else:
                bowler_selected=random.choice(bowlers_array)
    else:
        if user_choice_batfield == 'field':
            bowler_selected=random.choice(bowlers_array)
        elif user_choice_batfield == 'bat':
            # Select the bowler from the list of available bowlers
            print("Bowlers:",bowlers_array)
            bowlchoice=input("Choose your bowler: ")
            bowler_team_valid=0
            for i in range(0,11):
                if bowlchoice==bowlers_array[i]:
                    bowler_team_valid+=1
                    bowler_shortlisted=bowlchoice
            if bowler_team_valid!=0:
                bowler_selected=bowler_shortlisted
            else:
                bowler_selected=random.choice(bowlers_array)
    return bowler_selected
