import random
import ast

from modules import toss
from modules import scorecard
from modules.commentary import scoreRun
from modules.batting import playIn
from modules.bowling import playOut
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice

# Score for each ball faced in the first innings
l=[]
# Score for each ball faced in each over of the first innings
m=[]
# First innings score
sa=0
# Second innings score
sb=0
# Innings: 1st innings or 2nd innings
inig=1
# Possible scores in a ball.
runchoice=('0','1','2','3','4','5','6','W')

# Enter the password required to play the match
# pwod: User input password
# pchek: Required password
pwod=input("Enter match password: ")
fz=open("gpascd.txt",'r')
pchek=fz.read()
fz.close()

# Validate the password and proceed to the game
if pwod == pchek:
    try:
        opchoice=int(input("For how many overs game? Default: T20, Your choice: "))
    except:
        opchoice=20
    if opchoice<1:
        opchoice=20
    print("Match is for", opchoice, "overs.")

    try:
        wa=int(input("For how many wickets would you want to play? Default: 10 wicket game, Your choice: "))
    except:
        wa=10
    if wa<1 or wa>10:
        wa=10
    print("Total:", wa, "wickets game")

    # Variable za holds the decision from the toss: bat first or field first
    za=toss.tossPlay()

    # Prepare the team structure if player chooses to bat first
    if za == "bat":
        f=open("team1.txt", 'r')
        sla=f.read()
        f.close()
        la=ast.literal_eval(sla)
        T3=la[0]
        gpldb=int(la[12])
        gwonb=int(la[13])

        lc=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

    # Prepare the team structure if player chooses to field first
    else:
        la=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

        g=open("team1.txt", 'r')
        slb=g.read()
        g.close()
        lc=ast.literal_eval(slb)
        T3=lc[0]
        gpldb=int(lc[12])
        gwonb=int(lc[13])

    # The two teams look like this:

    #['P1','A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11']
    #['P2','B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11']

    T1=la[0]
    T2=lc[0]

    A1=la[1]
    A2=la[2]
    A3=la[3]
    A4=la[4]
    A5=la[5]
    A6=la[6]
    A7=la[7]
    A8=la[8]
    A9=la[9]
    A10=la[10]
    A11=la[11]

    B1=lc[1]
    B2=lc[2]
    B3=lc[3]
    B4=lc[4]
    B5=lc[5]
    B6=lc[6]
    B7=lc[7]
    B8=lc[8]
    B9=lc[9]
    B10=lc[10]
    B11=lc[11]

# First Innings - Main code
def innFirst():
    print("First Innings")
    # Initialize team score = 0
    sa=0
    # List of all batters not out
    btindex=[A1,A3,A4,A5,A6,A7,A8,A9,A10,A11,A2]
    # Choose the openers
    player1=batterChoice(btindex,0,inig,za)
    player2=batterChoice(btindex,player1,inig,za)
    # Batter statistics
    baindex={A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0]}
    # Bowler statistics
    bindex={B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    # List of all players in fielding side for bowler selection
    bowlerlist=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11]
    b=['']
    score=0
    wicket=0
    # First player is on strike
    onstrike=player1
    gameIsPlaying=True
    while gameIsPlaying:
        # i^th over
        for i in range (1, opchoice+1):
            # End the innings if all overs are bowled
            if i==opchoice:
                gameIsPlaying=False
            # End the innings if the batting side is all out
            if wicket==wa:
                gameIsPlaying=False
            # Innings in progress
            else:
                over=i
                print("Over", i)
                # The fielding side selects the bowler
                bowler=fieldChoice(bowlerlist,inig,za)
                # A bowler should not bowl for more than 20% of total overs
                # No bowler is allowed consecutive overs
                if bindex[bowler][0]>=(opchoice/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(opchoice/5):
                        bowlerlist.append(b[i-1])
                # Each over has 6 balls
                for j in range (1, 7):
                    # End the innings as soon as the batting side is all out
                    if wicket==wa:
                        gameIsPlaying=False
                    # Over in progress
                    else:
                        print("Ball", j)
                        # Bat or bowl
                        if za == "bat":
                            ra=playIn(bowler,onstrike)
                        else:
                            ra=playOut(bowler,onstrike)
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
                            if za == 'bat':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2,inig,za)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1,inig,za)
                                player2=onstrike
                        # Append the outcome to the over. Wicket counts as 'W'
                        m.append(ra)
                        # Append the outcome to the entire innings
                        l.append(ra)
                        # Append the scored runs to the over. No run is scored as a batter is dismissed. Hence, wicket counts as 0
                        lq.append(run)
                        # The batters cross for runs. If the runs scored is odd, the batters interchange positions.
                        if run%2 != 0:
                                if onstrike==player1:
                                    onstrike=player2
                                else:
                                    onstrike=player1
                # End if the over. This bowler just completed an over
                b.append(bowler)
                # Bowler completed an over. Add to bowler statistics
                bindex[bowler][0]+=1
                # Maiden over bowled
                if lq==[0,0,0,0,0,0]:
                    bindex[bowler][1]+=1
                # Display the over statistics
                print("This over:", m)
                print("Batting:")
                print(player1,":", baindex[player1][0],"(",baindex[player1][1],")")
                print(player2,":", baindex[player2][0],"(",baindex[player2][1],")")
                print("Bowling:")
                print(bowler,":",bindex[bowler][0],"-",bindex[bowler][1],"-",bindex[bowler][2],"-",bindex[bowler][3])
                print("Score: ", score, "/", wicket)
            # Interchange the batters
            if onstrike==player1:
                onstrike=player2
            else:
                onstrike=player1
            m.clear()
            lq.clear()
            # Ready for the next over
            yx=input()
    print("End of 1st innings")
    # Generate the scorecard at the end of the innings.
    scorecard.scoreCard(baindex,bindex,la,lc,inig)
    return score

