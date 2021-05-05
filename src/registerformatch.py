import json
import os
from modules import hashfunc


def setup_match():
    """ Setup a game between two teams.

    Arguments: None

    While running the function, the team file is read from the 'teams' folder.

    Returns:
    A JSON file (team1.json or team2.json) in the current directory.
    This file is a copy of the team file,
    except that the passwords may not match.

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
            # Get user password.
            match_key = input("Enter your password: ")
            match_hash = hashfunc.hash_password(match_key)
            # If opponent is computer, load the computer team as opponent.
            if(opponent_choice != 'human'):
                with open('ai_opponent/teamComputer.json', 'r') as team2:
                    ai_opponent_json = json.load(team2)
                    ai_team2_data = {
                        "team_name": ai_opponent_json["team_name"],
                        "team_members": ai_opponent_json["team_members"],
                        "games_played": ai_opponent_json["games_played"],
                        "games_won": ai_opponent_json["games_won"],
                        "password": match_hash
                        }
                match_team2_file = open("team2.json", 'w')
                json.dump(ai_team2_data, match_team2_file, indent=4)
                match_team2_file.close()
            # Convert the JSON into text file
            team_data = {
                    "team_name": team_data_json["team_name"],
                    "team_members": team_data_json["team_members"],
                    "games_played": team_data_json["games_played"],
                    "games_won": team_data_json["games_won"],
                    "password": match_hash
                    }
            # team1.json contains details of the team running this module.
            # If team1.json exists, then it's team2.json
            # Copy all contents except the password from the original team file
            # While playing, the list of players is obtained from the JSON file
            if(opponent_choice == "human"):
                try:
                    try:
                        # Team1 and Team2 set, remove Team2 and assign Team1
                        test_file_if_engine = open("team2.json", "r")
                        test_file_if_engine.close()
                        os.remove("team2.json")
                        match_team_file = open("team1.json", "w")
                    except:
                        try:
                            # Team1 waits for opponent, Team2: Your team
                            with open("team1.json", 'r') as match_team_file1:
                                team1_opponent = json.load(match_team_file1)
                                team1_teamname = team1_opponent["team_name"]
                                print("Your opponent is", team1_teamname)
                                match_team_file = open("team2.json", 'w')
                        except:
                            # Team1: Your team. Wait for Team2
                            match_team_file = open("team1.json", 'w')
                except:
                    match_team_file = open("team1.json", 'w')
            else:
                # Team1: Your team, Team2: Computer
                print("Your opponent is Computer")
                match_team_file = open("team1.json", 'w')
            json.dump(team_data, match_team_file, indent=4)
            match_team_file.close()
            confirm_read = input("Press 'Enter' key to complete this process.")
        else:
            print("The keys did not match.")
            print("Forgot your key? Contact support for key reset.")
            assume_forgotten = input()

    # If team file doesn't exist, we can't setup the match.
    except:
        print("Team", teamname, "is not available. \
    Please set up your team before proceeding.")
        confirm_unavailable = input()

setup_match()
