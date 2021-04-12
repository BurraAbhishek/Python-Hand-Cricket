# Python-Hand-Cricket
Play hand cricket as an individual or as a team of 11 against a team of 11 bots for free on the Python Command Line Interface! More information about the gameplay is available in the [documentation](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/docs/Hand%20Cricket%20Python%20App%20Documentation.pdf).

## NOTE:

All the links will soon be updated. To avoid breaking any links, it is recommended to use the v2.0 branch until all the links have moved.

## About this game

This is the legacy hand cricket game – implemented in Python and played using the command line interface.

This game was built entirely on Python 3.7.4. It is compatible with all releases of Python 3.5 and later.

The game can be played even without an internet connection.

Tournament mode is not yet included in this game. Customized tournaments can be created using individual team files. For such tournaments, at least 20 MB of disk space is recommended.

Full support for test cricket will soon be included.

This game supports almost all of the laws of cricket which can be implemented in a computer program.

NOTE: To play only the traditional hand cricket game, set a large number of overs (or infinite overs) and 1 wicket as the game settings.

### Modules:
- [Team setup](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/setupateam.py): Setup your team and it's members. Team members need not be unique, since only one person may actually be an entire team, i.e., the person wants to play as an individual. In that case, the person's name can be the name of each team member.
- [Match registration](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/registerformatch.py): Register a match between your team and a computer-controlled opposition team. This module prepares an interface to recognize your team as the computer team's opposition for the upcoming match. Of course, you can play the match whenever you want. Set up your team first before using this module.
- [Limited-overs game](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/handcricketgame.py): The limited-overs cricket module. 
- [Super over](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/handcricketgamesuperover.py): The super over tiebreaker. This module is accessible only if a limited-overs match is tied.
- [Test cricket](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/handcricketgametestcricket.py): The test cricket module. 
#### Submodules:
- [innings/scoring.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/innings/scoring.py): The innings in which teams try to score big. In limited-overs cricket, this is always the first innings. In test cricket, this is the non-chasing innings.
- [innings/chasing.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/innings/chasing.py): The innings in which teams chase the opposition's total.
- [modules/batterchoice.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/batterchoice.py): From a given list of players, select the player who will bat now.
- [modules/batting.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/batting.py): Module which contains the code for batting. The required module in this code is called playIn(), because the player's input contributes to the team's total.
- [modules/bowlerchoice.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/bowlerchoice.py): From a given list of players, select the bowler.
- [modules/bowling.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/bowling.py): Module which contains the code for bowling. The required module in this code is called playOut(), because the player's input contributes to dismissing the opposition (The batter should be out).
- [modules/commentary.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/commentary.py): Generate the commentary for each ball bowled, based on the result of that ball.
- [modules/scorecard.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/scorecard.py): Generate the innings scorecard at the end of each innings.
- [modules/toss.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/toss.py): Toss to decide which team bats / fields first. This code is not compatible with super over games, since this decision is the reverse of their decision in the latest tied game
- [modules/followon.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/modules/followon.py): Only works for test cricket. Determine whether the team which batted first can enforce the follow-on or not. This code runs only if the team batting first leads by a certain threshold.

## Getting Started:
### Rules of the game:
This game is a hybrid of cricket and hand cricket and runs on the Python Command-line interface. To know more about hand cricket, visit https://www.instructables.com/id/How-to-Play-Hand-Cricket/

To know more about the laws of cricket, visit https://en.wikipedia.org/wiki/Laws_of_Cricket (Wikipedia link)

#### NOTE: The scoring and dismissal mechanisms are determined by the rules of Hand Cricket. The rest of the game follows the Laws of Cricket

The ultimate goal is simple: Score more than your opponent to win.
### Pre-requisites:
To play this game, you need to have Python software installed. The software was built on Python 3.7.4, while the newest release as of 4 April 2021 is Python 3.9.4. Go to https://www.python.org/downloads to install the latest version.

Supported platforms:
-	Microsoft Windows 7 or later
-	Android API 24 or later (Apps are available on the Play Store)
-	Mac OS X 10.6 or later
-	Linux 

Either download this entire repository to play this game, or clone this repository using:

```
$ git clone https://github.com/BurraAbhishek/Python-Hand-Cricket.git
```

Disk space: 10 MB (minimum).

## Features of cricket which are not implemented in this game
- Run out: The batter fails to reach the crease before the wickets fall.
- Extras: Wides, no balls, free hits, dead balls. 
- This game implements a 6-run penalty for wrong bowling input. In actual cricket, various infractions by the fielding side can lead to 5 penalty runs.
- Rain delay and DLS par score
- Innings forfeiture in test cricket.

### Known bugs

Passwords are stored in text files. Until the issue is fixed, it is recommended to store a backup of your text files. Passwords can be changed by going into the text file and changing the password in the array to something else of your choice.

A hack exists wherein a team may abruptly and deliberately close the application to avoid losing a match. This bug will be fixed soon. 

Rain delay and abandoned matches are not yet implemented in this game. However, deliberately closing the application, as described above, is considered as an abandoned match. Soon, such deliberate abandonments will count as losses.
