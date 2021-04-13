import random
import ast
import math
import json
import sys

from modules import hashfunc
from modules import toss
from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice
from modules.followon import checkFollowOn
from modules.savegamedata import saveGame

from innings.scoring import scoringInnings
from innings.chasing import chasingInnings

# Score for each ball faced in the first innings of the first team
team1_innings1_data = {
    "battingteam": "Waiting for toss",
    "bowlingteam": "Waiting for toss",
    "innings": 1,
    "score": 0,
    "wickets_lost": 0,
    "data": [],
    "batter_stats": [],
    "bowler_stats": []
    }
# Score for each ball faced in the first innings of the second team
team2_innings1_data = {
    "battingteam": "Waiting for toss",
    "bowlingteam": "Waiting for toss",
    "innings": 1,
    "score": 0,
    "wickets_lost": 0,
    "data": [],
    "batter_stats": [],
    "bowler_stats": []
    }
# Score for each ball faced in the second innings of the first team
team1_innings2_data = {
    "battingteam": "Waiting for toss",
    "bowlingteam": "Waiting for toss",
    "innings": 2,
    "score": 0,
    "wickets_lost": 0,
    "data": [],
    "batter_stats": [],
    "bowler_stats": []
    }
# Score for each ball faced in the second innings of the second team
team2_innings2_data = {
    "battingteam": "Waiting for toss",
    "bowlingteam": "Waiting for toss",
    "innings": 2,
    "score": 0,
    "wickets_lost": 0,
    "data": [],
    "batter_stats": [],
    "bowler_stats": []
    }
# First innings score, first team
team1_score1 = 0
# Second innings score, first team
team1_score2 = 0
# First innings score, second team
team2_score1 = 0
# Second innings score, second team
team2_score2 = 0
# Innings: Assign the role of each team: bat / field.
# Doesn't represent 1st or 2nd innings.
innings = 1
# Is follow-on enforced?
# Decided after both teams complete their first innings.
isfollowon = False

# Enter the password required to play the match
# input_password: User input password
# match_password: Required password
with open("team1.json", 'r') as match_file:
    team_data = json.load(match_file)
match_password = team_data["password"]
match_file.close()
print("Playing team:", team_data["team_name"])
input_password = input("Enter match password: ")

# Exit if the password is wrong.
if not hashfunc.verify_password(input_password, match_password):
    print("Sorry, wrong password! ")
    print("Ensure that you type the match password, not your team password.")
    print("Ensure that you enter the correct password before proceeding.")
    wrong_password_notify = input()
    sys.exit(0)

# Validate the password and proceed to the game
try:
    print("By default, this is a 10-wickets match, unless specified otherwise")
    wickets_choice = int(input("How many wickets for each team? "))
except:
    wickets_choice = 10
if wickets_choice < 1 or wickets_choice > 10:
    wickets_choice = 10
print("Total:", wickets_choice, "wickets game")
try:
    print("By default, a follow-on requires at least 200 runs.")
    print("The minimum limit for this is at least 75 runs.")
    followon_choice = int(input("Minimum runs required for follow-on: "))
except:
    followon_choice = 200
if followon_choice < 75:
    followon_choice = 200
followon_minscore_notify = ("For follow-on to be permitted, "
                            + "the team batting first should score"
                            + "at least "
                            + str(followon_choice)
                            + " runs more than the team fielding first.")
print(followon_minscore_notify)

# Variable toss_chosen holds the decision from the toss:
# bat first or field first
toss_chosen = toss.tossPlay()
if toss_chosen == "bat":
    toss_reversed = "field"
else:
    toss_reversed = "bat"

# Prepare the team structure if player chooses to bat first
if toss_chosen == "bat":
    team1_list = [team_data["team_name"]]
    for i in range(0, 11):
        team1_list.append(team_data["team_members"][i])
    team1_list.append(team_data["games_played"])
    team1_list.append(team_data["games_won"])
    T3 = team1_list[0]
    games_played_old = int(team1_list[12])
    games_won_old = int(team1_list[13])
    team2_list = [
        'Computer',
        'CPU1',
        'CPU2',
        'CPU3',
        'CPU4',
        'CPU5',
        'CPU6',
        'CPU7',
        'CPU8',
        'CPU9',
        'CPU10',
        'CPU11'
        ]
