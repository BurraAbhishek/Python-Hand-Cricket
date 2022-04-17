from clas.team import Team


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
    Team()

team_setup()
