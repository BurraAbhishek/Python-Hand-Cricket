import random

from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice

# First Innings - Main code

# team_1_array : Array containing name of all players in the first team
# team_2_array : Array containing name of all players in the second team
# innings : First or second innings, except for test cricket.
# bat_bowl_choice : Result of the toss ( bat / field )
# batting_score : The team score, usually initialized to zero.
# innings_data : Ball-by-ball score
# start_message : Message displayed before innings start.
# max_overs : Maximum number of overs available in the innings.
# max_wickets : Maximum number of wickets in the innings.
# is_test : Boolean: Is the game a test match (is_test = true) or a limited-over match? (is_test = false)

def scoringInnings(team_1_array, team_2_array, innings, bat_bowl_choice, batting_score, innings_data, start_message, max_overs, max_wickets, is_test):
    # Regenerate team details
    T1 = team_1_array[0]
    T2 = team_2_array[0]

    A1 = team_1_array[1]
    A2 = team_1_array[2]
    A3 = team_1_array[3]
    A4 = team_1_array[4]
    A5 = team_1_array[5]
    A6 = team_1_array[6]
    A7 = team_1_array[7]
    A8 = team_1_array[8]
    A9 = team_1_array[9]
    A10 = team_1_array[10]
    A11 = team_1_array[11]

    B1 = team_2_array[1]
    B2 = team_2_array[2]
    B3 = team_2_array[3]
    B4 = team_2_array[4]
    B5 = team_2_array[5]
    B6 = team_2_array[6]
    B7 = team_2_array[7]
    B8 = team_2_array[8]
    B9 = team_2_array[9]
    B10 = team_2_array[10]
    B11 = team_2_array[11]
    print(start_message)
    # Initialize team score = 0
    batting_score = 0
    # Score for each ball faced in each over of the first innings
    ball_score = []
    # Numerical score for each ball faced in an over, first innings
    ball_score_integervalue = []
    # List of all batters not out
    batterlist = [A1,A3,A4,A5,A6,A7,A8,A9,A10,A11,A2]
    # Choose the openers
    player1 = batterChoice(batter_list = batterlist, non_striker = 0, innings = innings, user_choice_batfield = bat_bowl_choice)
    player2 = batterChoice(batter_list = batterlist, non_striker = player1, innings = innings, user_choice_batfield = bat_bowl_choice)
    # Batter statistics
    batter_stats = {A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0]}
    # Bowler statistics
    bowler_stats = {B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    # List of all players in fielding side for bowler selection
    bowlerlist = [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11]
    bowlers_history = ['']
    score = 0
    wicket = 0
    # Over increment variable: i
    i = 1
    # First player is on strike
    onstrike = player1
    gameIsPlaying = True
    while gameIsPlaying:
        # i^th over
        # for i in range (1, max_overs+1):
            # End the innings if all overs are bowled
            if i == max_overs + 1 and not is_test:
                gameIsPlaying = False
            # End the innings if the batting side is all out
            elif wicket == max_wickets:
                gameIsPlaying = False
            # Innings in progress
            else:
                over = i
                print("Over", i)
                # The fielding side selects the bowler
                bowler = fieldChoice(bowlerlist, innings, bat_bowl_choice)
                # A bowler should not bowl for more than 20% of total overs
                # No bowler is allowed consecutive overs
                if bowler_stats[bowler][0] >= (max_overs / 5) or bowler == bowlers_history[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bowler_stats[bowler][0] < (max_overs / 5) or is_test:
                        bowlerlist.append(bowlers_history[i-1])
                # Each over has 6 balls
                for j in range (1, 7):
                    # End the innings as soon as the batting side is all out
                    if wicket == max_wickets:
                        gameIsPlaying = False
                    # Over in progress
                    else:
                        print("Ball", j)
                        # Bat or bowl
                        if bat_bowl_choice == "bat":
                            ball_outcome = playIn(bowler = bowler, batter = onstrike, is_declare_permitted = is_test)
                        else:
                            ball_outcome = playOut(bowler = bowler, batter = onstrike)
                        # Outcome of the ball: 0, 1, 2, 3, 4, 5, 6, W.
                        # To declare test innings: Ball outcome: -1. Only works in test cricket module
                        if ball_outcome == -1:
                            gameIsPlaying = False
                        # Batter scores runs
                        if ball_outcome != 'W':
                            run = int(ball_outcome)
                        # Batter is out
                        else:
                            ball_outcome = 'W'
                            run = 0
                            # The team loses a wicket
                            wicket += 1
                            # The bowler claims a wicket (NOTE: run-out is not supported)
                            bowler_stats[bowler][3] += 1
                        # Add the outcome to the score
                        score = score + run
                        # The bowler bowled a ball. Add to bowler statistics
                        if j == 6:
                            # The bowler bowled an over
                            bowler_stats[bowler][0] = int((((bowler_stats[bowler][0])*10)+5)/10)
                        else:
                            # The bowler did not complete the over.
                            bowler_stats[bowler][0] = (((bowler_stats[bowler][0])*10)+1)/10
                        # The bowler concedes runs
                        bowler_stats[bowler][2] += run
                        # The batter scored the runs
                        batter_stats[onstrike][0] += run
                        # The batter faced a ball
                        batter_stats[onstrike][1] += 1
                        # Increment number of 4s if batter scores a boundary
                        if run == 4:
                            batter_stats[onstrike][2] += 1
                        # Increment number of 6s if batter scores a sixer
                        if run == 6:
                            batter_stats[onstrike][3] += 1
                        # Display the outcome and the commentary.
                        scoreRun(score = ball_outcome, bowler = bowler, batter = onstrike)
                        # When a wicket falls,
                        if ball_outcome == 'W' and wicket < max_wickets:
                            # The dismissed batter walks back
                            if onstrike == player1:
                                player1 = ''
                            elif player2 == onstrike:
                                player2 = ''
                            # Select the new batter.
                            if bat_bowl_choice == 'bat':
                                batterlist.append('')
                            if player1 == '':
                                onstrike = batterChoice(batter_list = batterlist, non_striker = player2, innings = innings, user_choice_batfield = bat_bowl_choice)
                                player1 = onstrike
                            elif player2 == '':
                                onstrike = batterChoice(batter_list = batterlist, non_striker = player1, innings = innings, user_choice_batfield = bat_bowl_choice)
                                player2 = onstrike
                        # Append the outcome to the over. Wicket counts as 'W'
                        ball_score.append(ball_outcome)
                        # Append the outcome to the entire innings
                        innings_data.append(ball_outcome)
                        # Append the scored runs to the over. No run is scored as a batter is dismissed. Hence, wicket counts as 0
                        ball_score_integervalue.append(run)
                        # The batters cross for runs. If the runs scored is odd, the batters interchange positions.
                        if run % 2 != 0:
                                if onstrike == player1:
                                    onstrike = player2
                                else:
                                    onstrike = player1
                # End if the over. This bowler just completed an over
                bowlers_history.append(bowler)
                # Maiden over bowled
                if ball_score_integervalue == [0,0,0,0,0,0]:
                    bowler_stats[bowler][1] += 1
                # Display the over statistics
                print("This over:", ball_score)
                print("Batting:")
                print(player1, ":", batter_stats[player1][0], "(", batter_stats[player1][1], ")")
                print(player2, ":", batter_stats[player2][0], "(", batter_stats[player2][1], ")")
                print("Bowling:")
                print(bowler,":",bowler_stats[bowler][0],"-",bowler_stats[bowler][1],"-",bowler_stats[bowler][2],"-",bowler_stats[bowler][3])
                print("Score: ", score, "/", wicket)
            # Interchange the batters
            if onstrike == player1:
                onstrike = player2
            else:
                onstrike = player1
            ball_score.clear()
            ball_score_integervalue.clear()
            # Prepare the next over
            i += 1
            # Ready for the next over
            alert_ready_nextover = input()
    print("End of 1st innings")
    # Generate the scorecard at the end of the innings.
    scorecard.scoreCard(batters_list = batter_stats, bowlers_list = bowler_stats, team1_players = team_1_array, team2_players = team_2_array, innings = innings)
    return score
