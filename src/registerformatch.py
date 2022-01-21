import json
import datetime
from modules import hashfunc
from modules import savegamedata


def setup_match() -> None:
    """ Setup a game between two teams.

    Arguments: None

    While running the function, the team file is read from the 'teams' folder.

    Returns:
    None. Updates the match pairings

    """

    # Teams are identified by team name.
    teamname = input("Team name: ")
    team_data_filename = "teams/team" + teamname + ".json"
    # Check if the team file exists
    try:
        # Open the team file
        with open(team_data_filename, 'r') as team_data_file:
            # Read from the json file
            team_data_json = json.load(team_data_file)
        team_key = input("Enter your team key: ")
        # Check if the key matches.
        if hashfunc.verify_password(team_key, team_data_json["team_key"]):
            # The team will play against an opponent.
            print("Team", teamname, "is now ready to play a match!")
            # Determine if the opponent is a human or a computer.
            print('Do you want to play against a human team or computer team?')
            print("To play against a human team, type 'human' and hit 'Enter'")
            print("To play against the usual computer team, just hit 'Enter'.")
            opponent_choice = input()
            # Get game ID.
            gameidfile = savegamedata.getUniqueSavefile()
            gameid = gameidfile[12:-5]
            thisGameID = True
            # If opponent is computer, load the computer team as opponent.
            if(opponent_choice != 'human'):
                pairing = {
                    "team1": teamname,
                    "team1_human": True,
                    "team1_confirm": True,
                    "team2": "Computer",
                    "team2_human": False,
                    "team2_confirm": True,
                    "gameid": hashfunc.hash_password(gameid),
                    "timestamp": datetime.datetime.now().timestamp()
                    }
                insertGameLog(pairing)
            # If opponent is human, pick an opponent or create a fresh pairing.
            if(opponent_choice == "human"):
                print("Do you want to choose your opponent (Y/N)")
                chooseopponentflag = input()
                if chooseopponentflag == 'Y':
                    # Create a match pairing.
                    opponent_teamname = findHumanOpponentExists(teamname)
                    if not checkPairingChosen(teamname, opponent_teamname):
                        pairing = {
                            "team1": teamname,
                            "team1_human": True,
                            "team1_confirm": True,
                            "team2": opponent_teamname,
                            "team2_human": True,
                            "team2_confirm": False,
                            "gameid": hashfunc.hash_password(gameid),
                            "timestamp": datetime.datetime.now().timestamp()
                            }
                        insertGameLog(pairing)
                    else:
                        thisGameID = False
                if chooseopponentflag != 'Y':
                    pairing = {
                        "team1": teamname,
                        "team1_human": True,
                        "team1_confirm": True,
                        "team2": None,
                        "team2_human": True,
                        "team2_confirm": False,
                        "gameid": hashfunc.hash_password(gameid),
                        "timestamp": datetime.datetime.now().timestamp()
                        }
                    insertGameLog(pairing)
            print("Your match is registered.")
            if thisGameID:
                print("Your match ID is: ")
                print(gameid)
                print("Share this match ID only with your opponent.")
            else:
                print("Please ask your opponent for the match ID.")
            _ = input("Press 'Enter' key to complete this process.")
        else:
            print("The keys did not match.")
            print("Forgot your key? Contact support for key reset.")
            _ = input()

    # If team file doesn't exist, we can't setup the match.
    except:
        print("Team", teamname, "is not available.")
        print("Please set up your team before proceeding.")
        _ = input()


def findHumanOpponentExists(player: str) -> str:
    """ Checks if an opponent team exists """

    opponent_teamname = input("Choose your opponent team by name: ")
    try:
        if player == opponent_teamname:
            raise Exception("Playing against yourself is strictly prohibited.")
        teamfilename = "teams/team" + opponent_teamname + ".json"
        teamfile = open(teamfilename, "r")
        teamfile.close()
    except:
        print("Chosen team doesn't exist. ")
        opponent_teamname = findHumanOpponentExists(player)
    return opponent_teamname


def checkPairingChosen(player: str, opponent: str) -> bool:
    """ Chooses a match among various pairings 

    Arguments:
    player: str. The name of your team.
    opponent: str. The name of your opponent team.

    Returns:
    A boolean value which checks if the pairing is confirmed.

    """

    try:
        chooseFrozen = False
        with open("matchpairings.json", 'r') as matchpairings:
            pairings = json.load(matchpairings)
            for i in pairings:
                if i["team1"] == opponent and not chooseFrozen:
                    if i["team2"] == player:
                        i["team2_confirm"] = True
                        i["timestamp"] = datetime.datetime.now().timestamp()
                        chooseFrozen = True
                    elif i["team2"] is None:
                        i["team2"] = player
                        i["team2_confirm"] = True
                        i["timestamp"] = datetime.datetime.now().timestamp()
                        chooseFrozen = True
        if chooseFrozen:
            f = open("matchpairings.json", "w")
            json.dump(pairings, f, indent=4)
            f.close()
    except:
        print("")
    return chooseFrozen


def insertGameLog(details: dict) -> None:
    """ Adds a game into the match pairings """

    try:
        with open("matchpairings.json", 'r') as matchpairings:
            pairings = json.load(matchpairings)
            pairings.append(details)
    except:
        pairings = [details]
    finally:
        pairing_file = open("matchpairings.json", "w")
        json.dump(pairings, pairing_file, indent=4)
        pairing_file.close()

setup_match()
