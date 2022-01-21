import random

from modules import scorecard
from modules.commentary import scoreRun
from modules.scoreinput import playBall
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice

# First Innings - Main code

# team_1_array : Array containing name of all players in the first team
# team_2_array : Array containing name of all players in the second team
# innings : First or second innings, except for test cricket.
# bat_bowl_choice : Result of the toss ( bat / field )
# batting_score : The team score, usually initialized to zero.
# innings_data : Contains the details of the innings
# start_message : Message displayed before innings start.
# max_overs : Maximum number of overs available in the innings.
# max_wickets : Maximum number of wickets in the innings.
# is_test : Boolean: Is the game a test match or a limited-overs match?


def scoringInnings(team_1_array: list,
                   team_2_array: list,
                   innings: int,
                   bat_bowl_choice: str,
                   innings_data: dict,
                   start_message: str,
                   max_overs,
                   max_wickets: int,
                   is_test: bool) -> int:
    """ Play the scoring innings

    In limited-overs cricket, this is always the first innings

    Arguments:
    team_1_array : (List) Names of all players in the first team
    team_2_array : (List) Names of all players in the second team
    innings : (int) First or second innings, except for test cricket.
    bat_bowl_choice : (string) Result of the toss ( bat / field )
    batting_score : (int) The team score, usually initialized to zero.
    innings_data : (object) Contains the details of the innings
    start_message : (string) Message displayed before innings start.
    max_overs : (int | float) Maximum number of overs available in the innings.
    max_wickets : (int) Maximum number of wickets in the innings.
    is_test : (Boolean) Is this a test match or a limited-over match?

    Returns:
    int: The score of the team

    Note:
    During runtime, this function modifies the innings data object.

    """

    # Enforce type safety for maximum number of overs.
    if is_test:
        if not isinstance(max_overs, float):
            raise TypeError(
                "The maximum number of overs must be a floating point."
                )
    else:
        if not isinstance(max_overs, int):
            raise TypeError(
                "The maximum number of overs must be an integer."
                )

    # Regenerate team details
    T1 = team_1_array[0]
    T2 = team_2_array[0]
    # Batters
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
    # Bowlers
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
    # Innings setup
    innings_data["battingteam"] = T1
    innings_data["bowlingteam"] = T2
    print(start_message)
    # Score for each ball faced in each over of the first innings
    ball_score = []
    # Numerical score for each ball faced in an over, first innings
    ball_score_integervalue = []
    # List of all batters not out
    batterlist = [A1, A3, A4, A5, A6, A7, A8, A9, A10, A11, A2]
    # Choose the openers
    player1 = batterChoice(batter_list=batterlist,
                           non_striker=0,
                           is_batter_human=team_1_array[14])
    player2 = batterChoice(batter_list=batterlist,
                           non_striker=player1,
                           is_batter_human=team_1_array[14])
    # Batter statistics
    batter_stats = {
        A1: [0, 0, 0, 0],
        A2: [0, 0, 0, 0],
        A3: [0, 0, 0, 0],
        A4: [0, 0, 0, 0],
        A5: [0, 0, 0, 0],
        A6: [0, 0, 0, 0],
        A7: [0, 0, 0, 0],
        A8: [0, 0, 0, 0],
        A9: [0, 0, 0, 0],
        A10: [0, 0, 0, 0],
        A11: [0, 0, 0, 0]
        }
    # Bowler statistics
    bowler_stats = {
        B1: [0, 0, 0, 0],
        B2: [0, 0, 0, 0],
        B3: [0, 0, 0, 0],
        B4: [0, 0, 0, 0],
        B5: [0, 0, 0, 0],
        B6: [0, 0, 0, 0],
        B7: [0, 0, 0, 0],
        B8: [0, 0, 0, 0],
        B9: [0, 0, 0, 0],
        B10: [0, 0, 0, 0],
        B11: [0, 0, 0, 0]
        }
    # List of all players in fielding side for bowler selection
    bowlerlist = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11]
    bowlers_history = ['']
    score = 0
    wicket = 0
    # Over increment variable: i
    i = 1
    # Declaring variable
    isInningsDeclared = False
    # First player is on strike
    onstrike = player1
    gameIsPlaying = True
    while gameIsPlaying:
        # i^th over
        # for i in range(1, max_overs+1):
            # End the innings if all overs are bowled
            if i == max_overs + 1 and not is_test:
                gameIsPlaying = False
            # End the innings if the batting side is all out
            elif wicket == max_wickets:
                gameIsPlaying = False
            # End the innings in test match if innings closed
            elif isInningsDeclared:
                gameIsPlaying = False
            # Innings in progress
            else:
                over = i
                print("Over", i)
                # The fielding side selects the bowler
                bowler = fieldChoice(bowlerlist,
                                     is_bowler_human=team_2_array[14])
                # A bowler can't bowl for more than 20% of total overs
                # No bowler is allowed consecutive overs
                if (bowler_stats[bowler][0] >= (max_overs / 5)
                        or bowler == bowlers_history[i-1]):
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler = random.choice(bowlerlist)
                    if bowler_stats[bowler][0] < (max_overs / 5) or is_test:
                        bowlerlist.append(bowlers_history[i-1])
                # Each over has 6 balls
                for j in range(1, 7):
                    # End the innings once the batting side is all out
                    if wicket == max_wickets:
                        gameIsPlaying = False
                    # End the innings in test match if innings closed
                    elif isInningsDeclared:
                        gameIsPlaying = False
                    # Over in progress
                    else:
                        print("Ball", j)
                        # Bat or bowl
                        ball_outcome = playBall(bowler=bowler,
                                                batter=onstrike,
                                                is_declare_permitted=is_test,
                                                bowler_human=team_2_array[14],
                                                batter_human=team_1_array[14])
                        # Outcome of the ball: 0, 1, 2, 3, 4, 5, 6, W.
                        # To declare test innings: Ball outcome: -1.
                        # Declaring innings works only in test cricket.
                        if ball_outcome == 'Declared':
                            run = 0
                            isInningsDeclared = True
                        # Batter scores runs
                        elif ball_outcome != 'W':
                            run = int(ball_outcome)
                        # Batter is out
                        else:
                            ball_outcome = 'W'
                            run = 0
                            # The team loses a wicket
                            wicket += 1
                            # The bowler claims a wicket
                            # (NOTE: run-out is not supported)
                            bowler_stats[bowler][3] += 1
                        # Add the outcome to the score
                        score = score + run
                        # The bowler bowled a ball.
                        # Add to bowler statistics.
                        if j == 6:
                            # The bowler bowled an over
                            bowler_stats[bowler][0] = int(
                                (((bowler_stats[bowler][0])*10)+5)/10)
                        else:
                            # The bowler did not complete the over.
                            bowler_stats[bowler][0] = (
                                ((bowler_stats[bowler][0])*10)+1)/10
                        # The bowler concedes runs
                        bowler_stats[bowler][2] += run
                        # The batter scored the runs
                        batter_stats[onstrike][0] += run
                        # The batter faced a ball
                        batter_stats[onstrike][1] += 1
                        # Increment number of 4s if batter scores a four
                        if run == 4:
                            batter_stats[onstrike][2] += 1
                        # Increment number of 6s if batter scores a six
                        if run == 6:
                            batter_stats[onstrike][3] += 1
                        # Display the outcome and the commentary.
                        scoreRun(score=ball_outcome,
                                 bowler=bowler,
                                 batter=onstrike)
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
                                c = bat_bowl_choice
                                c1 = team_1_array[14]
                                onstrike = batterChoice(batter_list=batterlist,
                                                        non_striker=player2,
                                                        is_batter_human=c1)
                                player1 = onstrike
                            elif player2 == '':
                                c = bat_bowl_choice
                                c1 = team_1_array[14]
                                onstrike = batterChoice(batter_list=batterlist,
                                                        non_striker=player1,
                                                        is_batter_human=c1)
                                player2 = onstrike
                        # Append the outcome to the over.
                        # Wicket counts as 'W'.
                        ball_score.append(ball_outcome)
                        # Generate the outcome metadata
                        if onstrike == player1:
                            nonstriker = player2
                        else:
                            nonstriker = player1
                        ball_stats = {
                            "bowler": bowler,
                            "batter": onstrike,
                            "nonstriker": nonstriker,
                            "over": i,
                            "ball": j,
                            "result": ball_outcome
                            }
                        # Append the outcome to the entire innings
                        innings_data["data"].append(ball_stats)
                        # Append the scored runs to the over.
                        # No run is scored as a batter is dismissed.
                        # Hence, wicket counts as 0
                        ball_score_integervalue.append(run)
                        # The batters cross for runs.
                        # If odd number of runs are scored,
                        # the batters interchange positions
                        if run % 2 != 0:
                                if onstrike == player1:
                                    onstrike = player2
                                else:
                                    onstrike = player1
                # End if the over. This bowler just completed an over
                bowlers_history.append(bowler)
                # Maiden over bowled
                if ball_score_integervalue == [0, 0, 0, 0, 0, 0]:
                    bowler_stats[bowler][1] += 1
                # Display the over statistics
                print("This over:", ball_score)
                print("Batting:")
                batter1_stats_string = (str(player1)
                                        + " : "
                                        + str(batter_stats[player1][0])
                                        + " ("
                                        + str(batter_stats[player1][1])
                                        + ")")
                print(batter1_stats_string)
                batter2_stats_string = (str(player2)
                                        + " : "
                                        + str(batter_stats[player2][0])
                                        + " ("
                                        + str(batter_stats[player2][1])
                                        + ")")
                print(batter2_stats_string)
                print("Bowling:")
                bowler_stats_string = (str(bowler)
                                       + ": "
                                       + str(bowler_stats[bowler][0])
                                       + " - "
                                       + str(bowler_stats[bowler][1])
                                       + " - "
                                       + str(bowler_stats[bowler][2])
                                       + " - "
                                       + str(bowler_stats[bowler][3]))
                print(bowler_stats_string)
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
            _ = input()
    print("End of 1st innings")
    # Generate the scorecard at the end of the innings.
    scorecard.scoreCard(batters_list=batter_stats,
                        bowlers_list=bowler_stats,
                        team1_players=team_1_array,
                        team2_players=team_2_array,
                        innings=innings)
    innings_data["batter_stats"] = batter_stats
    innings_data["bowler_stats"] = bowler_stats
    innings_data["score"] = score
    innings_data["wickets_lost"] = wicket
    return score