# Play the first innings.
if pwod == pchek:
    sa=innFirst()
    inig+=1

# Second Innings - Main code
def innSecond():
    print("Second Innings")
    # Display the target
    print("Target:", sa+1)
    # List of all batters not out    
    btindex=[B1,B3,B4,B5,B6,B7,B8,B9,B10,B11,B2]
    # Choose the openers    
    player1=batterChoice(btindex,0,inig,za)
    player2=batterChoice(btindex,player1,inig,za)
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
        for i in range (1, opchoice+1):
            # End the innings if all overs are bowled            
            if i==opchoice:
                gamebIsPlaying=False
            # End the innings if the batting side is all out
            if wicket==wa:
                gamebIsPlaying=False
            # End the innings if the target is successfully chased
            if score>sa:
                gamebIsPlaying=False
            # Innings in progress
            else:
                over=i
                print("Over", i)
                # The fielding side selects the bowler
                bowler=fieldChoice(bowlerlist,inig,za)
                # A bowler should not bowl for more than 20% of total overs
                # No bowler is allowed consecutive overs
                if bindex[bowler][0]>=(opchoice/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(opchoice/5):
                        bowlerlist.append(b[i-1])
                # Each over has 6 balls
                for j in range (1, 7):
                    # End the innings as soon as the batting side is all out
                    if wicket==wa or score>sa:
                        gamebIsPlaying=False
                    # Over in progress
                    else:
                        print("Ball", j)
                        # Bat or bowl
                        if za == "bat":
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
                            if za == 'field':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2,inig,za)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1,inig,za)
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
                print("Need", sa+1-score, "runs to win off", opchoice-i, "overs")
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
    scorecard.scoreCard(baindex,bindex,la,lc,inig)
    return [score, wicket]

# Compute the results. team_wins checks if the team wins against the computer or not.
if pwod == pchek:        
    sb=innSecond()
    # Score at the end of second innings
    sba=sb[0]
    # Number of wickets fallen at the end of second innings
    sbb=sb[1]
    # Team batting first successfully defends its score
    if sa>sba:
        if za == "bat":
            print("Congratulations, you won!")
            team_wins=1
        else:
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        print(T1, "wins by", sa-sba, "runs")
    # Team batting second successfully chases its target
    elif sa<sba:
        if za == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        else:
            print("Congratulations, you won!")
            team_wins=1
        print(T2, "wins by", 10-sbb, "wickets")
    # Scores are level - Match tied. Proceed to super over
    else:
        print("Tied")
        team_wins=0
        print("You are eligible to play Super Over to decide the tie! Win the super over and then see the number of games won!")
        new_super_over_key = random.randint(0,1000000000)
        print("Your Super over key is ", new_super_over_key, " Keep it safe since you need it to play the super over.")
        new_super_over_keyholder=open("tiepascd.txt","w")
        new_super_over_keyarray=[pchek,new_super_over_key,za]
        new_super_over_keyholder.write(str(new_super_over_keyarray))
        new_super_over_keyholder.close()

    # Open the team file and read its contents
    gwona="team"+str(T3)+".txt"
    gplda=open(gwona, "r")
    gpldh=gplda.read()
    gplda.close()
    playcountarray=ast.literal_eval(gpldh)
    print()
    # Get number of games played and won
    gpldc=int(int(playcountarray[12])+1)
    gwonb=int(playcountarray[13])

    # Update the playcount and wincount based on the result
    if team_wins==0:
        gwonc=gwonb
    else:
        gwonc=gwonb+1
    playcountarray[12]=gpldc
    playcountarray[13]=gwonc
    gwonf=open(gwona, "w")
    gwonf.write(str(playcountarray))
    gwonf.close()

    # Display the team stats at the end of the match    
    winpercentage=(gwonc*100)/gpldc
    print("Games played: ", gpldc)
    print("Games won: ", gwonc)
    print("Win Percentage", winpercentage)
    end_game_notify=input()

# Team fails to authenticate
if pwod != pchek:
    wrong_password_notify=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