# Prepare the team structure if player chooses to field first
else:
    team1_list = [
        'Computer',
        'CPU1',
        'CPU2',
        'CPU3',
        'CPU4',
        'CPU5',
        'CPU6',
        'CPU7',
        'CPU8',
        'CPU9',
        'CPU10',
        'CPU11'
        ]
    team2_list = [team_data["team_name"]]
    for i in range(0, 11):
        team2_list.append(team_data["team_members"][i])
    team2_list.append(team_data["games_played"])
    team2_list.append(team_data["games_won"])
    T3 = team2_list[0]
    games_played_old = int(team2_list[12])
    games_won_old = int(team2_list[13])

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

# Play the first innings of both sides.
team1_score1 = scoringInnings(team_1_array=team1_list,
                              team_2_array=team2_list,
                              innings=innings,
                              bat_bowl_choice=toss_chosen,
                              batting_score=team1_score1,
                              innings_data=team1_innings1_data,
                              start_message="Team 1 - First Innings",
                              max_overs=math.inf,
                              max_wickets=wickets_choice,
                              is_test=True)
team2_score1 = scoringInnings(team_1_array=team2_list,
                              team_2_array=team1_list,
                              innings=innings,
                              bat_bowl_choice=toss_reversed,
                              batting_score=team2_score1,
                              innings_data=team2_innings1_data,
                              start_message="Team 2 - First Innings",
                              max_overs=math.inf,
                              max_wickets=wickets_choice,
                              is_test=True)

# Check if follow-on is required or not, and then proceed accordingly.
if team1_score1 - team2_score1 >= followon_choice:
    isfollowon = checkFollowOn(team1_name=T1, team2_name=T2, p_name=T3)
    if isfollowon:
        print("Follow-on enforced by", T1)
        team2_score2 = scoringInnings(team_1_array=team2_list,
                                      team_2_array=team1_list,
                                      innings=innings,
                                      bat_bowl_choice=toss_reversed,
                                      batting_score=team2_score2,
                                      innings_data=team2_innings2_data,
                                      start_message="Team 2 - Second Innings",
                                      max_overs=math.inf,
                                      max_wickets=wickets_choice,
                                      is_test=True)
        innings = 2
    else:
        print(T1, "did not enforce follow on. ", T1, "will continue batting.")
        innings = 1
        team1_score2 = scoringInnings(team_1_array=team1_list,
                                      team_2_array=team2_list,
                                      innings=innings,
                                      bat_bowl_choice=toss_chosen,
                                      batting_score=team1_score2,
                                      innings_data=team1_innings2_data,
                                      start_message="Team 1 - Second Innings",
                                      max_overs=math.inf,
                                      max_wickets=wickets_choice,
                                      is_test=True)
        innings = 2
else:
    innings = 1
    team1_score2 = scoringInnings(team_1_array=team1_list,
                                  team_2_array=team2_list,
                                  innings=innings,
                                  bat_bowl_choice=toss_chosen,
                                  batting_score=team1_score2,
                                  innings_data=team1_innings2_data,
                                  start_message="Team 1 - Second Innings",
                                  max_overs=math.inf,
                                  max_wickets=wickets_choice,
                                  is_test=True)
    innings = 2

# Assign the innings accordingly.
# Check for innings victory
innings_victory = False
if team2_score1 + team2_score2 < team1_score1 and isfollowon:
    innings_victory = True
    if toss_chosen == "bat":
        print("Congratulations, you won!")
        team_wins = 1
    else:
        print("Sorry, you lost this game. Better luck next time.")
        team_wins = 0
    innings_win_message = (str(T1)
                           + " wins by an innings and "
                           + str(team1_score1 - (team2_score1 + team2_score2))
                           + " runs")
    print(innings_win_message)
elif team1_score1 + team1_score2 < team2_score1 and not isfollowon:
    innings_victory = True
    if toss_chosen == "bat":
        print("Sorry, you lost this game. Better luck next time.")
        team_wins = 0
    else:
        print("Congratulations, you won!")
        team_wins = 1
    innings_win_message = (str(T2)
                           + " wins by an innings and "
                           + str(team2_score1 - (team1_score1 + team1_score2))
                           + " runs")
    print(innings_win_message)
