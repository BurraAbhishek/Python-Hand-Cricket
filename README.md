# Python-Hand-Cricket
Play hand cricket as an individual or a team of 11 against a team of 11 bots for free on the Python Command Line Interface! More information about the gameplay is available in "Hand Cricket Python App Documentation.pdf" in this repository, which you can read just by clicking on it!

## Getting Started:
### Rules of the game:
This game is a hybrid of cricket and hand cricket and runs on the Python Command-line interface. To know more about hand cricket, visit https://www.instructables.com/id/How-to-Play-Hand-Cricket/

To know more about the laws of cricket, visit https://en.wikipedia.org/wiki/Laws_of_Cricket (Wikipedia link)

#### NOTE: The runs and wickets are determined by the rules of Hand Cricket. The rest of the game follows the Laws of Cricket

The ultimate goal is simple: Score more than your opponent to win.
### Pre-requisites:
To play this game, you need to have Python software installed. The software was built on Python 3.7.4, while the newest release as of 24 March 2021 is Python 3.9.2. Go to https://www.python.org/downloads to install the latest version.

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

### About this project

This is the legacy hand cricket game – implemented in Python and played using the command line interface.

This project was built entirely on Python 3.7.4 and is compatible with all later versions as well. 

The game can be played even without an internet connection.

Tournament mode is not yet included in this game. Customized tournaments can be created using individual team files. For such tournaments, at least 20 MB of disk space is recommended.

Support for test cricket will soon be included.

### Known bugs

Passwords are stored in text files. Until the issue is fixed, it is recommended to store a backup of your text files. Passwords can be changed by going into the text file and changing the password in the array to something else of your choice.

A hack exists wherein a team may abruptly and deliberately close the application to avoid losing a match. This bug is not fixed since a more serious bug, in which unexpected crashes would lead to a loss irrespective of the position, would otherwise overshadow the possibility of victory. 

Rain delay and abandoned matches are not yet implemented in this game. However, deliberately closing the application, as described above, is considered as an abandoned match. Soon, such deliberate abandonments will count as losses.

## Proposed Changes
- Add test cricket module
- Encrypt all passwords. This change is required for security purposes.
- Add support to save game data, so that teams can pick up from where they left off. This is a proposed fix for deliberate abandonment of games.
