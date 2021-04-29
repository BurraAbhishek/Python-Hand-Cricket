import random
import ast
import json
import sys

from modules import hashfunc
from modules import toss
from modules.savegamedata import saveGame
from modules.superover import superOver

from innings.scoring import scoringInnings
from innings.chasing import chasingInnings

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

# Enter the password required to play the match
# input_password: User input password
# match_password: Required password (Either team1 or team2 can type)
with open("team1.json", 'r') as match_file1:
    team_data1 = json.load(match_file1)
match_file1.close()
with open("team2.json", 'r') as match_file2:
    team_data2 = json.load(match_file2)
match_file2.close()
match_password1 = team_data1["password"]
match_password2 = team_data2["password"]
print("Playing game:", team_data1["team_name"], "Vs.", team_data2["team_name"])
input_password = input("Enter match password: ")

# Exit if the password is wrong.
if (not hashfunc.verify_password(input_password, match_password1)
        and not hashfunc.verify_password(input_password, match_password2)):
    print("Sorry, wrong password! ")
    print("Ensure that you type the match password, not your team password.")
    print("Ensure that you enter the correct password before proceeding.")
    wrong_password_notify = input()
    sys.exit(0)

# At this stage the password is correct
try:
    print("By default, the match is a T20, unless otherwise chosen.")
    overs_choice = int(input("Number of overs: "))
except:
    overs_choice = 20
if overs_choice < 1:
    overs_choice = 20
print("This is a", overs_choice, "overs match.")

try:
    print("By default, this is a 10-wickets match, unless specified otherwise")
    wickets_choice = int(input("How many wickets for each team? "))
except:
    wickets_choice = 10
if wickets_choice < 1 or wickets_choice > 10:
    wickets_choice = 10
print("Total:", wickets_choice, "wickets game")

# Variable toss_chosen holds the outcome of the toss: bat or field first
toss_chosen = toss.tossPlay(team_data1, team_data2)

# Prepare the team structure if team1 chooses to bat first
if toss_chosen == "bat":
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

# Prepare the team structure if team1 chooses to field first
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
# Team 1
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
# Team 2
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
                        bat_bowl_choice=toss_chosen,
                        batting_score=score1,
                        innings_data=innings1_data,
                        start_message="First Innings",
                        max_overs=overs_choice,
                        max_wickets=wickets_choice,
                        is_test=False)
innings += 1

# Play the second innings and compute the results.
# team_wins checks if the team wins against the computer or not.
score2 = chasingInnings(team_1_array=team1_list,
                        team_2_array=team2_list,
                        innings=innings,
                        bat_bowl_choice=toss_chosen,
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
# Open the team files and update only human results.
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
    if team_data_object1["isHuman"]:
        team_data_object1["games_played"] += 1
with open(player_teamfile2, 'r') as match_file2:
    team_data_object2 = json.load(match_file2)
    if team_data_object2["isHuman"]:
        team_data_object2["games_played"] += 1
# Team batting first successfully defends its score
if score1 > score2_runs:
    if toss_chosen == "bat":
        if not team_data_object2["isHuman"]:
            print("Congratulations, you won!")
    else:
        if not team_data_object1["isHuman"]:
            print("Sorry, you lost this game. Better luck next time.")
    team_wins = 1
    print(T1, "wins by", score1 - score2_runs, "runs")
# Team batting second successfully chases its target
elif score1 < score2_runs:
    if toss_chosen == "bat":
        if not team_data_object2["isHuman"]:
            print("Sorry, you lost this game. Better luck next time.")
    else:
        if not team_data_object1["isHuman"]:
            print("Congratulations, you won!")
    team_wins = -1
    print(T2, "wins by", 10 - score2_wickets, "wickets")
# Scores are level - Match tied. Proceed to super over
else:
    print("Match tied")
    team_wins = 0 - (superOver(toss_chosen))

# Update the playcount and wincount based on the result
if team_wins == 1:
    if team_data_object1["isHuman"]:
        team_data_object1["games_won"] += 1
    if team_data_object2["isHuman"]:
        team_data_object2["games_lost"] += 1
elif team_wins == -1:
    if team_data_object1["isHuman"]:
        team_data_object1["games_lost"] += 1
    if team_data_object2["isHuman"]:
        team_data_object2["games_won"] += 1
# Save statistics only if the teams have human players.
if team_data_object1["isHuman"]:
    match_file_write1 = open(player_teamfile1, "w")
    json.dump(team_data_object1, match_file_write1, indent=4)
    match_file_write1.close()
if team_data_object2["isHuman"]:
    match_file_write2 = open(player_teamfile2, "w")
    json.dump(team_data_object2, match_file_write2, indent=4)
    match_file_write2.close()

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

# Display the team stats at the end of the match
print(" ")
print("Stats: ")
if team_data_object1["isHuman"]:
    print("Team:", T1)
    winpercentage1 = (team_data_object1["games_won"] * 100)
    winpercentage1 /= team_data_object1["games_played"]
    print("Games played: ", team_data_object1["games_played"])
    print("Games won: ", team_data_object1["games_won"])
    print("Win Percentage", winpercentage1)
if team_data_object2["isHuman"]:
    print("Team:", T2)
    winpercentage2 = (team_data_object2["games_won"] * 100)
    winpercentage2 /= team_data_object2["games_played"]
    print("Games played: ", team_data_object2["games_played"])
    print("Games won: ", team_data_object2["games_won"])
    print("Win Percentage", winpercentage2)
end_game_notify = input()
