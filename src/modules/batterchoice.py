import random

# Select the batters


def batterChoice(batter_list, non_striker, innings, user_choice_batfield):
    # The team bats first
    if innings == 1:
        if user_choice_batfield == 'field':
            chosen_batter = random.choice(batter_list)
        elif user_choice_batfield == 'bat':
            # We have to choose the batter from the list of remaining batters
            print("Remaining batters:", cleanBatterList(batter_list))
            selected_batter = input("Choose your batter: ")
            # Check if the chosen batter is in the list.
            batter_chosen_valid = 0
            for i in range(0, len(batter_list)):
                # Verify that the batter is not already chosen
                if selected_batter == batter_list[i]:
                    if selected_batter != non_striker:
                        if selected_batter != '':
                            batter_chosen_valid += 1
                            chosen_batter_by_team = selected_batter
            if batter_chosen_valid == 1:
                # The chosen batter is in the list
                chosen_batter = chosen_batter_by_team
            else:
                # The chosen batter is not in the list
                chosen_batter = filterBatter(batter_list_dirty=batter_list)

    # The team chases the opponent score
    else:
        if user_choice_batfield == 'bat':
            chosen_batter = random.choice(batter_list)
        elif user_choice_batfield == 'field':
            # The player is chasing the target
            print("Remaining batters:", cleanBatterList(batter_list))
            selected_batter = input("Choose your batter: ")
            # Check if the chosen batter is in the list.
            batter_chosen_valid = 0
            for i in range(0, len(batter_list)):
                # Verify that the batter is not already chosen
                if selected_batter == batter_list[i]:
                    if selected_batter != non_striker:
                        if selected_batter != '':
                            batter_chosen_valid += 1
                            chosen_batter_by_team = selected_batter
            if batter_chosen_valid == 1:
                # The chosen batter is in the list
                chosen_batter = chosen_batter_by_team
            else:
                # The chosen batter is not in the list
                chosen_batter = filterBatter(batter_list_dirty=batter_list)
    # Remove the chosen batter from the list of remaining batters
    batter_list.pop(batter_list.index(chosen_batter))
    return chosen_batter


def cleanBatterList(batter_list):
    batter_list_clean = []
    for i in batter_list:
        if(len(i) > 0):
            batter_list_clean.append(i)
    return batter_list_clean


def filterBatter(batter_list_dirty):
    batter_list_clean = cleanBatterList(batter_list_dirty)
    if(len(batter_list_clean) > 0):
        returned_batter = random.choice(batter_list_clean)
    else:
        returned_batter = ''
    return returned_batter
