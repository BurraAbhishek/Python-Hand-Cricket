import random
import ast

from modules import toss
from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice

from innings.scoring import innFirst
from innings.chasing import innSecond

# Score for each ball faced in the first innings
innings1_data=[]
# Score for each ball faced in the second innings
innings2_data=[]
# First innings score
score1=0
# Second innings score
score2=0
# Innings: 1st innings or 2nd innings
innings=1
# Possible scores in a ball.
runchoice=('0','1','2','3','4','5','6','W')

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
        overs_choice=int(input("For how many overs game? Default: T20, Your choice: "))
    except:
        overs_choice=20
    if overs_choice<1:
        overs_choice=20
    print("Match is for", overs_choice, "overs.")

    try:
        wickets_choice=int(input("For how many wickets would you want to play? Default: 10 wicket game, Your choice: "))
    except:
        wickets_choice=10
    if wickets_choice<1 or wickets_choice>10:
        wickets_choice=10
    print("Total:", wickets_choice, "wickets game")

    # Variable toss_chosen holds the decision from the toss: bat first or field first
    toss_chosen = toss.tossPlay()

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

# Play the first innings.
if input_password == match_password:
    score1=innFirst(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = toss_chosen, batting_score = score1, innings_data = innings1_data, runchoice = runchoice, max_overs = overs_choice, max_wickets = wickets_choice, is_test = False)
    innings+=1

# Play the second innings and compute the results. team_wins checks if the team wins against the computer or not.
if input_password == match_password:        
    score2 = innSecond(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = toss_chosen, opponent_netscore = score1, batting_score = score2, innings_data = innings2_data, runchoice = runchoice, max_overs = overs_choice, max_wickets = wickets_choice, is_test = False)
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

# Team fails to authenticate
if input_password != match_password:
    wrong_password_notify=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
