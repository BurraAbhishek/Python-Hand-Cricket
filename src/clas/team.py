import json
from modules import hashfunc
from clas.exception import TeamNotFoundError, TeamAlreadyExistsError


class Team:
    """
    A class which handles all team operations throughout this game.

    To create a new team, use:

        Team()

    To retrieve an existing team called "test" (for example), use:

        Team(name="test")

    """

    # The name of the team
    name = None

    # The list of all team members
    members = []

    # The number of games played by the team
    games_played = 0

    # The number of games won by the team
    games_won = 0

    # The number of games lost by the team
    games_lost = 0

    # The number of test cricket matches tied by the team
    tests_tied = 0

    # The team key hash
    team_key = ""

    # Status of the team:
    # online: True
    # offline: False
    online = True

    # Check if the team has an ongoing super over
    has_super_over = False

    # Check if the team broke the rules
    tos_violation = False

    # Check if the team has all human players
    is_human = True

    # Store the result of an ongoing game
    gameresult = 0

    # List of prohibited team and member names
    __blacklist = [
            "cpu",
            "cpu0",
            "cpu1",
            "cpu2",
            "cpu3",
            "cpu4",
            "cpu5",
            "cpu6",
            "cpu7",
            "cpu8",
            "cpu9",
            "cpu10",
            "cpu11",
            "computer"
        ]

    def __init__(self, name=None) -> None:
        if name is None:
            # Create a new team
            self.set_team_name()
            self.set_team_members()
            self.set_team_pass()
            self.commit()
            print("Your team,", self.name, ", was successfully registered.")
            print("Open the Match registration module to play a match.")
            print("It's a good idea to close this module for security reasons")
            print("Hit 'Enter' to continue")
            _ = input()
        else:
            # Load an existing team
            self.name = name
            if name.strip().lower() in self.__blacklist:
                self.is_human = False
            self.load()

    def load_team_filename(self) -> str:
        """ Return the location of the team data as a string """

        # Store human teams and bot teams separately
        if self.is_human:
            # Human team
            return ("teams/team" + str(self.name) + ".json")
        else:
            # Bot team
            return ("ai_opponent/team" + str(self.name) + ".json")

    def set_team_name(self, name=None) -> None:
        """ Sets the name of the team """

        # If the name is not passed, prompt the user
        if name is None:
            name = input("Team name: ")
        # The name must be a string
        if not isinstance(name, str):
            raise TypeError("Team name must be a string")
        # The name of the team should have at least
        # one non-blank character.
        if len(name.strip()) < 1:
            raise NameError(
                "The name of your team cannot be blank!"
            )
        # The name must not be prohibited.
        if name.strip().lower() in self.__blacklist:
            raise NameError(
                "This team name is reserved. Please try another one."
                )
        self.name = name
        # The team must be newly created
        if self.team_already_exists():
            raise TeamAlreadyExistsError(
                "This team name is already in use, please try another one."
            )

    def set_team_members(self) -> None:
        """ Set the list of team members """

        # Name of all 11 players
        for i in range(1, 12):
            team_member_input_message = "Player ID " + str(i) + ": "
            team_member = input(team_member_input_message)
            team_member_clean = team_member.strip().lower()
            # Fails: blank string as player name
            condition1 = bool(len(team_member_clean) < 1)
            # Fails: The name is prohibited
            condition2 = bool(team_member_clean in self.__blacklist)
            # Ask the user for another name if any of these two hold.
            while(condition1 or condition2):
                team_member_input_message = "Player ID " + str(i) + ": "
                team_member = input(team_member_input_message)
                team_member_clean = team_member.strip().lower()
                condition1 = bool(len(team_member_clean) < 1)
                condition2 = bool(team_member_clean in self.__blacklist)
            # Save the team member
            self.members.append(team_member)

    def team_already_exists(self) -> bool:
        """ Check if the team already exists or not """

        try:
            # Check if the file exists.
            # This means that the team was already chosen.
            team_name = self.load_team_filename()
            f = open(team_name, "r")
            f.close()
            return True
        except:
            return False

    def set_team_pass(self) -> None:
        """ Set the team key """

        team_pass_uinput = input("Enter your team password: ")
        # Hash the team key before storing it
        self.team_key = hashfunc.hash_password(team_pass_uinput)

    def verify_team_pass(self, upass=None) -> bool:
        """ Verify the team key """

        if upass is None:
            upass = input("Enter your team key: ")
        return hashfunc.verify_password(
            upass,
            self.team_key
        )

    def commit(self) -> None:
        """ Save the team details """

        if self.is_human:
            file_name = self.load_team_filename()
            team_file = open(file_name, 'w')
            team_data_json = {
                "team_name": self.name,
                "team_members": self.members,
                "games_played": self.games_played,
                "games_won": self.games_won,
                "games_lost": self.games_lost,
                "tests_tied": self.tests_tied,
                "team_key": self.team_key,
                "online": self.online,
                "hasSuperOver": self.has_super_over,
                "tosViolation": self.tos_violation,
                "isHuman": self.is_human
            }
            json.dump(team_data_json, team_file, indent=4)
            team_file.close()

    def load(self) -> None:
        """ Load the team details """

        file_name = self.load_team_filename()
        try:
            team_file = open(file_name, 'r')
            team_data = json.load(team_file)
            self.name = team_data["team_name"]
            self.members = team_data["team_members"]
            self.games_played = team_data["games_played"]
            self.games_won = team_data["games_won"]
            self.games_lost = team_data["games_lost"]
            self.tests_tied = team_data["tests_tied"]
            self.team_key = team_data["team_key"]
            self.online = team_data["online"]
            self.has_super_over = team_data["hasSuperOver"]
            self.tos_violation = team_data["tosViolation"]
            self.is_human = team_data["isHuman"]
        except:
            e = "Your team, "
            e += str(self.name)
            e += " was not found."
            e += "Please register before proceeding."
            raise TeamNotFoundError(e)

    def set_result(self, result: int) -> None:
        """ Set the result of a recently completed game """

        # A new game was played
        self.games_played += 1
        # If no rules infraction
        if not self.tos_violation:
            # Won
            if result == 1:
                self.games_won += 1
            # Lost
            elif result == -1:
                self.games_lost += 1
            # Tied test match
            elif result == 0:
                self.tests_tied += 1

    def show_summary(self) -> None:
        """ Shows the summary of the team's performance """

        print("")
        print("Team:", self.name)
        print("Games played: ", self.games_played)
        print("Games won:", self.games_won)
        if self.games_played == 0:
            win_p = 0
        else:
            win_p = round(((100 * self.games_won) / self.games_played), 2)
        print("Win percentage: " + str(win_p) + "%")
        print("")
