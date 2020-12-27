import random
import ast
d={}
l=[]
m=[]
lb=[]
mb=[]
lq=[]
lp=[]
sa=0
sb=0
inig=1
runchoice=('0','1','2','3','4','5','6','W')

pwod=input("Enter match password: ")
fz=open("gpascd.txt",'r')
pchek=fz.read()
fz.close()

def tossPlay():
    print("Time for the toss!")
    try:
        numInput = int(input("Choose a number between 0 and 6: "))
    except:
        numInput=0
    turn = input("Odd or Even? zero is counted as even and the sum of your input and AI input is checked. ")

    c=(numInput + (random.randint(0, 1)))

    if c%2 == 0:
        if turn == 'Even':
            print("You won the toss");
            toss=1
        else:
            print("You lost the toss");
            toss=0
    else:
        if turn == 'Odd':
            print("You won the toss");
            toss=1
        else:
            print("You lost the toss");
            toss=0

    if toss==1:
        z=input("Choose to bat first or field first: ")
        print("You won the toss and chose to", z,"first");
    else:
        oinput=random.randint(0, 1)
        if oinput==0:
            z="bat"
            print("Your opponent won the toss and chose to field first")
        else:
            z="field"
            print("Your opponent won the toss and chose to bat first")
    return z

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

    za=tossPlay()

    if za == "bat":
        f=open("team1.txt", 'r')
        sla=f.read()
        f.close()
        la=ast.literal_eval(sla)
        T3=la[0]
        gpldb=int(la[12])
        gwonb=int(la[13])

        lc=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

    else:
        la=['Computer', 'CPU1', 'CPU2', 'CPU3', 'CPU4', 'CPU5', 'CPU6', 'CPU7', 'CPU8', 'CPU9', 'CPU10', 'CPU11']

        g=open("team1.txt", 'r')
        slb=g.read()
        g.close()
        lc=ast.literal_eval(slb)
        T3=lc[0]
        gpldb=int(lc[12])
        gwonb=int(lc[13])

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

def playIn(fd,bt):
    print("This is hand cricket batting. Bowler:", fd, ". Batter on strike:", bt)
    print("Any other input means NO RUN")
    prum=input("Bat any number from 0 to 6: ")
    try:
        prun=int(prum)
    except:
        prun=0
    orun=random.randint(0, 6)
    if prun<0 or prun>6:
        rr='0'
    else:
        if prun==orun:
            rr='W'
        else:
            rr=str(prun)
    return rr

def playOut(fd,bt):
    print("This is hand cricket batting. Bowler:", fd, ". Batter on strike:", bt)
    print("Any other input means free sixer for opponent.")
    prum=input("Bowl any number from 0 to 6: ")
    try:
        prun=int(prum)
    except:
        prun=6
    orun=random.randint(0, 6)
    if prun<0 or prun>6:
        rr='6'
    else:
        if prun==orun:
            rr='W'
        else:
            rr=str(orun)
    return rr

def outCall():
    x=random.randint(0, 5)
    if x==0 or x==1:
        y="bowled, what a beauty! The middle stump is broken"
    elif x==2 or x==3:
        y="caught, that was a terrific blinder. The fielder deserves a round of applause..."
    elif x==4:
        y="LBW, dead plumb, the batter is a goner. Three reds and no inside edge, the batter has to leave"
    elif x==5:
        y="stumped!! The batter is outside the crease and the bails are whipped off!"
    return y

def scoreRun(r,tx,rx):
    if r == '6':
        print(tx, "to", rx, ", SIX, That went too far away from the stadium. What a shot.")
    elif r == '5':
        print(tx, "to", rx, ", poor bowling. The ball races to the boundary and the batters cross for a run. 5 runs")
    elif r == '4':
        print(tx, "to", rx, ", FOUR. The ball races to the boundary and the fielders can do nothing")
    elif r == '3':
        print(tx, "to", rx, ", 3 runs")
    elif r == '2':
        print(tx, "to", rx, ", 2 runs")
    elif r == '1':
        print(tx, "to", rx, ", 1 run")
    elif r == '0':
        print(tx, "to", rx, ", NO RUN")
    elif r == 'W':
        print(tx, "to", rx, ", OUT", outCall())

