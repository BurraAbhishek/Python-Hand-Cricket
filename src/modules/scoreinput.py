from modules.batting import bat
from modules.bowling import bowl


def playBall(
    bowler: str, 
    batter: str, 
    is_declare_permitted: bool, 
    bowler_human: bool, 
    batter_human: bool
    ) -> str:

    print("This is a hand cricket-based cricket match.")
    print("Bowler:", bowler)
    print("Batter on strike:", batter)
    bowl_score = bowl(bowler_human)
    bat_score = bat(is_declare_permitted, batter_human)
    if(bowl_score == bat_score):
        outcome = 'W'
    elif(bowl_score == '7'):
        outcome = '6'
    elif(bat_score == '-2'):
        outcome = '0'
    else:
        outcome = str(bat_score)
    if(bat_score == '-1'):
        if is_declare_permitted:
            outcome = 'Declared'
        else:
            outcome = '0'
    return outcome
