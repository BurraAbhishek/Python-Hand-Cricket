import random
# Contains the commentary notes.

# Wickets

bowled_commentary = ["bowled, what a beauty! The middle stump is broken","bowled. The batter misses, but the ball hits the target.","bowled, crashing into the stumps."]
caught_commentary = ["caught, that was a terrific blinder. The fielder deserves a round of applause...","caught, that was a simple catch to the wicketkeeper.","caught, in the air...and straight into the hands of a fielder.","caught, simple catch to the fielder. That was a soft dismissal."]
lbw_commentary = ["LBW, dead plumb, the batter is a goner. Three reds and no inside edge, the batter has to leave","LBW, right in front of the wickets."]
stumped_commentary = ["stumped!! The batter is outside the crease and the bails are whipped off!","stumped!! That was quick wicketkeeping.","stumped!! That's why you shouldn't overstep the batting crease unnecessarily."]

def outCall():
    x=random.randint(0, 5)
    if x==0 or x==1:
        y=random.choice(bowled_commentary)
    elif x==2 or x==3:
        y=random.choice(caught_commentary)
    elif x==4:
        y=random.choice(lbw_commentary)
    elif x==5:
        y=random.choice(stumped_commentary)
    return y

# Runs

commentary_6runs = [", SIX, What a shot! That went too far away from the stadium.",", SIX, into the stands.",", SIX, over the fielder and out of the park.",", SIX, this one went over the roof!",", SIX, flat six! This one was slammed into the stands"]
commentary_5runs = [", 5 runs to the batting side. Just a single, but wait...misfield and four.",", 5 runs to the batting side. Missed run out becomes worse for the fielding side as the ball races to the boundary."]
commentary_4runs = [", FOUR! The ball races to the boundary.",", FOUR! The fielders can't stop the ball as it races towards the boundary.",", FOUR! Slammed towards the ropes!",", FOUR! One bounce, and into the stands.",", FOUR! Misfield and four runs."]

def scoreRun(score,bowler,batter):
    if score == '6':
        print(bowler, "to", batter, random.choice(commentary_6runs))
    elif score == '5':
        print(bowler, "to", batter, random.choice(commentary_5runs))
    elif score == '4':
        print(bowler, "to", batter, random.choice(commentary_4runs))
    elif score == '3':
        print(bowler, "to", batter, ", 3 runs")
    elif score == '2':
        print(bowler, "to", batter, ", 2 runs")
    elif score == '1':
        print(bowler, "to", batter, ", 1 run")
    elif score == '0':
        print(bowler, "to", batter, ", NO RUN")
    elif score == 'W':
        print(bowler, "to", batter, ", OUT", outCall())
