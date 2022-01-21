import json
from modules import hashfunc


def team_setup() -> None:
    """ Creates a new JSON file containing all the team details

    Usage:
    team_setup()

    Arguments: None.

    Returns:
    None.
    A JSON file containing all the team details
    is saved in the 'teams' directory

    Working:
    During runtime, the following inputs are required:
        Team name: (String) Name of the team
        Name of each players: (String) Name of each player sequentially.

    """

    print("Welcome to Python based hand cricket")
    print("NOTE: Team names 'Computer' and 'CPU' are system reserved. \
Hence, they are not allowed.")
    teamname = input("Team name: ")
    # These team names are not permitted because they are reserved.
    reserved_names = ["CPU", "Computer", ""]
    if teamname in reserved_names:
        perror_sysreserved = input("System reserved, \
can't give you chosen team. Hit 'Enter', and then try again.")
    else:
        # Name of the text file where the team data will be saved.
        file_name = "teams/team" + teamname + ".json"
        try:
            # Check if the team already exists.
            f = open(file_name, 'r')
            f.close()
            perror_duplicateteamname = input("Team name exists already, \
hence can't give you same team. Hit 'Enter', and then try again.")
        except:
            team_member_names = []
            # Get all 11 player names
            for i in range(1, 12):
                team_member_input_message = "Player ID " + str(i) + ": "
                team_member = input(team_member_input_message)
                # Team members must have a name; they can't be blank.
                while(len(team_member) < 1):
                    team_member_input_message = "Player ID " + str(i) + ": "
                    team_member = input(team_member_input_message)
                team_member_names.append(team_member)
            # Ask the user for the team passcode
            team_pass_uinput = input("Enter your team password: ")
            team_pass = hashfunc.hash_password(team_pass_uinput)
            # Prepare the JSON object.
            team_data_json = {
                "team_name": teamname,
                "team_members": team_member_names,
                "games_played": 0,
                "games_won": 0,
                "games_lost": 0,
                "tests_tied": 0,
                "team_key": team_pass,
                "online": True,
                "hasSuperOver": False,
                "tosViolation": False,
                "isHuman": True
                }
            print("Team registration in progress...")
            team_file = open(file_name, 'w')
            json.dump(team_data_json, team_file, indent=4)
            team_file.close()
            # NOTE: It is recommended that you save a copy of this file
            # elsewhere to avoid data loss due to accidental deletions.
            print("Your team,", teamname, ", was successfully registered.")
            print("Open the Match registration module to play a match.")
            print("It's a good idea to close this module for security reasons")
            print("Hit 'Enter' to continue")
            _ = input()

team_setup()
