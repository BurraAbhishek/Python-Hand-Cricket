# Generate the scorecard
# batters_list: Score Array of the team batting first
# bowlers_list: Score Array of the team fielding first
# team1_players: Name of all players of the team batting first
# team2_players: Name of all players of the team fielding first
# innings: 1st innings or 2nd innings


def printBatterStats(player: str, batters_list: dict) -> None:
    if(batters_list[player]["balls"] < 1):
        statstring = str(player) + " did not bat."
    else:
        statstring = (str(player)
                      + " scored "
                      + str(batters_list[player]["runs"]))
        if(batters_list[player]["runs"] == 1):
            statstring += " run off "
        else:
            statstring += " runs off "
        statstring += str(batters_list[player]["balls"])
        if(batters_list[player]["balls"] == 1):
            statstring += " ball, hitting "
        else:
            statstring += " balls, hitting "
        statstring += str(batters_list[player]["fours"])
        if(batters_list[player]["fours"] == 1):
            statstring += " four and "
        else:
            statstring += " fours and "
        statstring += str(batters_list[player]["sixes"])
        if(batters_list[player]["sixes"] == 1):
            statstring += " six."
        else:
            statstring += " sixes."
    print(statstring)


def printBowlerStats(player: str, bowlers_list: dict) -> None:
    if(bowlers_list[player]["overs"] > 0):
        statstring = (str(player)
                      + ": "
                      + str(bowlers_list[player]["overs"])
                      + " - "
                      + str(bowlers_list[player]["maidens"])
                      + " - "
                      + str(bowlers_list[player]["runs"])
                      + " - "
                      + str(bowlers_list[player]["wickets"]))
        print(statstring)


def scoreCard(batters_list: dict,
              bowlers_list: dict,
              team1_players: list,
              team2_players: list,
              innings: int) -> None:
    # Batting Statistics
    print("Batting")
    if innings == 1:
        for i in range(0, 11):
            printBatterStats(team1_players[i], batters_list)
    else:
        for i in range(0, 11):
            printBatterStats(team2_players[i], batters_list)
    # Bowling Statistics
    print("\nBowling")
    if innings == 2:
        for i in range(0, 11):
            printBowlerStats(team1_players[i], bowlers_list)
    else:
        for i in range(0, 11):
            printBowlerStats(team2_players[i], bowlers_list)
    print('')
