from math import ceil
from clas.team import Team
from modules import scorecard
from modules.commentary import scoreRun
from modules.scoreinput import playBall
from modules.batterchoice import batterChoice
from modules.bowlerchoice import fieldChoice


class Innings:
    """
    A class which plays the innings.

    Only new innings are created.
    The keyword arguments are self-explanatory.
    """

    # The batting team
    batting_team = None

    # The bowling team
    bowling_team = None

    # Test declaration
    # Applicable only for test cricket matches
    # True: test is declared, end of innings
    is_declared = False

    # Check if the innings is completed or not
    completed = False

    # Check if any team is chasing a target
    chasing = False

    # The target, if applicable
    target = 0

    # Innings data, as a dictionary (associated array)
    data = None

    # Name of the bowler
    bowler = None

    # Name of the bowler who bowled the previous over
    previousbowler = None

    # Batter on strike
    firstbatter = None

    # Batter at the non-striker's end
    secondbatter = None

    # Current over - 1
    # Since list indices start at 0
    over = 0

    # Current ball - 1
    # Since list indices start at 0
    ball = 0

    # Maximum number of overs, if applicable
    max_overs = 20

    # Maximum number of wickets
    # Default: 10
    max_wickets = 10

    # Addition to the batting team's score at every ball
    # Used to check if a bowler bowled a maiden over
    over_score = []

    # The outcome of every ball
    over_outcomes = []

    # List of remaining batters
    batter_list = None

    # List of remaining bowlers
    bowler_list = None

    # Is the game a test match?
    # True: test match
    # False: limited-overs match
    test = False

    def __init__(
        self,
        batting_team: str,
        bowling_team: str,
        test: bool,
        data: dict,
        max_overs=20,
        max_wickets=10,
        chasing=False,
        target=0
    ) -> None:
        self.batting_team = Team(batting_team)
        self.bowling_team = Team(bowling_team)
        self.data = data
        self.test = test
        self.chasing = chasing
        self.target = target
        self.max_overs = max_overs
        self.max_wickets = max_wickets
        self.batter_list = self.batting_team.members
        self.bowler_list = self.bowling_team.members
        self.batting_team = Team(batting_team)
        self.bowling_team = Team(bowling_team)
        self.data["battingteam"] = self.batting_team.name
        self.data["bowlingteam"] = self.bowling_team.name
        self.data["batter_stats"] = {}
        self.data["bowler_stats"] = {}
        for i in self.batting_team.members:
            self.data["batter_stats"][i] = (
                self.new_batter_stats()
            )
        for i in self.bowling_team.members:
            self.data["bowler_stats"][i] = (
                self.new_bowler_stats()
            )
        self.new_game()

    def new_game(self) -> None:
        self.firstbatter = batterChoice(
            batter_list=self.batter_list,
            non_striker="",
            is_batter_human=self.batting_team.is_human
        )
        self.secondbatter = batterChoice(
            batter_list=self.batter_list,
            non_striker=self.firstbatter,
            is_batter_human=self.batting_team.is_human
        )
        while self.is_playing():
            self.play_over()

    def conclude(self) -> None:
        self.completed = True
        scorecard.scoreCard(
            batters_list=self.data["batter_stats"],
            bowlers_list=self.data["bowler_stats"],
            team1_players=self.batting_team.members,
            team2_players=self.bowling_team.members,
            innings=1
        )

    def is_playing(self) -> bool:
        return (not self.completed)

    def check_overs(self) -> None:
        if not self.test:
            if self.over == self.max_overs:
                self.conclude()

    def check_wickets(self) -> None:
        if self.data["wickets_lost"] == self.max_wickets:
            self.conclude()

    def check_chased(self) -> None:
        if self.chasing and self.data["score"] >= self.target:
            self.conclude()

    def new_batter_stats(self) -> dict:
        return {
            "runs": 0,
            "balls": 0,
            "fours": 0,
            "sixes": 0,
            "dismissed": False,
            "dismissal": "Not out"
        }

    def record_outcome(self, outcome: str) -> dict:
        return {
            "bowler": self.bowler,
            "batter": self.firstbatter,
            "nonstriker": self.secondbatter,
            "over": self.over + 1,
            "ball": self.ball + 1,
            "result": outcome
        }

    def new_bowler_stats(self) -> dict:
        return {
            "overs": 0,
            "maidens": 0,
            "runs": 0,
            "wickets": 0
        }

    def commit(self):
        # saveGame(self.data)
        return self.data

    def play_over(self):
        if self.is_playing():
            if self.previousbowler is not None:
                self.previousbowler = self.bowler
                self.bowler_list.pop(
                    self.bowler_list.index(self.previousbowler)
                )
            for i in range(len(self.bowler_list) - 1, -1, -1):
                if self.is_bowler_exhausted(self.bowler_list[i]):
                    self.bowler_list.pop(i)
            self.bowler = fieldChoice(
                bowlers_array=self.bowler_list,
                is_bowler_human=self.bowling_team.is_human
            )
            for i in range(6):
                if not self.completed:
                    self.play_ball()
            if self.over_score == [0, 0, 0, 0, 0, 0]:
                self.data["bowler_stats"][self.bowler]["maidens"] += 1
            self.record_over()
            self.over_outcomes.clear()
            self.over_score.clear()
            self.rotate_strike()

    def play_ball(self):
        print("Ball", self.ball + 1)
        if self.chasing:
            balls_left = (6 * (self.max_overs - self.over)) - self.ball
            target_required_string = (
                "Need "
                + str(self.target - self.data["score"])
                + " runs to win"
            )
            if not self.test:
                target_required_string += (
                    " off "
                    + str(balls_left)
                    + " balls"
                )
            print(target_required_string)
        # outcome: 0, 1, 2, 3, 4, 5, 6, W, Declared
        outcome = playBall(
            bowler=self.bowler,
            batter=self.firstbatter,
            is_declare_permitted=self.test,
            bowler_human=self.bowling_team.is_human,
            batter_human=self.batting_team.is_human
        )
        if outcome == "Declared":
            self.completed = True
        else:
            scoreRun(outcome, self.bowler, self.firstbatter)
            self.over_outcomes.append(outcome)
            if outcome == "W":
                self.wicket()
            else:
                run = int(outcome)
                self.score_run(run)
            self.data["data"].append(
                self.record_outcome(outcome)
            )
            self.check_overs()
            if self.chasing:
                self.check_chased()

    def wicket(self):
        self.data["bowler_stats"][self.bowler]["overs"] = (
            self.record_increment_ball(
                self.data["bowler_stats"][self.bowler]["overs"]
            )
        )
        self.data["batter_stats"][self.firstbatter]["balls"] += 1
        self.data["batter_stats"][self.firstbatter]["dismissed"] = True
        self.data["bowler_stats"][self.bowler]["wickets"] += 1
        self.over_score.append(0)
        self.data["wickets_lost"] += 1
        self.check_wickets()
        if self.is_playing():
            self.firstbatter = batterChoice(
                batter_list=self.batter_list,
                non_striker=self.secondbatter,
                is_batter_human=self.batting_team.is_human
            )
        self.next_ball()

    def score_run(self, run: int) -> None:
        self.over_score.append(run)
        self.data["score"] += run
        self.data["batter_stats"][self.firstbatter]["runs"] += run
        self.data["batter_stats"][self.firstbatter]["balls"] += 1
        self.data["bowler_stats"][self.bowler]["runs"] += run
        if run == 4:
            self.data["batter_stats"][self.firstbatter]["fours"] += 1
        if run == 6:
            self.data["batter_stats"][self.firstbatter]["sixes"] += 1
        if run % 2 == 1:
            self.rotate_strike()
        self.data["bowler_stats"][self.bowler]["overs"] = (
            self.record_increment_ball(
                self.data["bowler_stats"][self.bowler]["overs"]
            )
        )
        self.next_ball()

    def rotate_strike(self):
        swapping = self.firstbatter
        self.firstbatter = self.secondbatter
        self.secondbatter = swapping

    def record_ball(self) -> float:
        return float(str(self.over) + "." + str(self.ball))

    def next_ball(self) -> None:
        self.ball += 1
        if (self.ball == 6):
            self.over += 1
            self.ball = 0

    def record_increment_ball(self, over):
        l = list(str(over))
        if len(l) == 1:
            l.append(".")
            l.append("0")
        local_over = int(l[0])
        local_ball = int(l[2])
        if (local_ball == 5):
            local_over += 1
            local_ball = 0
        else:
            local_ball += 1
        return float(str(local_over) + "." + str(local_ball))

    def is_bowler_exhausted(self, bowler: str) -> bool:
        if self.test:
            return False
        current = self.data["bowler_stats"][bowler]["overs"]
        if current < ceil(self.max_overs / 5):
            return False
        else:
            return True

    def record_over(self):
        print("This over:", self.over_outcomes)
        print("Batting:")
        batter1_stats_string = (
            str(self.firstbatter)
            + " : "
            + str(self.data["batter_stats"][self.firstbatter]["runs"])
        )
        if not self.data["batter_stats"][self.firstbatter]["dismissed"]:
            batter1_stats_string += "*"
        batter1_stats_string += (
            " ("
            + str(self.data["batter_stats"][self.firstbatter]["balls"])
            + ")"
        )
        print(batter1_stats_string)
        batter2_stats_string = (
            str(self.secondbatter)
            + " : "
            + str(self.data["batter_stats"][self.secondbatter]["runs"])
        )
        if not self.data["batter_stats"][self.secondbatter]["dismissed"]:
            batter2_stats_string += "*"
        batter2_stats_string += (
            " ("
            + str(self.data["batter_stats"][self.secondbatter]["balls"])
            + ")"
        )
        print(batter2_stats_string)
        print("Bowling:")
        bowler_stats_string = (
            str(self.bowler)
            + ": "
            + str(self.data["bowler_stats"][self.bowler]["overs"])
            + " - "
            + str(self.data["bowler_stats"][self.bowler]["maidens"])
            + " - "
            + str(self.data["bowler_stats"][self.bowler]["runs"])
            + " - "
            + str(self.data["bowler_stats"][self.bowler]["wickets"])
        )
        print(bowler_stats_string)
        print("Score: ", self.data["score"], "/", self.data["wickets_lost"])
