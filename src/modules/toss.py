import random
# Toss: The AI has a number in its mind. You select any number from 0 to 6.
# You also select whether the sum of these two numbers is odd or even.
# If your prediction is correct, you win the toss.
# Otherwise, you lose the toss.


def tossPlay():
    """ Toss for cricket matches, using the odd-or-even concept

    Arguments:
    None

    Returns:
    A string, either "bat" or "field"

    Description:
    The player must select an integer.
    Then, the bot will select either 0 or 1.
    The player must decide if the sum of these integers is odd or even.
    If the prediction is correct, the player wins the toss.
    Then, the player can choose batting or fielding (bowling)
    If the player loses the toss, or chooses something else,
        then the bot will choose whether to bat or field first.

    """

    play_start_with_possibilities = ["bat", "field"]
    print("Time for the toss!")
    # NOTE: We will not enforce the 0 to 6 constraint.
    # Generally, people play in that range.
    try:
        numInput = int(input("Choose a number between 0 and 6 (in [0, 6]): "))
    except:
        numInput = 0
    # Now decide whether the sum is Odd or Even.
    # If something else is typed, the player loses the toss.
    print("Odd or Even? NOTE: Zero is counted as even. ")
    print("The sum of your input and AI input is checked. ")
    print("The AI input is either 0 or 1. ")
    print("To win the toss, your prediction should be correct. ")
    turn = input("Either type 'Odd' or type 'Even': ")

    # Sum of the two input numbers = c
    c = (numInput + (random.randint(0, 1)))

    # The sum is actually even
    if c % 2 == 0:
        if turn == 'Even':
            print("You won the toss")
            toss = 1
        else:
            print("You lost the toss")
            toss = 0
    # The sum is actually odd
    else:
        if turn == 'Odd':
            print("You won the toss")
            toss = 1
        else:
            print("You lost the toss")
            toss = 0

    # Player wins the toss
    if toss == 1:
        choice = input("Choose to bat first or field first: ")
        # Ensure that bowling first redirects to fielding first
        if choice == "bowl":
            choice = "field"
        # Suppose the player types something else, randomly generate a decision
        if choice != "bat" and choice != "field":
            choice = play_start_with_possibilities[random.randint(0, 1)]
        print("You won the toss and chose to", choice, "first")

    # Player loses the toss
    else:
        opponent_input = random.randint(0, 1)
        if opponent_input == 0:
            choice = "bat"
            print("Your opponent won the toss and chose to field first")
        else:
            choice = "field"
            print("Your opponent won the toss and chose to bat first")
    # Return the choice
    return choice
