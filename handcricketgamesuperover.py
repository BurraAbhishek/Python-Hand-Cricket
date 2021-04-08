import random
import ast

from modules.scorecard import scoreCard
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

# Authenticate the team
old_match_passcode = input("Enter tied match password: ")
uinput_super_over_key = input("Enter super over key: ")
current_super_over_file = open("tied_pass.txt",'r')
current_super_over_keyholder = current_super_over_file.read()
current_super_over_array = ast.literal_eval(current_super_over_keyholder)
password_sent = current_super_over_array[0]
current_super_over_key = str(current_super_over_array[1])
old_toss = current_super_over_array[2]
current_super_over_file.close()
# Simulate a packet transmission over a network and corrupt it if authentication fails.
if old_match_passcode == password_sent and uinput_super_over_key == current_super_over_key:
    password_received = password_sent
else:
    password_received = password_sent + 'NA'
    
# Batting first and fielding first are reversed for every super over game.
if old_toss == 'bat':
    new_toss = "field"
else:
    new_toss = "bat"

# Authentication Successful
if password_received == password_sent:
    overs_choice = 1
    print("Super over")

    wickets_choice = 2
    print("Total:", wickets_choice, "wickets game")

    # Prepare the team structure if the user bats first in this super over
    if new_toss == "bat":
        bat_team_file=open("team1.txt", 'r')
        bat_team_string=bat_team_file.read()
        bat_team_file.close()
        team1_list=ast.literal_eval(bat_team_string)
        T3=team1_list[0]
        games_played_old=int(team1_list[12])
        games_won_old=int(team1_list[13])

        team2_list=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

    # Prepare the team structure if the user fields first in this super over
    else:
        team1_list=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

        bowl_team_file=open("team1.txt", 'r')
        bowl_team_string=bowl_team_file.read()
        bowl_team_file.close()
        team2_list=ast.literal_eval(bowl_team_string)
        T3=team2_list[0]
        games_played_old=int(team2_list[12])
        games_won_old=int(team2_list[13])

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
if password_received == password_sent:
    score1=innFirst(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = new_toss, batting_score = score1, innings_data = innings1_data, runchoice = runchoice, max_overs = overs_choice, max_wickets = wickets_choice, is_test = False)
    innings+=1

# Compute the results. team_wins checks if the team wins against the computer or not.
if password_received == password_sent:        
    score2 = innSecond(team_1_array = team1_list, team_2_array = team2_list, innings = innings, bat_bowl_choice = new_toss, opponent_netscore = score1, batting_score = score2, innings_data = innings2_data, runchoice = runchoice, max_overs = overs_choice, max_wickets = wickets_choice, is_test = False)    
    # Score at the end of second innings
    score2_runs=score2[0]
    # Number of wickets fallen at the end of second innings
    score2_wickets=score2[1]
    # Team batting first successfully defends its score
    if score1>score2_runs:
        if new_toss == "bat":
            print("Congratulations, you won!")
            team_wins=1
        else:
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        print(T1, "wins by super over.")
        super_over_teamfile=open("tied_pass.txt","w")
        super_over_teamfile.write("COMPLETED")
        super_over_teamfile.close()
    # Team batting second successfully chases its target
    elif score1<score2_runs:
        if new_toss == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        else:
            print("Congratulations, you won!")
            team_wins=1
        print(T2, "wins by super over.")
        super_over_teamfile=open("tied_pass.txt","w")
        super_over_teamfile.write("COMPLETED")
        super_over_teamfile.close()
    # Scores are level - Match tied. We need to play another super over to decide the winner
    else:
        print("Tied")
        team_wins=0
        print("You are eligible to play Super Over again to decide the tie! Win the super over and then see the number of games won!")
        new_super_over_key = random.randint(0,1000000000)
        print("Your Super over key is ", new_super_over_key, " Keep it safe since you need it to play the super over.")
        super_over_teamfile=open("tied_pass.txt","w")
        new_super_over_array=[password_sent,new_super_over_key,new_toss]
        super_over_teamfile.write(str(new_super_over_array))
        super_over_teamfile.close()        

    # Record the results
    player_teamname="team"+str(T3)+".txt"
    player_team_file=open(player_teamname, "r")
    player_team_gamestats=player_team_file.read()
    player_team_file.close()
    playcountarray=ast.literal_eval(player_team_gamestats)
    print()
    games_won_old=int(playcountarray[13])
    games_played_new=int(playcountarray[12])

    if team_wins==0:
        games_won_new=games_won_old
    else:
        games_won_new=games_won_old+1
    playcountarray[13]=games_won_new
    player_team_commit=open(player_teamname, "w")
    player_team_commit.write(str(playcountarray))
    player_team_commit.close()

    # Update the win count if the team wins super over    
    winpercentage=(games_won_new*100)/games_played_new
    print("Games played: ", games_played_new)
    print("Games won: ", games_won_new)
    print("Win Percentage", winpercentage)
    end_game_notify=input()

# Authentication fails - User is trying to misuse this feature
if password_received != password_sent:
    wrong_password_notify=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
