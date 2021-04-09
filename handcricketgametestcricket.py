import random
import ast
import math

from modules import toss
from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice
from modules.followon import checkFollowOn

from innings.scoring import scoringInnings
from innings.chasing import chasingInnings

# Score for each ball faced in the first innings of the first team
team1_innings1_data=[]
# Score for each ball faced in the first innings of the second team
team2_innings1_data=[]
# Score for each ball faced in the second innings of the first team
team1_innings2_data=[]
# Score for each ball faced in the second innings of the second team
team2_innings2_data=[]
# First innings score, first team
team1_score1=0
# Second innings score, first team
team1_score2=0
# First innings score, second team
team2_score1=0
# Second innings score, second team
team2_score2=0
# Innings: Assign the role of each team: bat / field. Doesn't represent 1st or 2nd innings.
innings=1
# Is follow-on enforced? Decided after both teams complete their first innings.
isfollowon = False

# Enter the password required to play the match
# input_password: User input password
# match_password: Required password
input_password = input("Enter match password: ")
match_pass_file = open("game_pass.txt",'r')
match_password = match_pass_file.read()
match_pass_file.close()

# Validate the password and proceed to the game
if input_password == match_password:
    try:
        wickets_choice = int(input("For how many wickets would you want to play? Default: 10 wicket game, Your choice: "))
    except:
        wickets_choice = 10
    if wickets_choice < 1 or wickets_choice > 10:
        wickets_choice = 10
    print("Total:", wickets_choice, "wickets game")
    try:
        followon_choice = int(input("Minimum runs required for follow-on: ? Default: 200 runs, Minimum: 50 runs, Your choice: "))
    except:
        followon_choice = 200
    if followon_choice < 50:
        followon_choice = 200
    print("For follow-on to be permitted, the team batting first should score at least", followon_choice, "runs more than the team fielding first.")

    # Variable toss_chosen holds the decision from the toss: bat first or field first
    toss_chosen = toss.tossPlay()
    if toss_chosen == "bat":
        toss_reversed = "field"
    else:
        toss_reversed = "bat"

    # Prepare the team structure if player chooses to bat first
    if toss_chosen == "bat":
        bat_team_file = open("team1.txt", 'r')
        bat_team_string = bat_team_file.read()
        bat_team_file.close()
        team1_list = ast.literal_eval(bat_team_string)
        T3=team1_list[0]
        games_played_old = int(team1_list[12])
        games_won_old = int(team1_list[13])

        team2_list = ['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

    # Prepare the team structure if player chooses to field first
    else:
        team1_list = ['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

        bowl_team_file = open("team1.txt", 'r')
        bowl_team_string = bowl_team_file.read()
        bowl_team_file.close()
        team2_list = ast.literal_eval(bowl_team_string)
        T3 = team2_list[0]
        games_played_old = int(team2_list[12])
        games_won_old = int(team2_list[13])

    # The two teams look like this:

    #['P1','A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11']
    #['P2','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11']

    T1=team1_list[0]
    T2=team2_list[0]

    A1=team1_list[1]
    A2=team1_list[2]
    A3=team1_list[3]
    A4=team1_list[4]
    A5=team1_list[5]
    A6=team1_list[6]
    A7=team1_list[7]
    A8=team1_list[8]
    A9=team1_list[9]
    A10=team1_list[10]
    A11=team1_list[11]

    B1=team2_list[1]
    B2=team2_list[2]
    B3=team2_list[3]
    B4=team2_list[4]
    B5=team2_list[5]
    B6=team2_list[6]
    B7=team2_list[7]
    B8=team2_list[8]
    B9=team2_list[9]
    B10=team2_list[10]
    B11=team2_list[11]

# Play the first innings of both sides.
if input_password == match_password:
    team1_score1=scoringInnings(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = toss_chosen, batting_score = team1_score1, innings_data = team1_innings1_data, start_message = "Team 1 - First Innings", max_overs = math.inf, max_wickets = wickets_choice, is_test = True)
    team2_score1=scoringInnings(team_1_array = team2_list, team_2_array = team1_list, innings = innings, bat_bowl_choice = toss_reversed, batting_score = team2_score1, innings_data = team2_innings1_data, start_message = "Team 2 - First Innings", max_overs = math.inf, max_wickets = wickets_choice, is_test = True)

# Check if follow-on is required or not, and then proceed accordingly.
if input_password == match_password:
    if team1_score1 - team2_score1 >= followon_choice:
        isfollowon = checkFollowOn(team1_name = T1, team2_name = T2, p_name = T3)

# Assign the innings accordingly.
if input_password == match_password:
    if isfollowon:
        print("Follow-on enforced by",T1)
        team2_score2=scoringInnings(team_1_array = team2_list, team_2_array = team1_list, innings = innings, bat_bowl_choice = toss_reversed, batting_score = team2_score2, innings_data = team2_innings2_data, start_message = "Team 2 - Second Innings", max_overs = math.inf, max_wickets = wickets_choice, is_test = True)
        innings = 1
    else:
        print(T1,"did not enforce follow on. Hence,",T1,"will continue batting.")
        innings = 1
        team1_score2=scoringInnings(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = toss_chosen, batting_score = team1_score2, innings_data = team1_innings2_data, start_message = "Team 1 - Second Innings", max_overs = math.inf, max_wickets = wickets_choice, is_test = True)
        innings = 2

'''
# @TODO 1. Assign the correct team the target to be chased using the chasingInnings module
# @TODO 2. Add innings victory support
# @TODO 3. Decide the other win conditions.
# @TODO 4. In case of a tie, declare match drawn. It will not count as a win and no super over will be provided.


Replace the lines within the triple quotes with the new code.
# Play the second innings and compute the results. team_wins checks if the team wins against the computer or not.
if input_password == match_password:        
    score2 = chasingInnings(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = toss_chosen, opponent_netscore = score1, batting_score = score2, innings_data = innings2_data, runchoice = runchoice, max_overs = -1, max_wickets = wickets_choice, is_test = False)
    # Score at the end of second innings
    score2_runs = score2[0]
    # Number of wickets fallen at the end of second innings
    score2_wickets = score2[1]
    # Team batting first successfully defends its score
    if score1 > score2_runs:
        if toss_chosen == "bat":
            print("Congratulations, you won!")
            team_wins=1
        else:
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        print(T1, "wins by", score1-score2_runs, "runs")
    # Team batting second successfully chases its target
    elif score1 < score2_runs:
        if toss_chosen == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        else:
            print("Congratulations, you won!")
            team_wins=1
        print(T2, "wins by", 10-score2_wickets, "wickets")
    # Scores are level - Match tied. Proceed to super over
    else:
        print("Tied")
        team_wins=0
        print("You are eligible to play Super Over to decide the tie! Win the super over and then see the number of games won!")
        new_super_over_key = random.randint(0,1000000000)
        print("Your Super over key is ", new_super_over_key, " Keep it safe since you need it to play the super over.")
        new_super_over_keyholder = open("tied_pass.txt","w")
        new_super_over_keyarray = [match_password,new_super_over_key,toss_chosen]
        new_super_over_keyholder.write(str(new_super_over_keyarray))
        new_super_over_keyholder.close()

    # Open the team file and read its contents
    player_teamname = "team"+str(T3)+".txt"
    player_team_file = open(player_teamname, "r")
    player_team_gamestats = player_team_file.read()
    player_team_file.close()
    playcountarray = ast.literal_eval(player_team_gamestats)
    print()
    # Get number of games played and won
    games_played_new = int(int(playcountarray[12])+1)
    games_won_old = int(playcountarray[13])

    # Update the playcount and wincount based on the result
    if team_wins==0:
        games_won_new = games_won_old
    else:
        games_won_new = games_won_old+1
    playcountarray[12] = games_played_new
    playcountarray[13] = games_won_new
    player_team_commit=open(player_teamname, "w")
    player_team_commit.write(str(playcountarray))
    player_team_commit.close()

    # Display the team stats at the end of the match    
    winpercentage=(games_won_new*100)/games_played_new
    print("Games played: ", games_played_new)
    print("Games won: ", games_won_new)
    print("Win Percentage", winpercentage)
    end_game_notify = input()
'''

# Team fails to authenticate
if input_password != match_password:
    wrong_password_notify=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
