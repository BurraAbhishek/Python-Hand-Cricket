from modules import toss
from modules.followon import checkFollowOn
from modules.savegamedata import saveGame, saveGameToID

from clas.team import Team
from clas.innings import Innings
from clas.pairing import Pairing
from clas.exception import IncorrectMatchType


class Game:
    """
    A class which handles all the games played here.

    To create a new game, simply call

        Game()

    To create a game with pre-defined parameters, call

        Game(new=False)

    Games called with new=False must be programmed; see the code in
    result() member function which calls the super over game.
    """

    # The batting team. Class: Team
    team1 = None

    # The fielding team. Class: Team
    team2 = None

    # The pairing, as a dictionary (associated array)
    pairing = None

    # Is the game a test match (true) or limited-overs match (false)
    test = False

    # The game data, as a dictionary
    data = None

    # The toss chosen, either 'bat' or 'field'
    toss_chosen = None

    # The game ID. 
    # For super over games, these are generated while saving the game.
    gameid = None

    # Is the game a super-over tiebreaker game or not
    super_over = False

    def __init__(self, new=True) -> None:
        if new:
            self.pairing = Pairing(exists=True)
            self.go()
            self.result()
            self.conclude()
            pass

    def verify_mode(self, test):
        if self.pairing.test == test:
            self.test = test
        else:
            raise IncorrectMatchType("Incorrect match type")

    def set_new_innings_data(self, innings: int) -> dict:
        d = {
            "battingteam": "Waiting for toss",
            "bowlingteam": "Waiting for toss",
            "innings": innings,
            "score": 0,
            "wickets_lost": 0,
            "data": [],
            "batter_stats": [],
            "bowler_stats": []
        }
        return d

    def set_game_data(
        self,
        wickets=10,
        overs=20,
        followon=200,
        isfollowon=False
    ) -> None:
        if self.test:
            game_data = {
                "isTest": True,
                "FollowOnScore": followon,
                "isFollowOn": isfollowon,
                "wickets": wickets,
                "innings_data": {
                    "team1_innings1_data": self.set_new_innings_data(1),
                    "team2_innings1_data": self.set_new_innings_data(1),
                    "team1_innings2_data": self.set_new_innings_data(2),
                    "team2_innings2_data": self.set_new_innings_data(2)
                    }
                }
        else:
            game_data = {
                "isTest": False,
                "overs": overs,
                "wickets": wickets,
                "innings_data": {
                    "innings1_data": self.set_new_innings_data(1),
                    "innings2_data": self.set_new_innings_data(2)
                    }
                }
        self.data = game_data

    def get_stats_by_prompt(self):
        try:
            print(
                "By default, this is a 10-wickets match,"
                + "unless specified otherwise"
            )
            wickets_choice = int(input("How many wickets for each team? "))
        except:
            wickets_choice = 10
        if wickets_choice < 1 or wickets_choice > 10:
            wickets_choice = 10
        print("Total:", wickets_choice, "wickets game")
        if self.test:
            try:
                print("By default, a follow-on requires at least 200 runs.")
                print("The minimum limit for this is at least 75 runs.")
                followon_choice = int(
                    input("Minimum runs required for follow-on: ")
                )
            except:
                followon_choice = 200
            if followon_choice < 75:
                followon_choice = 200
            followon_minscore_notify = ("For follow-on to be permitted, "
                                        + "the team batting first should score"
                                        + " at least "
                                        + str(followon_choice)
                                        + " runs more than the "
                                        + "team fielding first.")
            print(followon_minscore_notify)
            return wickets_choice, followon_choice
        else:
            try:
                print(
                    "By default, the match is a T20, unless otherwise chosen."
                )
                overs_choice = int(input("Number of overs: "))
            except:
                overs_choice = 20
            if overs_choice < 1:
                overs_choice = 20
            print("This is a", overs_choice, "overs match.")
            return wickets_choice, overs_choice

    def get_innings_data(self, index: int) -> dict:
        if self.test:
            if index == 0:
                return self.data["innings_data"]["team1_innings1_data"]
            elif index == 1:
                return self.data["innings_data"]["team2_innings1_data"]
            elif index == 2:
                return self.data["innings_data"]["team1_innings2_data"]
            elif index == 3:
                return self.data["innings_data"]["team2_innings2_data"]
        else:
            if index == 0:
                return self.data["innings_data"]["innings1_data"]
            elif index == 1:
                return self.data["innings_data"]["innings2_data"]

    def set_innings_data(self, index: int, data: dict) -> None:
        if self.test:
            if index == 0:
                self.data["innings_data"]["team1_innings1_data"] = data
            elif index == 1:
                self.data["innings_data"]["team2_innings1_data"] = data
            elif index == 2:
                self.data["innings_data"]["team1_innings2_data"] = data
            elif index == 3:
                self.data["innings_data"]["team2_innings2_data"] = data
        else:
            if index == 0:
                self.data["innings_data"]["innings1_data"] = data
            elif index == 1:
                self.data["innings_data"]["innings2_data"] = data

    def play_innings(self, index, chasing=False, target=0):
        if index % 2 == 0:
            batting_team = self.team1.name
            bowling_team = self.team2.name
        else:
            batting_team = self.team2.name
            bowling_team = self.team1.name
        if self.test:
            innings = Innings(
                batting_team=batting_team,
                bowling_team=bowling_team,
                test=True,
                data=self.get_innings_data(index),
                max_wickets=self.data["wickets"],
                chasing=chasing,
                target=target
            )
        else:
            innings = Innings(
                batting_team=batting_team,
                bowling_team=bowling_team,
                test=False,
                data=self.get_innings_data(index),
                max_overs=self.data["overs"],
                max_wickets=self.data["wickets"],
                chasing=chasing,
                target=target
            )
        self.set_innings_data(
            index,
            innings.commit()
        )

    def result(self):
        if self.test:
            team1_data = (self.get_innings_data(0))["score"]
            team1_data += (self.get_innings_data(2))["score"]
            team2_data = (self.get_innings_data(1))["score"]
            team2_data += (self.get_innings_data(3))["score"]
            if team1_data > team2_data:
                self.team1.set_result(1)
                self.team2.set_result(-1)
            elif team1_data < team2_data:
                self.team1.set_result(-1)
                self.team2.set_result(1)
            else:
                self.team1.set_result(0)
                self.team2.set_result(0)
        else:
            team1_data = self.get_innings_data(0)
            team2_data = self.get_innings_data(1)
            if team1_data["score"] > team2_data["score"]:
                self.team1.set_result(1)
                self.team2.set_result(-1)
                margin = team1_data["score"] - team2_data["score"]
                if self.super_over:
                    print(self.team1.name, "wins by super over")
                else:
                    if margin == 1:
                        print(self.team1.name, "wins by 1 run")
                    else:
                        print(self.team1.name, "wins by", margin, "runs")
                if self.team1.is_human and not self.team2.is_human:
                    self.result_message(1)
                    self.team1.show_summary()
                elif self.team2.is_human and not self.team1.is_human:
                    self.result_message(-1)
                    self.team2.show_summary()
            elif team1_data["score"] < team2_data["score"]:
                self.team1.set_result(-1)
                self.team2.set_result(1)
                wl = (self.get_innings_data(1))["wickets_lost"]
                margin = self.data["wickets"] - wl
                if self.super_over:
                    print(self.team2.name, "wins by super over")
                else:
                    if margin == 1:
                        print(self.team2.name, "wins by 1 wicket")
                    else:
                        print(self.team2.name, "wins by", margin, "wickets")
                if self.team1.is_human and not self.team2.is_human:
                    self.result_message(-1)
                    self.team1.show_summary()
                elif self.team2.is_human and not self.team1.is_human:
                    self.result_message(1)
                    self.team2.show_summary()
            else:
                # Super over
                g = Game(new=False)
                g.team1 = self.team2
                g.team2 = self.team1
                g.super_over = True
                g.set_game_data(wickets=2, overs=1)
                g.play()
                g.result()
                g.team1.commit()
                g.team2.commit()
                saveGame(g.data)
                pass

    def result_message(self, result: int) -> None:
        if result == 1:
            print("Congratulations, you won!")
        elif result == -1:
            print("Sorry, you lost this game. Better luck next time.")

    def play(self):
        if self.test:
            self.play_test()
        else:
            self.play_innings(0)
            scoredata = self.get_innings_data(0)
            target = scoredata["score"] + 1
            self.play_innings(1, chasing=True, target=target)

    def play_test(self):
        if self.test:
            self.play_innings(0)
            self.play_innings(1)
            d0 = self.get_innings_data(0)
            d1 = self.get_innings_data(1)
            if (d0["score"] - d1["score"]) >= self.data["FollowOnScore"]:
                if checkFollowOn(self.team1.is_human):
                    self.data["isFollowOn"] = True
            if self.data["isFollowOn"]:
                self.play_innings(3)
                d3 = self.get_innings_data(3)
                if (d1["score"] + d3["score"] >= d0["score"]):
                    # Chasing
                    target = d1["score"] + d3["score"] + 1 - d0["score"]
                    self.play_innings(2, chasing=True, target=target)
            else:
                self.play_innings(2)
                d2 = self.get_innings_data(2)
                if (d0["score"] + d2["score"] >= d1["score"]):
                    # Chasing
                    target = d0["score"] + d2["score"] + 1 - d1["score"]
                    self.play_innings(3, chasing=True, target=target)
        else:
            self.play()

    def go(self):
        matchID = input("Enter the match ID: ")
        p = Pairing(exists=True)
        self.pairing = p.find_pairing_by_id(id=matchID, remove=False)
        self.gameid = matchID
        self.test = self.pairing["test"]
        arg1, arg2 = self.get_stats_by_prompt()
        if self.test:
            self.set_game_data(wickets=arg1, followon=arg2)
        else:
            self.set_game_data(wickets=arg1, overs=arg2)
        self.team1 = Team(self.pairing["team1"])
        self.team2 = Team(self.pairing["team2"])
        self.toss_chosen = toss.tossPlay(
            team1_data=self.team1,
            team2_data=self.team2
        )
        if self.toss_chosen == "field":
            team_swap = self.team1
            self.team1 = self.team2
            self.team2 = team_swap
        self.play()

    def conclude(self):
        self.team1.commit()
        self.team2.commit()
        saveGameToID(self.data, self.gameid)
