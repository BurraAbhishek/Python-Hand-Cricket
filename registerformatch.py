import ast

# Teams are identified by team name.
teamname = input("Team name: ")
team_data_filename = "team" + teamname + ".txt"

# Check if the team file exists
try:
    # Open the team file
    team_data_file = open(team_data_filename, 'r')
    # Read its contents and store the string in variable 's'
    s = team_data_file.read()
    team_data_file.close()
    # Parse the team data
    team_data = ast.literal_eval(s)
    team_key = input("Enter your team key: ")
    # Check if the key matches.
    if team_key == team_data[14]:
        team_data.pop(14)
        # team1.txt contains the details of the team playing with the computer
        # Copy all contents except the password from the original team file.
        # While playing, the list of players is obtained from team1.txt
        g = open("team1.txt", 'w')
        g.write(str(team_data))
        g.close()
        # The team will play against the computer.
        print("Team",teamname,"is now ready to play a match!")
        # Get user password.
        match_key = input("Enter your password: ")
        # This password is currently stored in plaintext.
        # In a future release, passwords will be hashed and then stored.
        h = open("game_pass.txt",'w')
        h.write(match_key)
        h.close()
        print("Your password is",match_key)
        confirm_read = input("Press 'Enter' key to complete this process.")
    else:
        print("Looks like you forgot your key. Contact support for key reset.")
        assume_forgotten = input()

# If team file doesn't exist, we can't setup the match.
except:
    print("Team",teamname,"is not available. Please set up your team before proceeding.")
    confirm_unavailable = input()
