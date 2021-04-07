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

# Authenticate the team
old_match_passcode = input("Enter tied match password: ")
uinput_super_over_key = input("Enter super over key: ")
current_super_over_file = open("tiepascd.txt",'r')
current_super_over_keyholder = current_super_over_file.read()
current_super_over_array = ast.literal_eval(current_super_over_keyholder)
pchek = current_super_over_array[0]
current_super_over_key = str(current_super_over_array[1])
zab = current_super_over_array[2]
current_super_over_file.close()
if old_match_passcode == pchek and uinput_super_over_key == current_super_over_key:
    pwod = pchek
else:
    pwod = pchek + 'NA'
    
# Batting first and fielding first are reversed for every super over game.
if zab == 'bat':
    za = "field"
else:
    za = "bat"

# Authentication Successful
if pwod == pchek:
    opchoice = 1
    print("Super over")

    wa = 2
    print("Total:", wa, "wickets game")

    # Prepare the team structure if the user bats first in this super over
    if za == "bat":
        f=open("team1.txt", 'r')
        sla=f.read()
        f.close()
        la=ast.literal_eval(sla)
        T3=la[0]
        gpldb=int(la[12])
        gwonb=int(la[13])

        lc=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

    # Prepare the team structure if the user fields first in this super over
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

# Compute the results. team_wins checks if the team wins against the computer or not.
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
        print(T1, "wins by super over.")
        super_over_teamfile=open("tiepascd.txt","w")
        super_over_teamfile.write("COMPLETED")
        super_over_teamfile.close()
    # Team batting second successfully chases its target
    elif sa<sba:
        if za == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            team_wins=0
        else:
            print("Congratulations, you won!")
            team_wins=1
        print(T2, "wins by super over.")
        super_over_teamfile=open("tiepascd.txt","w")
        super_over_teamfile.write("COMPLETED")
        super_over_teamfile.close()
    # Scores are level - Match tied. We need to play another super over to decide the winner
    else:
        print("Tied")
        team_wins=0
        print("You are eligible to play Super Over again to decide the tie! Win the super over and then see the number of games won!")
        new_super_over_key = random.randint(0,1000000000)
        print("Your Super over key is ", new_super_over_key, " Keep it safe since you need it to play the super over.")
        super_over_teamfile=open("tiepascd.txt","w")
        new_super_over_array=[pchek,new_super_over_key,za]
        super_over_teamfile.write(str(new_super_over_array))
        super_over_teamfile.close()        

    # Record the results
    gwona="team"+str(T3)+".txt"
    gplda=open(gwona, "r")
    gpldh=gplda.read()
    gplda.close()
    playcountarray=ast.literal_eval(gpldh)
    print()
    gwonb=int(playcountarray[13])
    gpldc=int(playcountarray[12])

    if team_wins==0:
        gwonc=gwonb
    else:
        gwonc=gwonb+1
    playcountarray[13]=gwonc
    gwonf=open(gwona, "w")
    gwonf.write(str(playcountarray))
    gwonf.close()

    # Update the win count if the team wins super over    
    winpercentage=(gwonc*100)/gpldc
    print("Games played: ", gpldc)
    print("Games won: ", gwonc)
    print("Win Percentage", winpercentage)
    end_game_notify=input()

# Authentication fails - User is trying to misuse this feature
if pwod != pchek:
    wrong_password_notify=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
