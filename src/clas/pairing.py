import json
import datetime
from modules import hashfunc
from modules import savegamedata
from clas.team import Team
from clas.exception import PlayAgainstSelfError, AccessDenied


class Pairing:
    """
    A class which handles all pairings throughout this game

    To create a new pairing, use:

        Pairing()

    To create a blank pairing, use:

        Pairing(exists=True)

    To create a pairing with a known team (for example: Test)
    programmatically, use:

        Pairing(exists=True, name="Test")

    Use Pairing() if you don't already know which team will participate.
    """

    team1 = None
    team1_human = True
    team1_confirm = False
    team2 = None
    team2_human = True
    team2_confirm = False
    gameid = ""
    gameid_confirm = False
    test = False
    timestamp = datetime.datetime.now().timestamp()

    def __init__(self, exists=False, name=None) -> None:
        # Use this if you want to remove
        # old and unused pairings
        # self.remove_unused_games()
        # Init code
        if exists:
            if name is not None:
                self.get_team_data(1, name)
        else:
            self.new_pairing()
            self.opponent_select()
            self.set_gameid()
            print("Your match is registered.")
            if not self.check_if_pairing_exists():
                self.insert_game_log()
                if self.gameid_confirm:
                    print("Your match ID is: ")
                    print(self.gameid_unhashed)
                    print("Share this match ID only with your opponent.")
                else:
                    print("Ask your opponent for the match ID")
            else:
                print("Ask your opponent for the match ID")
        pass

    def new_pairing(self) -> None:
        teamname = input("Team name: ")
        team = Team(teamname)
        team_key = input("Enter your team key: ")
        if team.verify_team_pass(team_key):
            self.team1 = team.name
            self.team1_human = team.is_human
            self.confirm(1)
        else:
            raise AccessDenied

    def get_filename(self) -> None:
        return "matchpairings.json"

    def set_gameid(self) -> None:
        self.gameid_confirm = True
        gameidfile = savegamedata.getUniqueSavefile()
        gameid = gameidfile[12:-5]
        self.gameid_unhashed = gameid
        self.gameid = hashfunc.hash_password(gameid)

    def get_team_data(self, position: int, name: str) -> None:
        team_data = Team(name=name)
        if position == 1:
            self.team1 = team_data.name
            self.team1_human = team_data.is_human
        elif position == 2:
            self.team2 = team_data.name
            self.team2_human = team_data.is_human

    def opponent_select(self):
        print("Team", str(self.team1), "is now ready to play a match!")
        # Determine if the opponent is a human or a computer.
        print('Do you want to play against a human team or computer team?')
        print("To play against a human team, type 'human' and hit 'Enter'")
        print("To play against the usual computer team, just hit 'Enter'.")
        opponent_choice = input()
        if (opponent_choice == 'human'):
            self.opponent_human()
        else:
            self.play_computer()

    def opponent_human(self):
        print("Do you want to choose your opponent (Y/N)")
        chooseopponentflag = input()
        if chooseopponentflag == 'Y':
            opponent = self.find_human_opponent_exists(player=self.team1)
            team = Team(name=opponent)
            self.team2 = team.name
            self.team2_human = team.is_human
        else:
            self.quick_pairing()

    def confirm(self, position: int) -> None:
        if position == 1:
            self.team1_confirm = True
        elif position == 2:
            self.team2_confirm = True

    def play_computer(self) -> None:
        self.team2 = "Computer"
        self.team2_human = False
        self.team2_confirm = True

    def validate(self) -> None:
        team1 = Team(name=self.team1)
        team2 = Team(name=self.team2)
        if (team1.tos_violation != team2.tos_violation):
            return False
        if not self.team1_confirm:
            return False
        if not self.team2_confirm:
            return False
        if self.check_if_pairing_exists():
            return False
        return True

    def check_if_pairing_exists(self) -> None:
        try:
            pairingfilename = self.get_filename()
            with open(pairingfilename, 'r') as matchpairings:
                pairings = json.load(matchpairings)
                for i in pairings:
                    c1 = (i["team1"] == self.team1)
                    c2 = (i["team1_human"] == self.team1_human)
                    c3 = (i["team2"] == self.team2)
                    c4 = (i["team2_human"] == self.team2_human)
                    c5 = (i["team1"] == self.team2)
                    c6 = (i["team1_human"] == self.team2_human)
                    c7 = (i["team2"] == self.team1)
                    c8 = (i["team2_human"] == self.team1_human)
                    c9 = (i["test"] == self.test)
                    if (c1 and c2 and c3 and c4 and c9):
                        return True
                    elif (c5 and c6 and c7 and c8 and c9):
                        return True
            return False
        except:
            return False

    def insert_game_log(self) -> None:
        pairingfilename = self.get_filename()
        pairing = {
            "team1": self.team1,
            "team1_human": self.team1_human,
            "team1_confirm": self.team1_confirm,
            "team2": self.team2,
            "team2_human": self.team2_human,
            "team2_confirm": self.team2_confirm,
            "gameid": self.gameid,
            "test": self.test,
            "timestamp": datetime.datetime.now().timestamp()
        }
        try:
            with open(pairingfilename, 'r') as matchpairings:
                pairings = json.load(matchpairings)
                pairings.append(pairing)
        except:
            pairings = [pairing]
        finally:
            pairing_file = open(pairingfilename, "w")
            json.dump(pairings, pairing_file, indent=4)
            pairing_file.close()

    def find_pairing_by_id(
        self,
        id,
        remove: bool=True
    ) -> dict:
        pairingfilename = self.get_filename()
        with open(pairingfilename, 'r') as matchpairings:
            pairings = json.load(matchpairings)
            for i in range(0, len(pairings)):
                if (hashfunc.verify_password(id, pairings[i]["gameid"])):
                    if remove:
                        pairings.pop(i)
                        f = open(pairingfilename, 'w')
                        json.dump(pairings, f, indent=4)
                        f.close()
                    return pairings[i]
        raise Exception("Pairing was not found!")

    def find_pairing_by_teams(
        self,
        team1: str,
        team2: str,
        test: bool,
        remove: bool=True
    ) -> dict:
        pairingfilename = self.get_filename()
        with open(pairingfilename, 'r') as matchpairings:
            pairings = json.load(matchpairings)
            for i in range(0, len(pairings)):
                c1 = (pairings[i]["team1"] == team1)
                c2 = (pairings[i]["team2"] == team2)
                c3 = (pairings[i]["test"] == test)
                if (c1 and c2 and c3):
                    if remove:
                        pairings.pop(i)
                        f = open(pairingfilename, 'w')
                        json.dump(pairings, f, indent=4)
                        f.close()
                    return pairings[i]
        raise Exception("Pairing is not found")

    def check_pairing_chosen(self, opponent: str) -> bool:
        """ Chooses a match among various pairings

        Arguments:
        opponent: str. The name of your opponent team.

        Returns:
        A boolean value which checks if the pairing is confirmed.

        """

        pairingfilename = self.get_filename()
        try:
            chooseFrozen = False
            with open(pairingfilename, 'r') as matchpairings:
                pairings = json.load(matchpairings)
                for i in pairings:
                    c1 = (i["team1"] == opponent)
                    c2 = (i["test"] == self.test)
                    c3 = (not chooseFrozen)
                    if c1 and c2 and c3:
                        if i["team2"] == self.team1:
                            i["team2_confirm"] = True
                            i["timestamp"] = (
                                datetime.datetime.now().timestamp()
                            )
                            chooseFrozen = True
                        elif i["team2"] is None:
                            i["team2"] = self.team1
                            i["team2_confirm"] = True
                            i["timestamp"] = (
                                datetime.datetime.now().timestamp()
                            )
                            chooseFrozen = True
            if chooseFrozen:
                f = open(pairingfilename, "w")
                json.dump(pairings, f, indent=4)
                f.close()
        except:
            raise AccessDenied
        return chooseFrozen

    def find_human_opponent_exists(self, player: str) -> str:
        """ Checks if an opponent team exists """

        opponent_teamname = input("Choose your opponent team by name: ")
        try:
            if player == opponent_teamname:
                raise PlayAgainstSelfError(
                    "Playing against yourself is strictly prohibited."
                )
            t = Team(opponent_teamname)
            if not t.team_already_exists():
                raise Exception("Test")
        except:
            print("Chosen team doesn't exist. ")
            opponent_teamname = self.find_human_opponent_exists(player)
        return opponent_teamname

    def quick_pairing(self):
        pairingfilename = self.get_filename()
        c4 = False
        with open(pairingfilename, 'r') as matchpairings:
            pairings = json.load(matchpairings)
        for i in range(0, len(pairings)):
            c1 = (pairings[i]["team1"] != self.team1)
            c2 = (pairings[i]["team2"] is None)
            c3 = (self.team2 is None)
            if c1 and c2 and c3:
                pairings[i]["team2"] = self.team1
                pairings[i]["team2_human"] = self.team1_human
                pairings[i]["team2_confirm"] = self.team1_confirm
                pairings[i]["gameid"] = self.gameid
                c4 = True
                print("Your opponent is", pairings[i]["team1"])
                break
        if c4:
            pairing_file = open(pairingfilename, 'w')
            json.dump(pairings, pairing_file, indent=4)
            pairing_file.close()

    def remove_unused_games(self) -> None:
        pairingfilename = self.get_filename()
        current_time = datetime.datetime.now().timestamp()
        # Number of days after which the pairing is removed if not played.
        days_remaining = 14
        try:
            with open(pairingfilename, 'r') as matchpairings:
                pairings = json.load(matchpairings)
                time_remaining = days_remaining * 86400000
                for i in range(len(pairings) - 1, 0, -1):
                    diff = current_time - pairings[i]["timestamp"]
                    if (diff) > time_remaining:
                        pairings.pop(i)
                    elif (0 - diff) > time_remaining:
                        pairings.pop(i)
                f = open(pairingfilename, 'w')
                json.dump(pairings, f, indent=4)
                f.close()
        except:
            pass
