class TeamNotFoundError(FileNotFoundError):
    """ The team was not registered """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TeamAlreadyExistsError(FileExistsError):
    """ This team name is already in use """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PlayAgainstSelfError(PermissionError):
    """ You are not allowed to play against yourself! """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AccessDenied(PermissionError):
    """ You are not authorized to do this """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IncorrectMatchType(TypeError):
    """ You requested for some other match settings """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
