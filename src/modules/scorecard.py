# Generate the scorecard
# batters_list: Score Array of the team batting first
# bowlers_list: Score Array of the team fielding first
# team1_players: Name of all players of the team batting first
# team2_players: Name of all players of the team fielding first
# innings: 1st innings or 2nd innings


def printBatterStats(player, batters_list):
    if(batters_list[player][1] < 1):
        statstring = str(player) + " did not bat."
    else:
        statstring = (str(player)
                      + " scored "
                      + str(batters_list[player][0]))
        if(batters_list[player][0] == 1):
            statstring += " run off "
        else:
            statstring += " runs off "
        statstring += str(batters_list[player][1])
        if(batters_list[player][1] == 1):
            statstring += " ball, hitting "
        else:
            statstring += " balls, hitting "
        statstring += str(batters_list[player][2])
        if(batters_list[player][2] == 1):
            statstring += " four and "
        else:
            statstring += " fours and "
        statstring += str(batters_list[player][3])
        if(batters_list[player][3] == 1):
            statstring += " six."
        else:
            statstring += " sixes."
    print(statstring)


def printBowlerStats(player, bowlers_list):
    if(bowlers_list[player][0] > 0):
        statstring = (str(player)
                      + ": "
                      + str(bowlers_list[player][0])
                      + " - "
                      + str(bowlers_list[player][1])
                      + " - "
                      + str(bowlers_list[player][2])
                      + " - "
                      + str(bowlers_list[player][3]))
        print(statstring)


def scoreCard(batters_list,
              bowlers_list,
              team1_players,
              team2_players,
              innings):
    # Batting Statistics
    print("Batting")
    if innings == 1:
        for i in range(1, 12):
            printBatterStats(team1_players[i], batters_list)
    else:
        for i in range(1, 12):
            printBatterStats(team2_players[i], batters_list)
    # Bowling Statistics
    print("\nBowling")
    if innings == 2:
        for i in range(1, 12):
            printBowlerStats(team1_players[i], bowlers_list)
    else:
        for i in range(1, 12):
            printBowlerStats(team2_players[i], bowlers_list)
    print('')
