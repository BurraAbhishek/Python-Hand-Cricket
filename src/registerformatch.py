import json
from modules import hashfunc

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
        # The team will play against the computer.
        print("Team", teamname, "is now ready to play a match!")
        # Get user password.
        match_key = input("Enter your password: ")
        match_hash = hashfunc.hash_password(match_key)
        # Convert the JSON into text file
        team_data = {
                "team_name": team_data_json["team_name"],
                "team_members": team_data_json["team_members"],
                "games_played": team_data_json["games_played"],
                "games_won": team_data_json["games_won"],
                "password": match_hash
                }
        # team1.json contains the details of the team playing with the computer
        # Copy all contents except the password from the original team file.
        # While playing, the list of players is obtained from team1.json
        match_team_file = open("team1.json", 'w')
        json.dump(team_data, match_team_file, indent=4)
        match_team_file.close()
        confirm_read = input("Press 'Enter' key to complete this process.")
    else:
        print("Looks like you forgot your key. Contact support for key reset.")
        assume_forgotten = input()

# If team file doesn't exist, we can't setup the match.
except:
    print("Team", teamname, "is not available. \
Please set up your team before proceeding.")
    confirm_unavailable = input()
