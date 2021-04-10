# Generate the scorecard
# batters_list: Score Array of the team batting first
# bowlers_list: Score Array of the team fielding first
# team1_players: Name of all players of the team batting first
# team2_players: Name of all players of the team fielding first
# innings: 1st innings or 2nd innings

def scoreCard(batters_list, bowlers_list, team1_players, team2_players, innings):
    # List of all the players in team 1
    A1 = team1_players[1]
    A2 = team1_players[2]
    A3 = team1_players[3]
    A4 = team1_players[4]
    A5 = team1_players[5]
    A6 = team1_players[6]
    A7 = team1_players[7]
    A8 = team1_players[8]
    A9 = team1_players[9]
    A10 = team1_players[10]
    A11 = team1_players[11]
    # List of all the players in team 2
    B1 = team2_players[1]
    B2 = team2_players[2]
    B3 = team2_players[3]
    B4 = team2_players[4]
    B5 = team2_players[5]
    B6 = team2_players[6]
    B7 = team2_players[7]
    B8 = team2_players[8]
    B9 = team2_players[9]
    B10 = team2_players[10]
    B11 = team2_players[11]
    # Batting Statistics
    print("Batting")
    if innings == 1:
        print(A1, "scored", batters_list[A1][0], "runs off", batters_list[A1][1], "balls, hitting", batters_list[A1][2], "fours and", batters_list[A1][3], "sixes.")
        print(A2, "scored", batters_list[A2][0], "runs off", batters_list[A2][1], "balls, hitting", batters_list[A2][2], "fours and", batters_list[A2][3], "sixes.")
        print(A3, "scored", batters_list[A3][0], "runs off", batters_list[A3][1], "balls, hitting", batters_list[A3][2], "fours and", batters_list[A3][3], "sixes.")
        print(A4, "scored", batters_list[A4][0], "runs off", batters_list[A4][1], "balls, hitting", batters_list[A4][2], "fours and", batters_list[A4][3], "sixes.")
        print(A5, "scored", batters_list[A5][0], "runs off", batters_list[A5][1], "balls, hitting", batters_list[A5][2], "fours and", batters_list[A5][3], "sixes.")
        print(A6, "scored", batters_list[A6][0], "runs off", batters_list[A6][1], "balls, hitting", batters_list[A6][2], "fours and", batters_list[A6][3], "sixes.")
        print(A7, "scored", batters_list[A7][0], "runs off", batters_list[A7][1], "balls, hitting", batters_list[A7][2], "fours and", batters_list[A7][3], "sixes.")
        print(A8, "scored", batters_list[A8][0], "runs off", batters_list[A8][1], "balls, hitting", batters_list[A8][2], "fours and", batters_list[A8][3], "sixes.")
        print(A9, "scored", batters_list[A9][0], "runs off", batters_list[A9][1], "balls, hitting", batters_list[A9][2], "fours and", batters_list[A9][3], "sixes.")
        print(A10, "scored", batters_list[A10][0], "runs off", batters_list[A10][1], "balls, hitting", batters_list[A10][2], "fours and", batters_list[A10][3], "sixes.")
        print(A11, "scored", batters_list[A11][0], "runs off", batters_list[A11][1], "balls, hitting", batters_list[A11][2], "fours and", batters_list[A11][3], "sixes.")
    else:
        print(B1, "scored", batters_list[B1][0], "runs off", batters_list[B1][1], "balls, hitting", batters_list[B1][2], "fours and", batters_list[B1][3], "sixes.")
        print(B2, "scored", batters_list[B2][0], "runs off", batters_list[B2][1], "balls, hitting", batters_list[B2][2], "fours and", batters_list[B2][3], "sixes.")
        print(B3, "scored", batters_list[B3][0], "runs off", batters_list[B3][1], "balls, hitting", batters_list[B3][2], "fours and", batters_list[B3][3], "sixes.")
        print(B4, "scored", batters_list[B4][0], "runs off", batters_list[B4][1], "balls, hitting", batters_list[B4][2], "fours and", batters_list[B4][3], "sixes.")
        print(B5, "scored", batters_list[B5][0], "runs off", batters_list[B5][1], "balls, hitting", batters_list[B5][2], "fours and", batters_list[B5][3], "sixes.")
        print(B6, "scored", batters_list[B6][0], "runs off", batters_list[B6][1], "balls, hitting", batters_list[B6][2], "fours and", batters_list[B6][3], "sixes.")
        print(B7, "scored", batters_list[B7][0], "runs off", batters_list[B7][1], "balls, hitting", batters_list[B7][2], "fours and", batters_list[B7][3], "sixes.")
        print(B8, "scored", batters_list[B8][0], "runs off", batters_list[B8][1], "balls, hitting", batters_list[B8][2], "fours and", batters_list[B8][3], "sixes.")
        print(B9, "scored", batters_list[B9][0], "runs off", batters_list[B9][1], "balls, hitting", batters_list[B9][2], "fours and", batters_list[B9][3], "sixes.")
        print(B10, "scored", batters_list[B10][0], "runs off", batters_list[B10][1], "balls, hitting", batters_list[B10][2], "fours and", batters_list[B10][3], "sixes.")
        print(B11, "scored", batters_list[B11][0], "runs off", batters_list[B11][1], "balls, hitting", batters_list[B11][2], "fours and", batters_list[B11][3], "sixes.")
    # Bowling Statistics
    print("\nBowling")
    if innings == 2:
        print(A1, ":", bowlers_list[A1][0], "-", bowlers_list[A1][1], "-", bowlers_list[A1][2], "-", bowlers_list[A1][3])
        print(A2, ":", bowlers_list[A2][0], "-", bowlers_list[A2][1], "-", bowlers_list[A2][2], "-", bowlers_list[A2][3])
        print(A3, ":", bowlers_list[A3][0], "-", bowlers_list[A3][1], "-", bowlers_list[A3][2], "-", bowlers_list[A3][3])
        print(A4, ":", bowlers_list[A4][0], "-", bowlers_list[A4][1], "-", bowlers_list[A4][2], "-", bowlers_list[A4][3])
        print(A5, ":", bowlers_list[A5][0], "-", bowlers_list[A5][1], "-", bowlers_list[A5][2], "-", bowlers_list[A5][3])
        print(A6, ":", bowlers_list[A6][0], "-", bowlers_list[A6][1], "-", bowlers_list[A6][2], "-", bowlers_list[A6][3])
        print(A7, ":", bowlers_list[A7][0], "-", bowlers_list[A7][1], "-", bowlers_list[A7][2], "-", bowlers_list[A7][3])
        print(A8, ":", bowlers_list[A8][0], "-", bowlers_list[A8][1], "-", bowlers_list[A8][2], "-", bowlers_list[A8][3])
        print(A9, ":", bowlers_list[A9][0], "-", bowlers_list[A9][1], "-", bowlers_list[A9][2], "-", bowlers_list[A9][3])
        print(A10, ":", bowlers_list[A10][0], "-", bowlers_list[A10][1], "-", bowlers_list[A10][2], "-", bowlers_list[A10][3])
        print(A11, ":", bowlers_list[A11][0], "-", bowlers_list[A11][1], "-", bowlers_list[A11][2], "-", bowlers_list[A11][3])
    else:
        print(B1, ":", bowlers_list[B1][0], "-", bowlers_list[B1][1], "-", bowlers_list[B1][2], "-", bowlers_list[B1][3])
        print(B2, ":", bowlers_list[B2][0], "-", bowlers_list[B2][1], "-", bowlers_list[B2][2], "-", bowlers_list[B2][3])
        print(B3, ":", bowlers_list[B3][0], "-", bowlers_list[B3][1], "-", bowlers_list[B3][2], "-", bowlers_list[B3][3])
        print(B4, ":", bowlers_list[B4][0], "-", bowlers_list[B4][1], "-", bowlers_list[B4][2], "-", bowlers_list[B4][3])
        print(B5, ":", bowlers_list[B5][0], "-", bowlers_list[B5][1], "-", bowlers_list[B5][2], "-", bowlers_list[B5][3])
        print(B6, ":", bowlers_list[B6][0], "-", bowlers_list[B6][1], "-", bowlers_list[B6][2], "-", bowlers_list[B6][3])
        print(B7, ":", bowlers_list[B7][0], "-", bowlers_list[B7][1], "-", bowlers_list[B7][2], "-", bowlers_list[B7][3])
        print(B8, ":", bowlers_list[B8][0], "-", bowlers_list[B8][1], "-", bowlers_list[B8][2], "-", bowlers_list[B8][3])
        print(B9, ":", bowlers_list[B9][0], "-", bowlers_list[B9][1], "-", bowlers_list[B9][2], "-", bowlers_list[B9][3])
        print(B10, ":", bowlers_list[B10][0], "-", bowlers_list[B10][1], "-", bowlers_list[B10][2], "-", bowlers_list[B10][3])
        print(B11, ":", bowlers_list[B11][0], "-", bowlers_list[B11][1], "-", bowlers_list[B11][2], "-", bowlers_list[B11][3])
    print('')
