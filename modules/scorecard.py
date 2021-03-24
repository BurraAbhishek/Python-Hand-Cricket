# Generate the scorecard
# a1: Score Array of the team batting first
# b1: Score Array of the team fielding first
# la: Name of all players of the team batting first
# lc: Name of all players of the team fielding first
# innings: 1st innings or 2nd innings

def scoreCard(al,bl,la,lc,innings):
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
    print("Batting")
    if innings==1:
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
    if innings==2:
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
