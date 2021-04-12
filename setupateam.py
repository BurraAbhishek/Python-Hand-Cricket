import random
import string
import time

# Function to generate a random string


def rand_pass(size):
    """ Generate a random string containing uppercase, lowercase and digits.

    Usage:
    rand_pass(int)

    Arguments:
    size (int): Required. The number of characters of the string generated.
        This number should be greater than zero.

    Returns:
    string: The generated string.

    Example:
    rand_pass(10)
    Returns 'y2YGd7TSph'

    """

    generate_pass = ''.join([random.choice(string.ascii_uppercase 
    + string.ascii_lowercase + string.digits) for n in range(size)])
    return generate_pass


def team_setup():
    """ Creates a new text file containing all the team details

    Usage:
    team_setup()

    Arguments: None.

    Returns:
    A text file containing all the team details, saved in the same directory.

    Working:
    During runtime, the following inputs are required:
        Team name: (String) Name of the team
        Name of each players: (String) Name of each player sequentially.
    The team details is an array. The array contains the following elements:
        array[0]: Team name
        array[1] to array[11]: Names of all the 11 team members
        array[12]: Number of games played
        array[13]: Number of games won
        array[14]: Team passcode, stored in plaintext format.

    """

    # Generate a random password for this team.
    n = random.randint(8, 12)
    team_pass = rand_pass(n)

    # Main program.
    print("Welcome to Python based hand cricket")
    print("NOTE: Team names '1', 'Computer' and 'CPU' are system reserved. \
Hence, they are not allowed.")
    teamname = input("Team name: ")
    reserved_names = ["1", "CPU", "Computer", ""]
    if teamname in reserved_names:
        perror_sysreserved = input("System reserved, \
can't give you chosen team. Hit enter, and then try again.")
    else:
        # Name of the text file where the team data will be saved.
        file_name = "team" + teamname + ".txt"
        try:
            # Check if the team already exists.
            f = open(file_name, 'r')
            f.close()
            perror_duplicateteamname = input("Team name exists already, \
hence can't give you same team. Hit enter, and then try again.")
        except:
            team_data = [teamname]
            # Get all 11 player names
            for i in range(1, 12):
                team_member_input_message = "Player ID " + str(i) + ": "
                team_member = input(team_member_input_message)
                # Team members must have a name; they can't be blank.
                while(len(team_member) < 1):
                    team_member_input_message = "Player ID " + str(i) + ": "
                    team_member = input(team_member_input_message)
                team_data.append(team_member)
            # Number of games played: Initialized to 0
            team_data.append(0)
            # Number of games won: Initialized to 0
            team_data.append(0)
            # Team passcode. 
            team_data.append(team_pass)
            # Encode the array into a string. 
            # Then, save it in a text file such that:
            # The file name contains the name of the team.
            s = str(team_data)
            print("Team registration in progress...")

            f = open(file_name, 'w')
            f.write(s)
            f.close()
            # NOTE: It is recommended that you save a copy of this file
            # elsewhere to avoid data loss due to accidental deletions.
            # NOTE: Passwords are currently stored in plaintext. 
            # In a future release, passwords will be hashed and then stored.

            print("Registered. Open Match registration file to play match")
            print("ATTENTION! Your team key is ", team_pass, " .\
Keep it safe because you need it every time you register for a match")
            success_notification = input()

team_setup()
