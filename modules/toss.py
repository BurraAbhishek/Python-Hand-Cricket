import random

# Toss: The AI has a number in its mind. You select any number from 0 to 6. You also select whether the sum of these two numbers is odd or even
# If your prediction is correct, you win the toss. Otherwise, you lose the toss.
def tossPlay():
    play_start_with_possibilities = ["bat","field"]
    print("Time for the toss!")
    # NOTE: We will not enforce the 0 to 6 constraint. Generally, people play in that range.
    try:
        numInput = int(input("Choose a number between 0 and 6: "))
    except:
        numInput=0
    # Now decide whether the sum is Odd or Even. If something else is input, the player loses the toss.
    turn = input("Odd or Even? zero is counted as even and the sum of your input and AI input is checked. ")

    # Sum of the numbers
    c=(numInput + (random.randint(0, 1)))

    # The sum is actually even
    if c%2 == 0:
        if turn == 'Even':
            print("You won the toss");
            toss=1
        else:
            print("You lost the toss");
            toss=0
    # The sum is actually odd
    else:
        if turn == 'Odd':
            print("You won the toss");
            toss=1
        else:
            print("You lost the toss");
            toss=0

    # Player wins the toss
    if toss==1:
        z=input("Choose to bat first or field first: ")
        # Ensure that bowling first redirects to fielding first
        if z=="bowl":
            z = "field"
        # Suppose the player types something else, randomly generate a decision.
        if z!="bat" and z!="field":
            z = play_start_with_possibilities[random.randint(0, 1)]
        print("You won the toss and chose to", z,"first");

    # Player loses the toss
    else:
        oinput=random.randint(0, 1)
        if oinput==0:
            z="bat"
            print("Your opponent won the toss and chose to field first")
        else:
            z="field"
            print("Your opponent won the toss and chose to bat first")
    # Return the choice
    return z
