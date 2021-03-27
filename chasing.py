import random

from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice

# Second Innings - Main code
def innSecond(team_1_array,team_2_array,innings,bat_bowl_choice,sa,batting_score,lb,runchoice,max_overs,max_wickets):
    T1=team_1_array[0]
    T2=team_2_array[0]

    A1=team_1_array[1]
    A2=team_1_array[2]
    A3=team_1_array[3]
    A4=team_1_array[4]
    A5=team_1_array[5]
    A6=team_1_array[6]
    A7=team_1_array[7]
    A8=team_1_array[8]
    A9=team_1_array[9]
    A10=team_1_array[10]
    A11=team_1_array[11]

    B1=team_2_array[1]
    B2=team_2_array[2]
    B3=team_2_array[3]
    B4=team_2_array[4]
    B5=team_2_array[5]
    B6=team_2_array[6]
    B7=team_2_array[7]
    B8=team_2_array[8]
    B9=team_2_array[9]
    B10=team_2_array[10]
    B11=team_2_array[11]
    print("Second Innings")
    # Display the target
    print("Target:", sa+1)
    # Score for each ball faced in each over of the second innings
    mb=[]
    # Numerical score for each ball faced in an over, second innings
    lp=[]
    # List of all batters not out    
    btindex=[B1,B3,B4,B5,B6,B7,B8,B9,B10,B11,B2]
    # Choose the openers    
    player1=batterChoice(btindex,0,innings,bat_bowl_choice)
    player2=batterChoice(btindex,player1,innings,bat_bowl_choice)
    # Batter statistics
    baindex={B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    # Bowler statistics    
    bindex={A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0],}
    # List of all players in fielding side for bowler selection
    bowlerlist=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]
    b=['']
    score=0
    wicket=0
    # First player is on strike
    onstrike=player1
    gamebIsPlaying=True
    while gamebIsPlaying:
        # i^th over
        for i in range (1, max_overs+1):
            # End the innings if all overs are bowled            
            if i==max_overs:
                gamebIsPlaying=False
            # End the innings if the batting side is all out
            if wicket==max_wickets:
                gamebIsPlaying=False
            # End the innings if the target is successfully chased
            if score>sa:
                gamebIsPlaying=False
            # Innings in progress
            else:
                over=i
                print("Over", i)
                # The fielding side selects the bowler
                bowler=fieldChoice(bowlerlist,innings,bat_bowl_choice)
                # A bowler should not bowl for more than 20% of total overs
                # No bowler is allowed consecutive overs
                if bindex[bowler][0]>=(max_overs/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(max_overs/5):
                        bowlerlist.append(b[i-1])
                # Each over has 6 balls
                for j in range (1, 7):
                    # End the innings as soon as the batting side is all out
                    if wicket==max_wickets or score>sa:
                        gamebIsPlaying=False
                    # Over in progress
                    else:
                        print("Ball", j)
                        # Bat or bowl
                        if bat_bowl_choice == "bat":
                            ra=playOut(bowler,onstrike)
                        else:
                            ra=playIn(bowler,onstrike)
                        # Outcome of the ball: 0, 1, 2, 3, 4, 5, 6
                        if ra != 'W':
                            run=int(ra)
                        # Batter is out
                        else:
                            ra='W'
                            run=0
                            # The team loses a wicket
                            wicket+=1
                            # The bowler claims a wicket (NOTE: run-out is not supported)
                            bindex[bowler][3]+=1
                        # Add the outcome to the score
                        score=score+run
                        # The bowler concedes runs
                        bindex[bowler][2]+=run
                        # The batter scored the runs
                        baindex[onstrike][0]+=run
                        # The batter faced a ball
                        baindex[onstrike][1]+=1
                        # Increment number of 4s if batter scores a boundary
                        if run==4:
                            baindex[onstrike][2]+=1
                        # Increment number of 6s if batter scores a sixer
                        if run==6:
                            baindex[onstrike][3]+=1
                        # Display the outcome and the commentary.    
                        scoreRun(ra,bowler,onstrike)
                        # When a wicket falls,
                        if ra == 'W':
                            # The dismissed batter walks back
                            if onstrike == player1:
                                player1=''
                            elif player2 == onstrike:
                                player2=''
                            # Select the new batter.
                            if bat_bowl_choice == 'field':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2,innings,bat_bowl_choice)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1,innings,bat_bowl_choice)
                                player2=onstrike
                        # Append the outcome to the over. Wicket counts as 'W'
                        mb.append(ra)
                        # Append the outcome to the entire innings
                        lb.append(ra)
                        # Append the scored runs to the over. No run is scored as a batter is dismissed. Hence, wicket counts as 0
                        lp.append(run)
                        # The batters cross for runs. If the runs scored is odd, the batters interchange positions.
                        if run%2 != 0:
                                if onstrike==player1:
                                    onstrike=player2
                                else:
                                    onstrike=player1  
                b.append(bowler)
                # Bowler completed an over. Add to bowler statistics
                bindex[bowler][0]+=1
                # Maiden over bowled
                if lp==[0,0,0,0,0,0]:
                    bindex[bowler][1]+=1
                # Display the over statistics
                print("This over:", mb)
                print("Batting:")
                print(player1,":", baindex[player1][0],"(",baindex[player1][1],")")
                print(player2,":", baindex[player2][0],"(",baindex[player2][1],")")
                print("Bowling:")
                print(bowler,":",bindex[bowler][0],"-",bindex[bowler][1],"-",bindex[bowler][2],"-",bindex[bowler][3])
                print("Score: ", score, "/", wicket)
                print("Need", sa+1-score, "runs to win off", max_overs-i, "overs")
                # Interchange the batters
                if onstrike==player1:
                    onstrike=player2
                else:
                    onstrike=player1
                lp.clear()
                mb.clear()
                # Ready for the next over
                yx=input()
    # Generate the scorecard at the end of the innings.
    scorecard.scoreCard(baindex,bindex,team_1_array,team_2_array,innings)
    return [score, wicket]