def batterChoice(bta,stk):
    if inig==1:
        if za == 'field':
            btf=random.choice(bta)
        elif za == 'bat':
            print("Remaining batters:",bta)
            bth=input("Choose your batter: ")
            btvrify=0
            for i in range(0,len(bta)):
                if bth==bta[i] and bth!=stk and bth!='':
                    btvrify+=1
                    batchox=bth
            if btvrify==1:
                btf=batchox
            else:
                btf=random.choice(bta)
              
    else:
        if za == 'bat':
            btf=random.choice(bta)
        elif za == 'field':
            print("Remaining batters:",bta)            
            bth=input("Choose your batter: ")
            btvrify=0
            for i in range(0,len(bta)):
                if bth==bta[i] and bth!=stk and bth!='':
                    btvrify+=1
                    batchox=bth
            if btvrify==1:
                btf=batchox
            else:
                btf=random.choice(bta)
    bta.pop(bta.index(btf))             
    return btf

def fieldChoice(bowlerlistx):
    if inig==1:
        if za == 'bat':
            bowlerx=random.choice(bowlerlistx)
        elif za == 'field':
            print("Bowlers:",bowlerlistx)
            bowlchoice=input("Choose your bowler: ")
            bvrify=0
            for i in range(0,11):
                if bowlchoice==bowlerlistx[i]:
                    bvrify+=1
                    bowlchox=bowlchoice
            if bvrify!=0:
                bowlerx=bowlchox
            else:
                bowlerx=random.choice(bowlerlistx)
    else:
        if za == 'field':
            bowlerx=random.choice(bowlerlistx)
        elif za == 'bat':
            print("Bowlers:",bowlerlistx)
            bowlchoice=input("Choose your bowler: ")
            bvrify=0
            for i in range(0,11):
                if bowlchoice==bowlerlistx[i]:
                    bvrify+=1
                    bowlchox=bowlchoice
            if bvrify!=0:
                bowlerx=bowlchox
            else:
                bowlerx=random.choice(bowlerlistx)
    return bowlerx

        
