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

def scoreRun(r,tx,rx):
    if r == '6':
        print(tx, "to", rx, random.choice(commentary_6runs))
    elif r == '5':
        print(tx, "to", rx, random.choice(commentary_5runs))
    elif r == '4':
        print(tx, "to", rx, random.choice(commentary_4runs))
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
