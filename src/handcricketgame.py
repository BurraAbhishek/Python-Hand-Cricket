import random
import ast
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
from modules.savegamedata import saveGame

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
toss_chosen = toss.tossPlay()

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
# Team batting first successfully defends its score
if score1 > score2_runs:
    if toss_chosen == "bat":
        print("Congratulations, you won!")
        team_wins = 1
    else:
        print("Sorry, you lost this game. Better luck next time.")
        team_wins = 0
    print(T1, "wins by", score1 - score2_runs, "runs")
# Team batting second successfully chases its target
elif score1 < score2_runs:
    if toss_chosen == "bat":
        print("Sorry, you lost this game. Better luck next time.")
        team_wins = 0
    else:
        print("Congratulations, you won!")
        team_wins = 1
    print(T2, "wins by", 10 - score2_wickets, "wickets")
# Scores are level - Match tied. Proceed to super over
else:
    print("Match tied")
    team_wins = 0
    print("You are eligible to play Super Over to decide the tie! ")
    print("Win the super over and then see the number of games won!")
    new_super_over_key = random.randint(0, 1000000000)
    print("Your Super over key is ", new_super_over_key)
    print("Keep it safe since you need it to play the super over.")
    new_super_over_keyholder = open("tied_pass.txt", "w")
    new_super_over_keyarray = [match_password, new_super_over_key, toss_chosen]
    new_super_over_keyholder.write(str(new_super_over_keyarray))
    new_super_over_keyholder.close()

# Update the playcount and wincount based on the result
games_played_new = games_played_old + 1
if team_wins == 0:
    games_won_new = games_won_old
else:
    games_won_new = games_won_old + 1
player_teamfile = "teams/team" + str(T3) + ".json"
with open(player_teamfile, 'r') as match_file:
    team_data_object = json.load(match_file)
    team_data_object["games_played"] = games_played_new
    team_data_object["games_won"] = games_won_new
match_file.close()
match_file_write = open(player_teamfile, "w")
json.dump(team_data_object, match_file_write, indent=4)
match_file_write.close()

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
winpercentage = (games_won_new * 100) / games_played_new
print("Games played: ", games_played_new)
print("Games won: ", games_won_new)
print("Win Percentage", winpercentage)
end_game_notify = input()