def scoreCard(al,bl):
    print("Batting")
    if inig==1:
        print(A1,"scored",al[A1][0],"runs off",al[A1][1],"balls, hitting",al[A1][2],"fours and",al[A1][3],"sixes.")
        print(A2,"scored",al[A2][0],"runs off",al[A2][1],"balls, hitting",al[A2][2],"fours and",al[A2][3],"sixes.")
        print(A3,"scored",al[A3][0],"runs off",al[A3][1],"balls, hitting",al[A3][2],"fours and",al[A3][3],"sixes.")
        print(A4,"scored",al[A4][0],"runs off",al[A4][1],"balls, hitting",al[A4][2],"fours and",al[A4][3],"sixes.")
        print(A5,"scored",al[A5][0],"runs off",al[A5][1],"balls, hitting",al[A5][2],"fours and",al[A5][3],"sixes.")
        print(A6,"scored",al[A6][0],"runs off",al[A6][1],"balls, hitting",al[A6][2],"fours and",al[A6][3],"sixes.")
        print(A7,"scored",al[A7][0],"runs off",al[A7][1],"balls, hitting",al[A7][2],"fours and",al[A7][3],"sixes.")
        print(A8,"scored",al[A8][0],"runs off",al[A8][1],"balls, hitting",al[A8][2],"fours and",al[A8][3],"sixes.")
        print(A9,"scored",al[A9][0],"runs off",al[A9][1],"balls, hitting",al[A9][2],"fours and",al[A9][3],"sixes.")
        print(A10,"scored",al[A10][0],"runs off",al[A10][1],"balls, hitting",al[A10][2],"fours and",al[A10][3],"sixes.")
        print(A11,"scored",al[A11][0],"runs off",al[A11][1],"balls, hitting",al[A11][2],"fours and",al[A11][3],"sixes.")
    else:
        print(B1,"scored",al[B1][0],"runs off",al[B1][1],"balls, hitting",al[B1][2],"fours and",al[B1][3],"sixes.")
        print(B2,"scored",al[B2][0],"runs off",al[B2][1],"balls, hitting",al[B2][2],"fours and",al[B2][3],"sixes.")
        print(B3,"scored",al[B3][0],"runs off",al[B3][1],"balls, hitting",al[B3][2],"fours and",al[B3][3],"sixes.")
        print(B4,"scored",al[B4][0],"runs off",al[B4][1],"balls, hitting",al[B4][2],"fours and",al[B4][3],"sixes.")
        print(B5,"scored",al[B5][0],"runs off",al[B5][1],"balls, hitting",al[B5][2],"fours and",al[B5][3],"sixes.")
        print(B6,"scored",al[B6][0],"runs off",al[B6][1],"balls, hitting",al[B6][2],"fours and",al[B6][3],"sixes.")
        print(B7,"scored",al[B7][0],"runs off",al[B7][1],"balls, hitting",al[B7][2],"fours and",al[B7][3],"sixes.")
        print(B8,"scored",al[B8][0],"runs off",al[B8][1],"balls, hitting",al[B8][2],"fours and",al[B8][3],"sixes.")
        print(B9,"scored",al[B9][0],"runs off",al[B9][1],"balls, hitting",al[B9][2],"fours and",al[B9][3],"sixes.")
        print(B10,"scored",al[B10][0],"runs off",al[B10][1],"balls, hitting",al[B10][2],"fours and",al[B10][3],"sixes.")
        print(B11,"scored",al[B11][0],"runs off",al[B11][1],"balls, hitting",al[B11][2],"fours and",al[B11][3],"sixes.")
    print("\nBowling")
    if inig==2:
        print(A1,":",bl[A1][0],"-",bl[A1][1],"-",bl[A1][2],"-",bl[A1][3])
        print(A2,":",bl[A2][0],"-",bl[A2][1],"-",bl[A2][2],"-",bl[A2][3])
        print(A3,":",bl[A3][0],"-",bl[A3][1],"-",bl[A3][2],"-",bl[A3][3])
        print(A4,":",bl[A4][0],"-",bl[A4][1],"-",bl[A4][2],"-",bl[A4][3])
        print(A5,":",bl[A5][0],"-",bl[A5][1],"-",bl[A5][2],"-",bl[A5][3])
        print(A6,":",bl[A6][0],"-",bl[A6][1],"-",bl[A6][2],"-",bl[A6][3])
        print(A7,":",bl[A7][0],"-",bl[A7][1],"-",bl[A7][2],"-",bl[A7][3])
        print(A8,":",bl[A8][0],"-",bl[A8][1],"-",bl[A8][2],"-",bl[A8][3])
        print(A9,":",bl[A9][0],"-",bl[A9][1],"-",bl[A9][2],"-",bl[A9][3])
        print(A10,":",bl[A10][0],"-",bl[A10][1],"-",bl[A10][2],"-",bl[A10][3])
        print(A11,":",bl[A11][0],"-",bl[A11][1],"-",bl[A11][2],"-",bl[A11][3])
    else:
        print(B1,":",bl[B1][0],"-",bl[B1][1],"-",bl[B1][2],"-",bl[B1][3])
        print(B2,":",bl[B2][0],"-",bl[B2][1],"-",bl[B2][2],"-",bl[B2][3])
        print(B3,":",bl[B3][0],"-",bl[B3][1],"-",bl[B3][2],"-",bl[B3][3])
        print(B4,":",bl[B4][0],"-",bl[B4][1],"-",bl[B4][2],"-",bl[B4][3])
        print(B5,":",bl[B5][0],"-",bl[B5][1],"-",bl[B5][2],"-",bl[B5][3])
        print(B6,":",bl[B6][0],"-",bl[B6][1],"-",bl[B6][2],"-",bl[B6][3])
        print(B7,":",bl[B7][0],"-",bl[B7][1],"-",bl[B7][2],"-",bl[B7][3])
        print(B8,":",bl[B8][0],"-",bl[B8][1],"-",bl[B8][2],"-",bl[B8][3])
        print(B9,":",bl[B9][0],"-",bl[B9][1],"-",bl[B9][2],"-",bl[B9][3])
        print(B10,":",bl[B10][0],"-",bl[B10][1],"-",bl[B10][2],"-",bl[B10][3])
        print(B11,":",bl[B11][0],"-",bl[B11][1],"-",bl[B11][2],"-",bl[B11][3])
    print('')
        
