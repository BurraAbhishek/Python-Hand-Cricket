import random


def shout(s: str) -> str:
    cleaned = ' '.join(s.split())
    return cleaned


# This module contains the commentary notes.

# Wickets

bowled_commentary = [
    "bowled, what a beauty! The middle stump is broken",
    "bowled. The batter misses, but the ball hits the target.",
    "bowled, crashing into the stumps."
    ]

caught_commentary = [
    "caught, that was terrific! The fielder deserves a round of applause...",
    "caught, that was a simple catch to the wicketkeeper.",
    "caught, in the air... and straight into the hands of a fielder.",
    "caught, simple catch to the fielder. That was a soft dismissal."
    ]

lbw_commentary = [
    "LBW, dead plumb! Three reds and no inside edge, the batter has to leave",
    "LBW, right in front of the wickets."
    ]

stumped_commentary = [
    "stumped!! The batter is outside the batting crease \
        and the wickets are put down!",
    "stumped!! That was quick wicketkeeping.",
    "stumped!! That's why you shouldn't overstep the \
        batting crease unnecessarily."
    ]


def outCall() -> str:
    x = random.randint(0, 5)
    if x == 0 or x == 1:
        y = random.choice(bowled_commentary)
    elif x == 2 or x == 3:
        y = random.choice(caught_commentary)
    elif x == 4:
        y = random.choice(lbw_commentary)
    elif x == 5:
        y = random.choice(stumped_commentary)
    return y

# Runs

commentary_6runs = [
    ", SIX, What a shot! That went too far away from the stadium.",
    ", SIX, into the stands.",
    ", SIX, over the fielder and out of the park.",
    ", SIX, this one went over the roof!",
    ", SIX, flat six! This one was slammed into the stands"
    ]

commentary_5runs = [
    ", 5 runs to the batting side. Just a single... \
        but wait! Misfield and four!",
    ", 5 runs to the batting side. Missed run out becomes \
        worse for the fielding side as the ball races to the boundary."
    ]

commentary_4runs = [
    ", FOUR! The ball races to the boundary.",
    ", FOUR! The ball is too fast for the fielders \
        as it races away towards the ropes!",
    ", FOUR! Slammed towards the ropes!",
    ", FOUR! One bounce, and into the stands.",
    ", FOUR! Misfield and four runs."
    ]

commentary_3runs = [
    ", 3 runs",
    ", 3 runs. That was quick running between the wickets",
    ", 3 runs! Brilliant effort by the fielder \
        to stop the ball from hitting the ropes. One run saved."
    ]

commentary_2runs = [
    ", 2 runs",
    ", 2 runs. The fielders have saved two runs for their side.",
    ", 2 runs. Phew! The batters wanted to come back for the second, \
        and they made it just in time as the wicketkeeper collected the ball."
]

commentary_1runs = [
    ", 1 run",
    ", 1 run. Just a single."
]

commentary_0runs = [
    ", NO RUN",
    ", NO RUN. Simple defense.",
    ", NO RUN. Left alone.",
    ", NO RUN. Huge shout for LBW, and it's turned down. Not out.",
    ", NO RUN. The batters wanted to run, but the fielders were too quick.",
]

def scoreRun(score: str, bowler: str, batter: str) -> None:
    if score == '6':
        print(bowler, "to", batter, shout(random.choice(commentary_6runs)))
    elif score == '5':
        print(bowler, "to", batter, shout(random.choice(commentary_5runs)))
    elif score == '4':
        print(bowler, "to", batter, shout(random.choice(commentary_4runs)))
    elif score == '3':
        print(bowler, "to", batter, shout(random.choice(commentary_3runs)))
    elif score == '2':
        print(bowler, "to", batter, shout(random.choice(commentary_2runs)))
    elif score == '1':
        print(bowler, "to", batter, shout(random.choice(commentary_1runs)))
    elif score == '0':
        print(bowler, "to", batter, shout(random.choice(commentary_0runs)))
    elif score == 'W':
        print(bowler, "to", batter, ", OUT", shout(outCall()))
