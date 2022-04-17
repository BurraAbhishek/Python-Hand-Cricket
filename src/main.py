from clas import team, pairing, game
import help as h


def main():
    play = True
    while play:
        print("Welcome to Python-based Hand Cricket!")
        print("Choose any of the following:")
        print()
        print("Type 'register' to register a team.")
        print("Type 'pair' to set up a match pairing.")
        print("Type 'play' to play a match.")
        print("Type 'help' to view the documentation.")
        print("Type anything else to exit.")
        user_choice = input()
        print()
        uc_p = user_choice.lower()
        if (uc_p == "register"):
            team.Team()
        elif (uc_p == "pair"):
            pairing.Pairing()
        elif (uc_p == "play"):
            game.Game()
        elif (uc_p == "help"):
            h.help()
        else:
            play = False

main()