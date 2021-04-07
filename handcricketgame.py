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
l=[]
# Score for each ball faced in the second innings
lb=[]
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

# Play the first innings.
if pwod == pchek:
    sa=innFirst(la,lc,inig,za,sa,l,runchoice,opchoice,wa)
    inig+=1

# Play the second innings and compute the results. team_wins checks if the team wins against the computer or not.
if pwod == pchek:        
    sb=innSecond(la,lc,inig,za,sa,sb,lb,runchoice,opchoice,wa)
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
    