def innFirst():
    print("First Innings")
    sa=0
    btindex=[A1,A3,A4,A5,A6,A7,A8,A9,A10,A11,A2]
    player1=batterChoice(btindex,0)
    #btindex.pop(btindex.index(player1))
    player2=batterChoice(btindex,player1)
    #btindex.pop(btindex.index(player2))
    baindex={A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0]}
    bindex={B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    bowlerlist=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11]
    b=['']
    score=0
    wicket=0
    onstrike=player1
    gameIsPlaying=True
    while gameIsPlaying:
        for i in range (1, opchoice+1):
            if i==opchoice:
                gameIsPlaying=False
            if wicket==wa:
                gameIsPlaying=False
            else:
                over=i
                print("Over", i)
                bowler=fieldChoice(bowlerlist)
                if bindex[bowler][0]>=(opchoice/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(opchoice/5):
                        bowlerlist.append(b[i-1])
                for j in range (1, 7):
                    if wicket==wa:
                        gameIsPlaying=False
                    else:
                        print("Ball", j)
                        if za == "bat":
                            ra=playIn(bowler,onstrike)
                        else:
                            ra=playOut(bowler,onstrike)
                        if ra != 'W':
                            run=int(ra)
                        else:
                            ra='W'
                            run=0
                            wicket+=1
                            bindex[bowler][3]+=1
                        score=score+run
                        bindex[bowler][2]+=run
                        baindex[onstrike][0]+=run
                        baindex[onstrike][1]+=1
                        if run==4:
                            baindex[onstrike][2]+=1
                        if run==6:
                            baindex[onstrike][3]+=1
                        scoreRun(ra,bowler,onstrike)
                        if ra == 'W':
                            if onstrike == player1:
                                player1=''
                            elif player2 == onstrike:
                                player2=''
                            
                            if za == 'bat':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1)
                                player2=onstrike
                        m.append(ra)
                        l.append(ra)
                        lq.append(run)
                        if run%2 != 0:
                                if onstrike==player1:
                                    onstrike=player2
                                else:
                                    onstrike=player1  
                b.append(bowler)
                bindex[bowler][0]+=1
                if lq==[0,0,0,0,0,0]:
                    bindex[bowler][1]+=1
                print("This over:", m)
                print("Batting:")
                print(player1,":", baindex[player1][0],"(",baindex[player1][1],")")
                print(player2,":", baindex[player2][0],"(",baindex[player2][1],")")
                print("Bowling:")
                print(bowler,":",bindex[bowler][0],"-",bindex[bowler][1],"-",bindex[bowler][2],"-",bindex[bowler][3])
                print("Score: ", score, "/", wicket)
            if onstrike==player1:
                onstrike=player2
            else:
                onstrike=player1
            m.clear()
            lq.clear()
            yx=input()
    print("End of 1st innings")
    scoreCard(baindex,bindex)
    return score

if pwod == pchek:
    sa=innFirst()
    inig+=1

