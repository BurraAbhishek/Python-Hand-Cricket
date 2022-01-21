import json

from modules.savegamedata import saveGame

from innings.scoring import scoringInnings
from innings.chasing import chasingInnings


def superOver(old_toss, team1_teamfile, team2_teamfile):
    # Score for each ball faced in the first innings
    innings1_data = {
        "battingteam": "Waiting for toss",
        "bowlingteam": "Waiting for toss",
        "innings": 1,
        "score": 0,
        "wickets_lost": 0,
        "data": [],
        "batter_stats": [],
        "bowler_stats": []
        }
    # Score for each ball faced in the second innings
    innings2_data = {
        "battingteam": "Waiting for toss",
        "bowlingteam": "Waiting for toss",
        "innings": 2,
        "score": 0,
        "wickets_lost": 0,
        "data": [],
        "batter_stats": [],
        "bowler_stats": []
        }
    # First innings score
    score1 = 0
    # Second innings score
    score2 = 0
    # Innings: 1st innings or 2nd innings
    innings = 1
    # Batting first and fielding first are reversed for every super over.
    if old_toss == 'bat':
        new_toss = "field"
    else:
        new_toss = "bat"

    # Super Over
    overs_choice = 1
    print("Super over")
    wickets_choice = 2
    print("Total:", wickets_choice, "wickets game")

    # Team files
    with open(team1_teamfile, 'r') as match_file1:
        team_data1 = json.load(match_file1)
    match_file1.close()
    with open(team2_teamfile, 'r') as match_file2:
        team_data2 = json.load(match_file2)
    match_file2.close()

    # Prepare the team structure if team1 bats first
    if new_toss == "bat":
        team1_list = [team_data1["team_name"]]
        for i in range(0, 11):
            team1_list.append(team_data1["team_members"][i])
        team1_list.append(team_data1["games_played"])
        team1_list.append(team_data1["games_won"])
        team1_list.append(team_data1["isHuman"])

        team2_list = [team_data2["team_name"]]
        for i in range(0, 11):
            team2_list.append(team_data2["team_members"][i])
        team2_list.append(team_data2["games_played"])
        team2_list.append(team_data2["games_won"])
        team2_list.append(team_data2["isHuman"])

    # Prepare the team structure if team1 fields first
    else:
        team1_list = [team_data2["team_name"]]
        for i in range(0, 11):
            team1_list.append(team_data2["team_members"][i])
        team1_list.append(team_data2["games_played"])
        team1_list.append(team_data2["games_won"])
        team1_list.append(team_data2["isHuman"])

        team2_list = [team_data1["team_name"]]
        for i in range(0, 11):
            team2_list.append(team_data1["team_members"][i])
        team2_list.append(team_data1["games_played"])
        team2_list.append(team_data1["games_won"])
        team2_list.append(team_data1["isHuman"])

    # The two teams look like this:

    # ['T1','A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11']
    # ['T2','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11']

    T1 = team1_list[0]
    T2 = team2_list[0]

    A1 = team1_list[1]
    A2 = team1_list[2]
    A3 = team1_list[3]
    A4 = team1_list[4]
    A5 = team1_list[5]
    A6 = team1_list[6]
    A7 = team1_list[7]
    A8 = team1_list[8]
    A9 = team1_list[9]
    A10 = team1_list[10]
    A11 = team1_list[11]

    B1 = team2_list[1]
    B2 = team2_list[2]
    B3 = team2_list[3]
    B4 = team2_list[4]
    B5 = team2_list[5]
    B6 = team2_list[6]
    B7 = team2_list[7]
    B8 = team2_list[8]
    B9 = team2_list[9]
    B10 = team2_list[10]
    B11 = team2_list[11]

    # Play the first innings.
    score1 = scoringInnings(team_1_array=team1_list,
                            team_2_array=team2_list,
                            innings=innings,
                            bat_bowl_choice=new_toss,
                            batting_score=score1,
                            innings_data=innings1_data,
                            start_message="First Innings",
                            max_overs=overs_choice,
                            max_wickets=wickets_choice,
                            is_test=False)
    innings += 1

    # Compute the results.
    # team_wins checks if the team wins against the computer.
    score2 = chasingInnings(team_1_array=team1_list,
                            team_2_array=team2_list,
                            innings=innings,
                            bat_bowl_choice=new_toss,
                            opponent_netscore=score1,
                            batting_score=score2,
                            innings_data=innings2_data,
                            start_message="Second Innings",
                            max_overs=overs_choice,
                            max_wickets=wickets_choice,
                            is_test=False)
    # Score at the end of second innings
    score2_runs = score2[0]
    # Number of wickets fallen at the end of second innings
    score2_wickets = score2[1]
    # Open the team files.
    if team1_list[14]:
        player_teamfile1 = "teams/team" + str(T1) + ".json"
    else:
        player_teamfile1 = "ai_opponent/team" + str(T1) + ".json"
    if team2_list[14]:
        player_teamfile2 = "teams/team" + str(T2) + ".json"
    else:
        player_teamfile2 = "ai_opponent/team" + str(T2) + ".json"
    with open(player_teamfile1, 'r') as match_file1:
        team_data_object1 = json.load(match_file1)
    with open(player_teamfile2, 'r') as match_file2:
        team_data_object2 = json.load(match_file2)
    # Team batting first successfully defends its score
    if score1 > score2_runs:
        if new_toss == "bat":
            if not team_data_object2["isHuman"]:
                print("Congratulations, you won!")
        else:
            if not team_data_object2["isHuman"]:
                print("Sorry, you lost this game. Better luck next time.")
        team_wins = 1
        print(T1, "wins by super over.")
    # Team batting second successfully chases its target
    elif score1 < score2_runs:
        if new_toss == "bat":
            if not team_data_object2["isHuman"]:
                print("Sorry, you lost this game. Better luck next time.")
        else:
            if not team_data_object2["isHuman"]:
                print("Congratulations, you won!")
        team_wins = -1
        print(T2, "wins by super over.")
    # Scores are level - Match tied.
    # We need to play another super over to decide the winner
    else:
        print("Tied")
        team_wins = 0 - (superOver(new_toss, team1_teamfile, team2_teamfile))

    # Save the statistics.
    game_data = {
        "isTest": False,
        "overs": overs_choice,
        "wickets": wickets_choice,
        "innings_data": {
            "innings1_data": innings1_data,
            "innings2_data": innings2_data
            }
        }
    saveGame(game_data)

    return team_wins