# If the result is not an innings victory,
# play the second innings of the other team.
if not innings_victory:
    # Selecting the team which has to chase it's opposition's total score
    if isfollowon:
        # Second innings
        team1_score2 = chasingInnings(team_1_array=team2_list,
                                      team_2_array=team1_list,
                                      innings=innings,
                                      bat_bowl_choice=toss_reversed,
                                      opponent_netscore=(team2_score1
                                                         + team2_score2
                                                         - team1_score1),
                                      batting_score=team1_score2,
                                      innings_data=team1_innings2_data,
                                      start_message="Team 1 - Second Innings",
                                      max_overs=math.inf,
                                      max_wickets=wickets_choice,
                                      is_test=True)
        # Score at the end of second innings
        score2_runs = team1_score2[0]
        # Number of wickets fallen at the end of second innings
        score2_wickets = team1_score2[1]
        # Compute the overall score of both teams
        team1_totalscore = team1_score1 + score2_runs
        team2_totalscore = team2_score1 + team2_score2
    else:
        # Second innings
        team2_score2 = chasingInnings(team_1_array=team1_list,
                                      team_2_array=team2_list,
                                      innings=innings,
                                      bat_bowl_choice=toss_chosen,
                                      opponent_netscore=(team1_score1
                                                         + team1_score2
                                                         - team2_score1),
                                      batting_score=team2_score2,
                                      innings_data=team2_innings2_data,
                                      start_message="Team 2 - Second Innings",
                                      max_overs=math.inf,
                                      max_wickets=wickets_choice,
                                      is_test=True)
        # Score at the end of second innings
        score2_runs = team2_score2[0]
        # Number of wickets fallen at the end of second innings
        score2_wickets = team2_score2[1]
        # Compute the overall score of both teams
        team1_totalscore = team1_score1 + team1_score2
        team2_totalscore = team2_score1 + score2_runs

    # Generate the result for all remaining outcomes of a test match
    # (Except a draw by insufficient time)
    # Team batting first successfully defends its score
    if team1_totalscore > team2_totalscore:
        if toss_chosen == "bat":
            print("Congratulations, you won!")
            team_wins = 1
        else:
            print("Sorry, you lost this game. Better luck next time.")
            team_wins = 0
        if isfollowon:
            print(T1, "wins by", 10 - score2_wickets, "wickets")
        else:
            print(T1, "wins by", team1_totalscore - team2_totalscore, "runs")
    # Team batting second successfully chases its target
    elif team1_totalscore < team2_totalscore:
        if toss_chosen == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            team_wins = 0
        else:
            print("Congratulations, you won!")
            team_wins = 1
        if isfollowon:
            print(T2, "wins by", team2_totalscore - team1_totalscore, "runs")
        else:
            print(T2, "wins by", 10 - score2_wickets, "wickets")
    # Scores are level - Match tied.
    else:
        print("Tied")
        team_wins = 0

# Update the playcount and wincount based on the result
player_teamfile = "teams/team" + str(T3) + ".json"
with open(player_teamfile, 'r') as match_file:
    team_data_object = json.load(match_file)
    games_played_old = team_data_object["games_played"]
    games_won_old = team_data_object["games_won"]
games_played_new = games_played_old + 1
if team_wins == 0:
    games_won_new = games_won_old
else:
    games_won_new = games_won_old + 1
team_data_object["games_played"] = games_played_new
team_data_object["games_won"] = games_won_new
match_file.close()
match_file_write = open(player_teamfile, "w")
json.dump(team_data_object, match_file_write, indent=4)
match_file_write.close()

# Save the statistics.
game_data = {
    "isTest": True,
    "isFollowOn": isfollowon,
    "wickets": wickets_choice,
    "innings_data": {
        "team1_innings1_data": team1_innings1_data,
        "team2_innings1_data": team2_innings1_data,
        "team1_innings2_data": team1_innings2_data,
        "team2_innings2_data": team2_innings2_data
        }
    }
saveGame(game_data)

# Display the team stats at the end of the match
winpercentage = (games_won_new * 100) / games_played_new
print("Games played: ", games_played_new)
print("Games won: ", games_won_new)
print("Win Percentage", winpercentage)
end_game_notify = input()
