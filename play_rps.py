import random


def game_time():
    user_input = input("Rock, paper, or scissors: ")
    rand = random.randrange(1, 3)
    valid_inputs = "rpsRPS"

    plays = {1: "r", 2: "p", 3: "s"}
    opponent_input = plays[rand]

    # check if valid input
    '''for char in valid_inputs:
        if user_input == char:
            break
    
    '''
    print("You:", user_input)
    print("Opponent:", opponent_input)

    if (user_input == "r" and opponent_input == "p") or (user_input == "s" and opponent_input == "r") or (
            user_input == "p" and opponent_input == "s"):
        print("Opponent wins!\n")
        return ("o")
    elif (user_input == "r" and opponent_input == "s") or (user_input == "p" and opponent_input == "r") or (
            user_input == "s" and opponent_input == "p"):
        print("You win!\n")
        return ("u")
    else:
        print("It's a tie!\n")
        return ("t")