def innSecond():
    print("Second Innings")
    print("Target:", sa+1)
    btindex=[B1,B3,B4,B5,B6,B7,B8,B9,B10,B11,B2]
    player1=batterChoice(btindex,0)
    #btindex.pop(btindex.index(player1))
    player2=batterChoice(btindex,player1)
    #btindex.pop(btindex.index(player2))
    baindex={B1:[0,0,0,0], B2:[0,0,0,0], B3:[0,0,0,0], B4:[0,0,0,0], B5:[0,0,0,0], B6:[0,0,0,0], B7:[0,0,0,0], B8:[0,0,0,0], B9:[0,0,0,0], B10:[0,0,0,0], B11:[0,0,0,0]}
    bindex={A1:[0,0,0,0], A2:[0,0,0,0], A3:[0,0,0,0], A4:[0,0,0,0], A5:[0,0,0,0], A6:[0,0,0,0], A7:[0,0,0,0], A8:[0,0,0,0], A9:[0,0,0,0], A10:[0,0,0,0], A11:[0,0,0,0],}
    bowlerlist=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]
    b=['']
    score=0
    wicket=0
    onstrike=player1
    gamebIsPlaying=True
    while gamebIsPlaying:
        for i in range (1, opchoice+1):
            if i==opchoice:
                gamebIsPlaying=False
            if wicket==wa or score>sa:
                gamebIsPlaying=False
            else:
                over=i
                print("Over", i)
                bowler=fieldChoice(bowlerlist)
                if bindex[bowler][0]>=(opchoice/5) or bowler == b[i-1]:
                    bowlerlist.pop(bowlerlist.index(bowler))
                    bowler=random.choice(bowlerlist)
                    if bindex[bowler][0]<(opchoice/5):
                        bowlerlist.append(b[i-1])
                for j in range (1, 7):
                    if wicket==wa or score>sa:
                        gamebIsPlaying=False
                    else:
                        print("Ball", j)
                        if za == "bat":
                            ra=playOut(bowler,onstrike)
                        else:
                            ra=playIn(bowler,onstrike)
                        if ra != 'W':
                            run=int(ra)
                        else:
                            ra='W'
                            run=0
                            wicket+=1
                            bindex[bowler][3]+=1
                        score=score+run
                        bindex[bowler][2]+=run
                        baindex[onstrike][0]+=run
                        baindex[onstrike][1]+=1
                        if run==4:
                            baindex[onstrike][2]+=1
                        if run==6:
                            baindex[onstrike][3]+=1                        
                        scoreRun(ra,bowler,onstrike)
                        if ra == 'W':
                            if onstrike == player1:
                                player1=''
                            elif player2 == onstrike:
                                player2=''
                            
                            if za == 'field':
                                btindex.append('')
                            if player1 == '':
                                onstrike=batterChoice(btindex,player2)
                                player1=onstrike
                            elif player2 == '':
                                onstrike=batterChoice(btindex,player1)
                                player2=onstrike
                        mb.append(ra)
                        lb.append(ra)
                        lp.append(run)
                        if run%2 != 0:
                                if onstrike==player1:
                                    onstrike=player2
                                else:
                                    onstrike=player1  
                b.append(bowler)
                bindex[bowler][0]+=1
                if lp==[0,0,0,0,0,0]:
                    bindex[bowler][1]+=1
                print("This over:", mb)
                print("Batting:")
                print(player1,":", baindex[player1][0],"(",baindex[player1][1],")")
                print(player2,":", baindex[player2][0],"(",baindex[player2][1],")")
                print("Bowling:")
                print(bowler,":",bindex[bowler][0],"-",bindex[bowler][1],"-",bindex[bowler][2],"-",bindex[bowler][3])
                print("Score: ", score, "/", wicket)
                print("Need", sa+1-score, "runs to win off", opchoice-i, "overs")
                if onstrike==player1:
                    onstrike=player2
                else:
                    onstrike=player1
                lp.clear()
                mb.clear()
                yx=input()
    scoreCard(baindex,bindex)
    return [score, wicket]

if pwod == pchek:        
    sb=innSecond()
    sba=sb[0]
    sbb=sb[1]
    if sa>sba:
        if za == "bat":
            print("Congratulations, you won!")
            zza=1
        else:
            print("Sorry, you lost this game. Better luck next time.")
            zza=0
        print(T1, "wins by", sa-sba, "runs")
    elif sa<sba:
        if za == "bat":
            print("Sorry, you lost this game. Better luck next time.")
            zza=0
        else:
            print("Congratulations, you won!")
            zza=1
        print(T2, "wins by", 10-sbb, "wickets")
    else:
        print("Tied")
        zza=0
        print("You are eligible to play Super Over to decide the tie! Win the super over and then see the number of games won!")
        xzzzint = random.randint(0,1000000000)
        print("Your Super over key is ", xzzzint, " Keep it safe since you need it to play the super over.")
        xzzzza=open("tiepascd.txt","w")
        xzzzzl=[pchek,xzzzint,za]
        xzzzza.write(str(xzzzzl))
        xzzzza.close()

    gwona="team"+str(T3)+".txt"
    gplda=open(gwona, "r")
    gpldh=gplda.read()
    gplda.close()
    dtja=ast.literal_eval(gpldh)
    print()
    gpldc=int(int(dtja[12])+1)
    gwonb=int(dtja[13])

    if zza==0:
        gwonc=gwonb
    else:
        gwonc=gwonb+1
    dtja[12]=gpldc
    dtja[13]=gwonc
    gwonf=open(gwona, "w")
    gwonf.write(str(dtja))
    gwonf.close()

        
    winpercentage=(gwonc*100)/gpldc
    print("Games played: ", gpldc)
    print("Games won: ", gwonc)
    print("Win Percentage", winpercentage)
    xyaaa=input()

if pwod != pchek:
    xza=input("Sorry, wrong password! Make sure that you enter the correct password before proceeding")
