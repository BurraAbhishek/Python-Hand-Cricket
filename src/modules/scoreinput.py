from modules.batting import bat
from modules.bowling import bowl

# Player is batting


def playBall(bowler, batter, is_declare_permitted, bowler_human, batter_human):
    print("This is a hand cricket-based cricket match.")
    print("Bowler:", bowler)
    print("Batter on strike:", batter)
    bowl_score = bowl(bowler, bowler_human)
    bat_score = bat(batter, is_declare_permitted, batter_human)
    if(bowl_score == bat_score):
        outcome = 'W'
    elif(bowl_score == '7'):
        outcome = '6'
    elif(bat_score == '-2'):
        outcome = '0'
    else:
        outcome = str(bat_score)
    return outcome
