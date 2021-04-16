import json
import ast
import hashlib


def team_setup_convert():
    """ Update the game data from plaintext format to JSON format """

    print("This module converts the old team plaintext data to JSON data")
    teamname = input("Team name: ")
    # Name of the text file where the team data will be saved.
    input_name = "team" + teamname + ".txt"
    output_name = "team" + teamname + ".json"
    try:
        # Check if the team already exists.
        f = open(input_name, 'r')
        s = f.read()
        f.close()
        input_data = ast.literal_eval(s)
        team_member_names = []
        # Get all 11 player names
        for i in range(1, 12):
            team_member_input_message = "Player ID " + str(i) + ": "
            team_member = input_data[i]
            # Team members must have a name; they can't be blank.
            while(len(team_member) < 1):
                team_member_input_message = "Player ID " + str(i) + ": "
                team_member = "Player" + str(i)
            team_member_names.append(team_member)
        # Number of games played: Initialized to 0
        games_played = input_data[12]
        # Number of games won: Initialized to 0
        games_won = input_data[13]
        # Ask the user for the team passcode
        team_pass_uinput = input_data[14]
        sha3_object = hashlib.sha3_256(team_pass_uinput.encode('UTF-8'))
        team_pass = sha3_object.hexdigest()
        # Prepare the JSON object.
        team_data_json = {
            "team_name": teamname,
            "team_members": team_member_names,
            "games_played": games_played,
            "games_won": games_won,
            "team_key": team_pass
            }
        print("Team registration in progress...")
        team_file = open(output_name, 'w')
        json.dump(team_data_json, team_file, indent=4)
        team_file.close()
        # NOTE: It is recommended that you save a copy of this file
        # elsewhere to avoid data loss due to accidental deletions.
        print("Conversion completed")
    except:
        print("Team file does not exist!")

team_setup_convert()
