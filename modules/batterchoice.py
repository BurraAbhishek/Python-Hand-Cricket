import random

# Select the batters
def batterChoice(bta,stk,innings,user_choice_batfield):
    # The team bats first
    if innings==1:
        if user_choice_batfield == 'field':
            chosen_batter=random.choice(bta)
        elif user_choice_batfield == 'bat':
            # We have to choose the batter from the list of remaining batters
            print("Remaining batters:",bta)
            bth=input("Choose your batter: ")
            # Check if the chosen batter is in the list.
            batter_chosen_valid=0
            for i in range(0,len(bta)):
                # Verify that the batter is not already chosen
                if bth==bta[i] and bth!=stk and bth!='':
                    batter_chosen_valid+=1
                    chosen_batter_by_team=bth
            if batter_chosen_valid==1:
                # The chosen batter is in the list
                chosen_batter=chosen_batter_by_team
            else:
                # The chosen batter is not in the list
                chosen_batter=random.choice(bta)

    # The team chases the opponent score  
    else:
        if user_choice_batfield == 'bat':
            chosen_batter=random.choice(bta)
        elif user_choice_batfield == 'field':
            # The player is chasing the target
            print("Remaining batters:",bta)            
            bth=input("Choose your batter: ")
            # Check if the chosen batter is in the list.
            batter_chosen_valid=0
            for i in range(0,len(bta)):
                # Verify that the batter is not already chosen
                if bth==bta[i] and bth!=stk and bth!='':
                    batter_chosen_valid+=1
                    chosen_batter_by_team=bth
            if batter_chosen_valid==1:
                # The chosen batter is in the list
                chosen_batter=chosen_batter_by_team
            else:
                # The chosen batter is not in the list
                chosen_batter=random.choice(bta)
    bta.pop(bta.index(chosen_batter))             
    return chosen_batter
